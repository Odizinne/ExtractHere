import sys
import os
import zipfile
from PyQt5.QtWidgets import QApplication, QFrame, QLabel, QProgressBar, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal, Qt

class ExtractionThread(QThread):
    update_progress = pyqtSignal(int)
    update_status = pyqtSignal(str)
    extraction_complete = pyqtSignal()

    def __init__(self, archive_paths):
        super().__init__()
        self.archive_paths = archive_paths

    def run(self):
        for archive_path in self.archive_paths:
            self.extract_archive(archive_path)

        self.extraction_complete.emit()

    def extract_archive(self, archive_path, extraction_dir=None):
        if extraction_dir is None:
            extraction_dir = os.path.splitext(archive_path)[0]

        if not os.path.exists(extraction_dir):
            os.makedirs(extraction_dir)

        try:
            with zipfile.ZipFile(archive_path, 'r') as archive:
                file_list = archive.namelist()
                total_files = len(file_list)
                self.update_status.emit(f"Extracting {os.path.basename(archive_path)}...")

                for i, file in enumerate(file_list, start=1):
                    archive.extract(file, extraction_dir)
                    progress = int(i / total_files * 100)
                    self.update_progress.emit(progress)

        except Exception as e:
            self.update_status.emit(f"Error extracting {os.path.basename(archive_path)}: {e}")

class ZipExtractorFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Extract here")
        self.setFixedSize(400, 100)

        self.status_label = QLabel("Waiting to extract files...")
        self.status_label.setWordWrap(True)
        self.progressbar = QProgressBar()

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.progressbar)
        self.setLayout(layout)

    def start_extraction(self, archive_paths):
        self.thread = ExtractionThread(archive_paths)
        self.thread.update_progress.connect(self.update_progressbar)
        self.thread.update_status.connect(self.update_status_label)
        self.thread.extraction_complete.connect(QApplication.instance().quit)
        self.thread.start()

    def update_progressbar(self, value):
        self.progressbar.setValue(value)

    def update_status_label(self, status):
        max_label_width = self.status_label.width()
        font_metrics = self.status_label.fontMetrics()
        elided_text = font_metrics.elidedText(status, Qt.ElideRight, max_label_width)
        self.status_label.setText(elided_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = ZipExtractorFrame()

    if len(sys.argv) > 1:
        archive_paths = sys.argv[1:]
        frame.start_extraction(archive_paths)
    else:
        frame.status_label.setText("No archive files provided.")
        print("No archive files provided.")

    frame.show()
    sys.exit(app.exec_())

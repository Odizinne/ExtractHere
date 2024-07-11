import sys
import os
import zipfile
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QThread, pyqtSignal

from design import Ui_MainWindow

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
                self.update_status.emit(f"Extracting {os.path.basename(archive_path)}")
                self.update_progress.emit(0)

                for i, file in enumerate(file_list, start=1):
                    archive.extract(file, extraction_dir)
                    progress = int(i / total_files * 100)
                    self.update_progress.emit(progress)
                    self.update_status.emit(f"{i} / {total_files}")

        except Exception as e:
            self.update_status.emit(f"Error extracting {os.path.basename(archive_path)}: {e}")

class ZipExtractorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.init_ui()

    def init_ui(self):
        self.ui.extractProgressBar.setValue(0)

    def start_extraction(self, archive_paths):
        for path in archive_paths:
            if not zipfile.is_zipfile(path):
                sys.exit(1)

        self.thread = ExtractionThread(archive_paths)
        self.thread.update_progress.connect(self.update_progressbar)
        self.thread.update_status.connect(self.update_status_label)
        self.thread.extraction_complete.connect(self.extraction_complete)
        self.thread.start()

    def update_progressbar(self, value):
        self.ui.extractProgressBar.setValue(value)

    def update_status_label(self, status):
        if status.startswith("Extracting"):
            self.ui.archiveLabel.setText(status)
            self.ui.statusLabel.setText("")
        else:
            self.ui.statusLabel.setText(status)

    def extraction_complete(self):
        self.ui.statusLabel.setText("Extraction complete.")
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ZipExtractorApp()

    if len(sys.argv) > 1:
        archive_paths = sys.argv[1:]
        window.start_extraction(archive_paths)
    else:
        sys.exit(1)

    window.show()
    sys.exit(app.exec())

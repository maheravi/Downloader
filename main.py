# This Python file uses the following encoding: utf-8
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtUiTools import QUiLoader
import random
import urllib.request


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.setWindowTitle("Download")
        self.ui.browse.clicked.connect(self.Browse)
        self.ui.download.clicked.connect(self.Download)
        self.ui.cancel.clicked.connect(self.Cancel)
        self.ui.show()

    def Download(self):
        url = self.ui.url.text()
        save = self.ui.download_des.text()

        try:
            urllib.request.urlretrieve(url, save, self.Report)
        except Exception:
            QMessageBox.warning(self, "Failed", "Cannot Download Yare")
            return

        QMessageBox.information(self, 'Done!', 'Download Complete')
        self.ui.progressBar.setValue(0)
        self.ui.url.setText("")
        self.ui.download_des.setText("")

    @staticmethod
    def Cancel(self):
        sys.exit(app.exec_())

    def Browse(self):
        location = QFileDialog.getSaveFileName(self, caption="Download Location", filter="All Files(*.*")
        self.ui.download_des.setText(location[0])

    def Report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if blocksize > 0:
            percent = readsofar * 100 / totalsize
            self.ui.progressBar.setValue(int(percent))


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    # window.show()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets, QtGui, QtCore


class PlaylistDialog(QtWidgets.QDialog):
    def __init__(self, data, title, parent=None):
        super().__init__(parent)
        self.data = data
        self.title = title

        self.setWindowTitle(f'Songs in {self.title}')
        self.setGeometry(550, 200, 500, 300)
        self.setMinimumSize(QtCore.QSize(500, 300))
        self.setMaximumSize(QtCore.QSize(500, 300))

        self.playlist_widget = QtWidgets.QListWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.playlist_widget)
        self.playlist_widget.addItems(data)

        # Customize the popup
        # Hide Scrollbars
        self.playlist_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playlist_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Customize the font
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(70)
        self.playlist_widget.setFont(font)

        # Change Window Colors
        self.setStyleSheet(
            "background-color: rgb(10, 25, 47)"
        )
        self.playlist_widget.setStyleSheet(
            "color: rgb(86, 227, 194);\n"
            "background-color: rgba(0, 0, 0, 100);\n"
            "selection-background-color: rgb(255, 140, 64);\n"
            "selection-color: rgb(255, 255, 255);\n"
            "padding:10px;\n"
        )


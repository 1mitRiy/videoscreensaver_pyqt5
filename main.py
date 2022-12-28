import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtMultimedia


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('form.ui', self)

        # TODO: Не забудьте изменить путь к видеозаставке и ширину с высотой!
        self.path_to_screensaver = './screensaver.mp4'
        # Ширина и высота видео-заставки.
        self.width_video = 640
        self.height_video = 360
        self.setFixedSize(self.width_video, self.height_video)

        # Запускаем заставку.
        self.media = QtMultimedia.QMediaPlayer(self)
        self.media.setVideoOutput(self.video)
        self.media.setMedia(
            QtMultimedia.QMediaContent(
                QtCore.QUrl.fromLocalFile(self.path_to_screensaver)
            )
        )
        self.media.play()

        # TODO: Обязательно скорректируйте громкость заставки!
        self.media.setVolume(5)

        # Отслеживаем статус видео, чтобы скрыть его после проигрывания.
        self.media.mediaStatusChanged.connect(self.hide_screensaver)

    def hide_screensaver(self, status):
        if status == QtMultimedia.QMediaPlayer.EndOfMedia:
            self.video.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

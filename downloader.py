import sys
import os
import yt_dlp
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QHBoxLayout, QButtonGroup


class DownloaderThread(QThread):
    progress = pyqtSignal(str)

    def __init__(self, url, output_format):
        super().__init__()
        self.url = url
        self.output_format = output_format

    def run(self):
        options = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.output_format,
                'preferredquality': '192',
            }],
            'progress_hooks': [self.progress_hook],
        }

        if self.output_format == "mp4":
            options['format'] = 'best'
            options['postprocessors'] = [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([self.url])

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            progress_info = f'{d ["_percent_str"]} {d ["_total_bytes_str"]} {d ["_speed_str"]}'.replace('[', ' ')
            self.progress.emit(progress_info)


class DownloaderWindow(QWidget):
    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        
        self.url_label = QLabel("Digite a URL do vídeo do YouTube:")
        vbox.addWidget(self.url_label)

        self.url_input = QLineEdit()
        vbox.addWidget(self.url_input)

        self.format_label = QLabel("Selecione o formato de saída:")
        vbox.addWidget(self.format_label)

        hbox = QHBoxLayout()

        self.mp3_radio = QRadioButton("MP3")
        self.mp3_radio.setChecked(True)
        hbox.addWidget(self.mp3_radio)

        self.mp4_radio = QRadioButton("MP4")
        hbox.addWidget(self.mp4_radio)

        vbox.addLayout(hbox)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.mp3_radio, 0)
        self.button_group.addButton(self.mp4_radio, 1)

        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.start_download)
        vbox.addWidget(self.download_button)

        self.progress_label = QLabel("Status da Execução")
        self.progress_label_2 = QLabel("Status do Download")
        

        vbox.addWidget(self.progress_label)
        vbox.addWidget(self.progress_label_2)

        self.setLayout(vbox)

    def start_download(self):
        
        url = self.url_input.text().strip()
        if not url:
            return
        self.progress_label.setStyleSheet("color: #f20538")
        
        output_format = "mp3" if self.mp3_radio.isChecked() else "mp4"

        self.progress_label.setText("Baixando!")
        

        self.downloader_thread = DownloaderThread(url, output_format)
        self.downloader_thread.progress.connect(self.update_progress_label)
        self.downloader_thread.finished.connect(self.download_finished)
        self.downloader_thread.start()
        
    def update_progress_label(self, progress_info):
        self.progress_label_2.setText(progress_info)
        self.progress_label_2.setStyleSheet("color: #042904")

    def download_finished(self):

        self.progress_label.setText("Download concluído!")
        self.progress_label.setStyleSheet("color: #042904")
        self.progress_label.setPalette(QApplication.palette())
        self.progress_label_2.setText("Status do Download")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DownloaderWindow()
    window.setWindowTitle("YouTube Video Downloader - MP3 / MP4")
    window.setFixedSize(400,200)
    window.show()

    sys.exit(app.exec_())


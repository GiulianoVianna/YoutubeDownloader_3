# Youtube Downloader 3
![image](https://user-images.githubusercontent.com/101942554/226234944-e7fcc281-1f2d-4210-a8f5-9e3ff3833f49.png)

## Informações

Downloader de vídeos do YouTube com uma interface gráfica de usuário (GUI) construída usando PyQt5. O usuário pode inserir a URL de um vídeo do YouTube, escolher o formato de saída desejado (MP3 para áudio ou MP4 para vídeo) e baixar o arquivo. A aplicação exibe o status do download em tempo real, mostrando a porcentagem, o tamanho total do arquivo e a velocidade de download.

O programa é dividido em duas classes principais:

DownloaderThread: Esta classe herda de QThread e é responsável por baixar o vídeo do YouTube usando a biblioteca yt_dlp. Ela aceita a URL do vídeo e o formato de saída como argumentos e emite sinais de progresso do download em tempo real.

DownloaderWindow: Esta classe herda de QWidget e implementa a interface gráfica do usuário. Ela contém várias widgets, como labels, botões de rádio, botões e campos de entrada de texto. A classe também define os métodos para iniciar o download, atualizar a label de progresso e lidar com a conclusão do download.

Quando o usuário clica no botão "Download", a aplicação inicia uma nova thread para baixar o vídeo e exibe o status do download em tempo real. Quando o download é concluído, a label de progresso é atualizada para mostrar "Download concluído!".

## Bibliotecas

sys </br>
os </br>
yt_dlp </br>
PyQt5.QtCore </br>
PyQt5.QtGui </br>
PyQt5.QtWidgets </br>

## Instalação das dependências
Execute o comando abaixo para instalar as bibliotecas necessárias:

<pre>
pip install yt-dlp

pip install PyQt5
</pre>

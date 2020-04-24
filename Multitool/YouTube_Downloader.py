import pytube

link = input('Ссылка на видео: ')
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download('video/')

import os

from PIL import Image
from pythumb import Thumbnail
from youtube_dl import YoutubeDL


class DataOfYoutubeLink:
    def __init__(self, url, type, quality):
        self.url = url
        self.pathThumb = ''
        self.path = ''
        self.title = ''
        self.format = ''
        self.quality = ''
        self.size = ''

        if type == 'mp4':
            if quality == '360':
                self.ytdl_opts = {'format': '134+140'}
            elif quality == '480':
                self.ytdl_opts = {'format': '135+140/134+140'}
            elif quality == '720':
                self.ytdl_opts = {'format': '136+140/135+140/134+140/22/17/18'}
            elif quality == '1080':
                self.ytdl_opts = {'format': '22/17/18'}
            else:
                pass

        elif type == 'mp3':
            pass

        self.ytdl_opts['progress_hooks'] = [self.my_hook]
        self.ytdl_opts['outtmpl'] = 'downloads/%(title)s.%(ext)s'
        self.ytdl = YoutubeDL(self.ytdl_opts)

    def get_thumb(self):
        thumb = Thumbnail(self.url)
        thumb.fetch()
        try:
            self.pathThumb = thumb.save(f'downloads/{self.pathThumb}')

            image = Image.open(self.pathThumb)
            new_image = image.resize((60, 40))
            new_image.save(self.pathThumb)

            return self.pathThumb

        except:
            pass

    def get_title(self):
        data = self.ytdl.extract_info(self.url, download=False)
        self.title = data['title']

        return self.title

    def get_info_about_download(self, type, quality):
        if type == 'mp4':
            if quality == '360':
                self.ytdl_opts = {'format': '134'}
            elif quality == '480':
                self.ytdl_opts = {'format': '135/134'}
            elif quality == '720':
                self.ytdl_opts = {'format': '136/135/134/22/17/18'}
            elif quality == '1080':
                self.ytdl_opts = {'format': '22/17/18'}


        elif type == 'mp3':
            pass

        ytdli = YoutubeDL(self.ytdl_opts)
        data = ytdli.extract_info(self.url, download=False)
        self.size = data['filesize']

        return round(self.size / 1000000, 2)

    def progress_download(self, d):
        pass

    def my_hook(self, d):
        if d['status'] == 'finished':
            file_tuple = os.path.split(os.path.abspath(d['filename']))
            print("Done downloading {}".format(file_tuple[1]))

        if d['status'] == 'downloading':
            p = d['_percent_str']
            p = p.replace('%', '')
            print(d['_percent_str'])

    def download(self, link):
        self.ytdl.download([link])
        print('done')

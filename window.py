from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from threading import Thread
from data_youtube import DataOfYoutubeLink

import regex


class MainWindow:
    def __init__(self, root):
        # CONFIGURE THE NOTEBOOK
        self.noteBook = ttk.Notebook(root)
        self.noteBook.configure(width=510, height=520)

        #################################### HOME PAGE ######################################################
        self.homePage = ttk.Frame(self.noteBook)

        self.youtubeImage = ImageTk.PhotoImage(Image.open('assets/youtube-icon-60.png'))
        self.nameLabel = ttk.Label(self.homePage, text='YOUTUBE  ', font='helvetica 20 italic',
                                   image=self.youtubeImage, compound=LEFT)
        self.nameLabel.configure(width=15, padding='20 40 0 0')

        # LINK TO DOWNLOAD
        self.linkVar = StringVar()
        self.linkValidation = self.homePage.register(self.link_validation)
        self.linkEntry = ttk.Entry(self.homePage, textvariable=self.linkVar, validate='focusout',
                                   validatecommand=self.link_validation)
        self.linkEntry.configure(width=40)

        self.downloadButtonImage = ImageTk.PhotoImage(Image.open('assets/download-button-icon-24.png'))
        self.downloadButton = ttk.Button(self.homePage, text='Download',
                                         image=self.downloadButtonImage, compound=RIGHT,
                                         command=self.action_download)

        # CHOSE TYPE OF THE DOWNLOAD
        self.typeLabel = ttk.Label(self.homePage, text='Chose the type')
        self.radioTypeVar = StringVar(self.homePage, 'mp4')
        self.radioTypeMP4 = ttk.Radiobutton(self.homePage, text='MP4', value='mp4', variable=self.radioTypeVar,
                                            command=self.update_quality_mp)
        self.radioTypeMP3 = ttk.Radiobutton(self.homePage, text='MP3', value='mp3', variable=self.radioTypeVar,
                                            command=self.update_quality_mp)

        self.lineDivisor = ttk.Separator(self.homePage, orient='horizontal')

        # CHOSE QUALITY OF THE DOWNLOAD
        self.qualityLabel = ttk.Label(self.homePage, text='Chose the quality')
        self.radioQualityVar = StringVar(self.homePage, '720')
        self.radioQ1MP = ttk.Radiobutton(self.homePage, text='360', value='360', variable=self.radioQualityVar)
        self.radioQ2MP = ttk.Radiobutton(self.homePage, text='480', value='480', variable=self.radioQualityVar)
        self.radioQ3MP = ttk.Radiobutton(self.homePage, text='720 HD', value='720', variable=self.radioQualityVar)
        self.radioQ4MP = ttk.Radiobutton(self.homePage, text='1080 FULL HD', value='1080',
                                         variable=self.radioQualityVar)

        # SHOW INFO ABOUT THE DOWNLOAD
        self.showInfoLabel = ttk.Label(self.homePage, text='', font='helvetica 10 italic')

        # STATUS OF INTERNET
        self.greenStatusImage = ImageTk.PhotoImage(Image.open('assets/green-status-icon-16.png'))
        self.yellowStatusImage = ImageTk.PhotoImage(Image.open('assets/yellow-status-icon-16.png'))
        self.redStatusImage = ImageTk.PhotoImage(Image.open('assets/red-status-icon-16.png'))
        self.statusConnection = ttk.Label(self.homePage, text='Disconnected', font='Arial 9', width=12,
                                          image=self.redStatusImage, compound=RIGHT)

        ############################## DOWNLOAD PAGE ################################################################

        ##################################### ADD PAGES TO THE NOTEBOOK #############################################
        self.homeImage = ImageTk.PhotoImage(Image.open('assets/home-icon-30.png'))
        self.noteBook.add(self.homePage, text='Home', image=self.homeImage, compound=LEFT)
        self.downloadImage = ImageTk.PhotoImage(Image.open('assets/download-icon-30.png'))
        self.noteBook.add(self.downloadPage, text='Downloads', image=self.downloadImage, compound=LEFT)

        #

        #
        self.draw_widgets()

    def draw_widgets(self):
        # DRAW THE NOTEBOOK
        self.noteBook.grid(row=0, column=0)

        # DRAW WIDGETS OF HOME PAGE
        # NAME APP
        self.nameLabel.grid(row=0, column=0)

        # LINK SPACE
        self.linkEntry.grid(row=1, column=0, columnspan=1, pady=(70, 0), padx=(30, 0), sticky='w')
        self.downloadButton.grid(row=1, column=1, pady=(70, 0), padx=(15, 0), sticky='w')

        # CHOSE TYPE OF DOWNLOAD
        self.typeLabel.grid(row=2, column=0, pady=(20, 0), padx=(0, 70), sticky='e')
        self.radioTypeMP4.grid(row=3, column=0, pady=(15, 0), padx=(150, 0), sticky='w')
        self.radioTypeMP3.grid(row=3, column=0, columnspan=2, pady=(15, 0), padx=(280, 0), sticky='w')

        self.lineDivisor.grid(row=4, column=0, columnspan=3, pady=(15, 0), padx=(17, 0), sticky='we')

        # CHOSE QUALITY OF DOWLOAD
        self.qualityLabel.grid(row=5, column=0, pady=(20, 0), padx=(0, 60), sticky='e')
        self.radioQ1MP.grid(row=6, column=0, columnspan=4, pady=(15, 0), padx=(30, 0), sticky='w')
        self.radioQ2MP.grid(row=6, column=0, columnspan=4, pady=(15, 0), padx=(125, 0), sticky='w')
        self.radioQ3MP.grid(row=6, column=0, columnspan=4, pady=(15, 0), padx=(230, 0), sticky='w')
        self.radioQ4MP.grid(row=6, column=0, columnspan=4, pady=(15, 0), padx=(350, 0), sticky='w')

        # SHOW INFO ABOUT THE DOWNLOAD
        self.showInfoLabel.grid(row=7, column=0, columnspan=4, pady=(30, 0), padx=(190, 0), sticky='we')

        # STATUS OF CONNECTION
        self.statusConnection.grid(row=8, columnspan=5, pady=(20, 0), padx=(0, 0), sticky='se')

        # DRAW WIDGETS OF DOWNLOAD PAGE

    def focus_in_link_entry(self, *args):
        pass

    def focus_out_link_entry(self, *args):
        pass

    def link_validation(self, *args):
        re = regex.compile(
            r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)('
            r'\S+)?$')
        if re.match(self.linkVar.get()):
            return True
        else:
            return False

    def update_quality_mp(self, *args):
        if self.radioTypeVar.get() == 'mp4':
            self.radioQ1MP['text'] = '360'
            self.radioQ1MP['value'] = '360'
            self.radioQ1MP['variable'] = self.radioQualityVar

            self.radioQ2MP['text'] = '480'
            self.radioQ2MP['value'] = '480'
            self.radioQ2MP['variable'] = self.radioQualityVar

            self.radioQ3MP['text'] = '720 HD'
            self.radioQ3MP['value'] = '720'
            self.radioQ3MP['variable'] = self.radioQualityVar

            self.radioQ4MP['text'] = '1080 FULL HD'
            self.radioQ4MP['value'] = '1080'
            self.radioQ4MP['variable'] = self.radioQualityVar

            self.radioQualityVar.set('720')

        elif self.radioTypeVar.get() == 'mp3':
            # self.radioQ1MP['text'] = 'BAIXA'
            # self.radioQ1MP['value'] = '48'
            # self.radioQ1MP['variable'] = self.radioQualityVar
            #
            # self.radioQ2MP['text'] = 'NORMAL'
            # self.radioQ2MP['value'] = '128'
            # self.radioQ2MP['variable'] = self.radioQualityVar
            #
            # self.radioQ3MP['text'] = 'ALTA'
            # self.radioQ3MP['value'] = '256'
            # self.radioQ3MP['variable'] = self.radioQualityVar
            #
            # self.radioQ4MP['text'] = 'MELHOR'
            # self.radioQ4MP['value'] = '257'
            # self.radioQ4MP['variable'] = self.radioQualityVar
            #
            # self.radioQualityVar.set('257')

            pass

    # FUNCTIONS
    def action_download(self, *args):
        # VERIRY THE PATTERN LINK
        if not self.link_validation():
            messagebox.showerror('Invalid link', 'Please insert a valid link')
        else:
            # SEND DOWNLOAD TO DOWNLOAD PAGE
            yt = DataOfYoutubeLink(self.linkVar.get(),
                                   self.radioTypeVar.get(),
                                   self.radioQualityVar.get())

            print(yt.get_title())
            print(yt.get_thumb())
            print(f'{yt.get_info_about_download(self.radioTypeVar.get(), self.radioQualityVar.get())} MB')

            Thread(self.download_tread(yt)).start()

            # SHOW DOWNLOAD INFO RESPONSE
            self.showInfoLabel['text'] = 'Download added'
            self.showInfoLabel.after(5000, self.update_show_info)

    def update_show_info(self):
        self.showInfoLabel['text'] = ''

    def download_tread(self, youtube):
        link = self.linkVar.get().strip()
        youtube.download(link)
        messagebox.showinfo('Donwload', 'Your download is complete')

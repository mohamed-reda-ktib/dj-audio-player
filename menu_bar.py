#stander libraries import
import wx


#the menu bar class
class MenuBar(wx.MenuBar):
    """The menu bar class.
    It contains all menu bar widgets and methods related to them.
    """
    #constructor
    def __init__(self, music_list, audio_list):
        """The constructor of the class.
        It initializes the class and calls all necessary methods to add the menu bar to the frame.
        This method has 2 parameters:
        -music_list: a widget of a wx list where the music tracks will be made,
        -and audio_list: a widget of a wx list where the short audio tracks will be made.
        """
        super().__init__()
        self.music_list = music_list
        self.audio_list = audio_list
        #calling methods
        self.menu_bar_items()


    #menu Bar items
    def menu_bar_items(self):
        """Adding menu Bar items.
        This method adds different menus and their items.
        It also bind every item with its method to carry out the requested operation.
        Menus and their items are as follow:
        -file menu: open music, open short audios, exit.
        """
        #file menu
        file_menu = wx.Menu()
        open_music_item = file_menu.Append(wx.ID_ANY, _('Open Music')+'\tCTRL+O', _('Open one or more music files'))
        open_audio_item = file_menu.Append(wx.ID_ANY, _('Open Short Audios')+'\tCTRL+SHIFT+O', _('Open one or more short audio files'))
        exit_item = file_menu.Append(wx.ID_EXIT, 'Exit', 'Exit the program')
        self.Append(file_menu, '&File')
        #binding file menu items
        self.Bind(wx.EVT_MENU, self.open_music, open_music_item)
        self.Bind(wx.EVT_MENU, self.open_short_audios, open_audio_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)
        
    #open music to be played
    def open_music(self, e):
        """Open music to be played.
        This method opens one or more music tracks and makes them in the music list.
        """
        pass

    #open short audios to be played
    def open_short_audios(self, e):
        pass

    #exit the program
    def on_exit(self, e):
        wx.Exit()

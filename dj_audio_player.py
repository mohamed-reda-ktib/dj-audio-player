#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Wed Mar 15 21:56:59 2023
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainPanel.__init__
        kwds["style"] = kwds.get("style", 0)
        wx.Panel.__init__(self, *args, **kwds)

        main_HS = wx.BoxSizer(wx.HORIZONTAL)

        main_VS = wx.BoxSizer(wx.VERTICAL)
        main_HS.Add(main_VS, 1, wx.ALL | wx.EXPAND, 5)

        info_HS = wx.BoxSizer(wx.HORIZONTAL)
        main_VS.Add(info_HS, 1, wx.BOTTOM | wx.EXPAND, 5)

        aud_title_lbl = wx.StaticText(self, wx.ID_ANY, _("Audio title"))
        info_HS.Add(aud_title_lbl, 1, wx.ALL | wx.EXPAND, 5)

        duration_lbl = wx.StaticText(self, wx.ID_ANY, _("Duration"))
        info_HS.Add(duration_lbl, 1, wx.ALL | wx.EXPAND, 5)

        time_passed_lbl = wx.StaticText(self, wx.ID_ANY, _("Time passed"))
        info_HS.Add(time_passed_lbl, 1, wx.ALL | wx.EXPAND, 5)

        time_remaining_lbl = wx.StaticText(self, wx.ID_ANY, _("Time remaining"))
        info_HS.Add(time_remaining_lbl, 1, wx.ALL | wx.EXPAND, 5)

        previous_media_lbl = wx.StaticText(self, wx.ID_ANY, _("Previous media title"))
        info_HS.Add(previous_media_lbl, 1, wx.ALL | wx.EXPAND, 5)

        next_media_lbl = wx.StaticText(self, wx.ID_ANY, _("Next media title"))
        info_HS.Add(next_media_lbl, 1, wx.ALL | wx.EXPAND, 5)

        main_ctrl_HS = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Main playback device")), wx.HORIZONTAL)
        main_VS.Add(main_ctrl_HS, 1, wx.EXPAND, 0)

        main_ctrl_GS = wx.GridBagSizer(5, 5)
        main_ctrl_HS.Add(main_ctrl_GS, 1, wx.BOTTOM | wx.TOP, 5)

        self.rewind_btn = wx.Button(self, wx.ID_ANY, _("Rewind"))
        main_ctrl_GS.Add(self.rewind_btn, (0, 0), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.pause_btn = wx.ToggleButton(self, wx.ID_ANY, _("Pause/play"))
        main_ctrl_GS.Add(self.pause_btn, (0, 1), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.fast_btn = wx.Button(self, wx.ID_ANY, _("fast forward"))
        main_ctrl_GS.Add(self.fast_btn, (0, 2), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.previous_btn = wx.Button(self, wx.ID_ANY, _("Previous item"))
        main_ctrl_GS.Add(self.previous_btn, (1, 0), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.stop_btn = wx.ToggleButton(self, wx.ID_ANY, _("Stop/play"))
        main_ctrl_GS.Add(self.stop_btn, (1, 1), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.next_btn = wx.Button(self, wx.ID_ANY, _("Next item"))
        main_ctrl_GS.Add(self.next_btn, (1, 2), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        monitoring_ctrl_HS = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Monitoring playback device")), wx.HORIZONTAL)
        main_VS.Add(monitoring_ctrl_HS, 1, wx.EXPAND, 0)

        monitoring_ctrl_GS = wx.GridBagSizer(5, 5)
        monitoring_ctrl_HS.Add(monitoring_ctrl_GS, 1, wx.BOTTOM | wx.TOP, 5)

        self.rewind_btn_copy = wx.Button(self, wx.ID_ANY, _("Rewind"))
        monitoring_ctrl_GS.Add(self.rewind_btn_copy, (0, 0), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.pause_btn_copy = wx.ToggleButton(self, wx.ID_ANY, _("Pause/play"))
        monitoring_ctrl_GS.Add(self.pause_btn_copy, (0, 1), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.fast_btn_copy = wx.Button(self, wx.ID_ANY, _("fast forward"))
        monitoring_ctrl_GS.Add(self.fast_btn_copy, (0, 2), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.previous_btn_copy = wx.Button(self, wx.ID_ANY, _("Previous item"))
        monitoring_ctrl_GS.Add(self.previous_btn_copy, (1, 0), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.stop_btn_copy = wx.ToggleButton(self, wx.ID_ANY, _("Stop/play"))
        monitoring_ctrl_GS.Add(self.stop_btn_copy, (1, 1), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.next_btn_copy = wx.Button(self, wx.ID_ANY, _("Next item"))
        monitoring_ctrl_GS.Add(self.next_btn_copy, (1, 2), (1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        aud_list_VS = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Music list")), wx.VERTICAL)
        main_HS.Add(aud_list_VS, 1, wx.EXPAND, 0)

        aud_list_GS = wx.FlexGridSizer(2, 2, 3, 5)
        aud_list_VS.Add(aud_list_GS, 1, wx.EXPAND, 0)

        music_list_lbl = wx.StaticText(self, wx.ID_ANY, _("Music list"))
        aud_list_GS.Add(music_list_lbl, 0, 0, 0)

        self.music_list = wx.ListBox(self, wx.ID_ANY, choices=[_("choice 1")])
        self.music_list.SetSelection(0)
        aud_list_GS.Add(self.music_list, 1, wx.ALL | wx.EXPAND, 5)

        audio_list_lbl = wx.StaticText(self, wx.ID_ANY, _("Short audios list"))
        aud_list_GS.Add(audio_list_lbl, 0, 0, 0)

        self.audio_list = wx.ListBox(self, wx.ID_ANY, choices=[_("choice 1")])
        self.audio_list.SetSelection(0)
        aud_list_GS.Add(self.audio_list, 1, wx.ALL | wx.EXPAND, 5)

        aud_list_VS.Add((0, 0), 0, 0, 0)

        aud_list_GS.AddGrowableCol(1)

        self.SetSizer(main_HS)

        self.Layout()
        # end wxGlade

# end of class MainPanel

class DJAudioPlayer(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: DJAudioPlayer.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1296, 696))
        self.SetTitle(_("DJ Audio Player"))

        # Menu Bar
        self.menu_bar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_OPEN, _("Open music"), "")
        self.Bind(wx.EVT_MENU, self.wx, id=wx.ID_OPEN)
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _("Open short audios"), "")
        self.Bind(wx.EVT_MENU, self.wx, item)
        self.menu_bar.Append(wxglade_tmp_menu, _("Open"))
        self.SetMenuBar(self.menu_bar)
        # Menu Bar end

        self.main_pnl = MainPanel(self, wx.ID_ANY)
        self.Layout()
        self.Centre()

        # end wxGlade

    def wx(self, event):  # wxGlade: DJAudioPlayer.<event_handler>
        print("Event handler 'wx' not implemented!")
        event.Skip()

# end of class DJAudioPlayer

class SettingsDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SettingsDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle(_("Settings"))

        main_settings_VS = wx.BoxSizer(wx.VERTICAL)

        main_device_HS = wx.BoxSizer(wx.HORIZONTAL)
        main_settings_VS.Add(main_device_HS, 1, wx.EXPAND, 0)

        main_devices_lbl = wx.StaticText(self, wx.ID_ANY, _("Choice main device playback"))
        main_device_HS.Add(main_devices_lbl, 0, 0, 0)

        self.Main_devices_list = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        main_device_HS.Add(self.Main_devices_list, 1, wx.EXPAND, 0)

        monitoring_device_HS = wx.BoxSizer(wx.HORIZONTAL)
        main_settings_VS.Add(monitoring_device_HS, 1, wx.EXPAND, 0)

        monitoring_devices_lbl = wx.StaticText(self, wx.ID_ANY, _("Choice monitoring device playback"))
        monitoring_device_HS.Add(monitoring_devices_lbl, 0, 0, 0)

        self.monitoring_devices_list = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        monitoring_device_HS.Add(self.monitoring_devices_list, 1, wx.EXPAND, 0)

        buttons_SDBS = wx.StdDialogButtonSizer()
        main_settings_VS.Add(buttons_SDBS, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.cancel_btn = wx.Button(self, wx.ID_CANCEL, "")
        buttons_SDBS.AddButton(self.cancel_btn)

        self.ok_btn = wx.Button(self, wx.ID_OK, "")
        self.ok_btn.SetDefault()
        buttons_SDBS.AddButton(self.ok_btn)

        self.apply_btn = wx.Button(self, wx.ID_APPLY, "")
        buttons_SDBS.AddButton(self.apply_btn)

        buttons_SDBS.Realize()

        self.SetSizer(main_settings_VS)
        main_settings_VS.Fit(self)

        self.SetAffirmativeId(self.ok_btn.GetId())
        self.SetEscapeId(self.cancel_btn.GetId())

        self.Layout()
        self.Centre()
        # end wxGlade

# end of class SettingsDialog

class MyApp(wx.App):
    def OnInit(self):
        self.DJ_audio_player = DJAudioPlayer(None, wx.ID_ANY, "")
        self.SetTopWindow(self.DJ_audio_player)
        self.DJ_audio_player.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()

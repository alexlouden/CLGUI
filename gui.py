#-------------------------------------------------------------------------------
# Name:        CL GUI
# Purpose:
#
# Author:      Alex Louden
#
# Created:     02/12/2012
# Copyright:   (c) Alex Louden 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import wx
from controller import Controller

helptext = "Help!"

class MainFrame(wx.Frame):
    def __init__(self, controller):

        # Store controller reference in object for access in other functions
        self.controller = controller

        # Create frame
        wx.Frame.__init__(self, None, title="Commandline GUI Template",  size=(400, 400))

        # Create the controls, and recieve the frame sizer
        sizer = self.create_controls()

        # Add sizer to frame
        self.SetSizer(sizer)

        # Show frame
        self.Show(True)

    def create_controls(self):

        # Add control (textbox) and display (Label)
        self.control = wx.TextCtrl(self)
        self.display = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_READONLY)

        # Add a callback function to handle key presses
        self.control.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)

        # And another to handle when the text is changed
        self.control.Bind(wx.EVT_TEXT, self.onTextChanged)

        # Sizer - this is used to handle the sizing of the elements in this frame
        boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

        # Add elements to sizer
        boxSizer.Add(self.control, border=5, flag=wx.ALL|wx.EXPAND)
        boxSizer.Add(self.display, 1, border=5, flag=wx.EXPAND)

        return boxSizer

    def onKeyPress(self, event=None):
        """Handle keypress events for self.control"""

        # Check to see if enter was pressed
        if event.GetKeyCode() == 13:
            # Run controller
            self.run()
            # Clear control
            self.control.SetLabel('')
            return

        # Check to see if ? was pressed
        if event.GetKeyCode() == 47 and event.ShiftDown():
            # Show help
            self.show_help()
            return

        # Skip event, so it gets passed to text control
        event.Skip()

    def onTextChanged(self, event=None):
        """Handle text changed events for self.control"""
        pass

    def run(self):
        """Run controller, display result"""
        result = self.controller.run(self.control.GetLabel())
        self.log(result)

    def show_help(self):
        """Displays some help text"""
        self.log(helptext)

    def log(self, text):
        """Logs text to the display box"""
        self.display.AppendText(text + '\n')

def main():
    app = wx.App(False)
    controller = Controller()
    frame = MainFrame(controller)
    app.SetTopWindow(frame)
    app.MainLoop()

if __name__ == '__main__':
    main()


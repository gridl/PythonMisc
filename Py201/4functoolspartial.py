# use partial to create a new function with partial application of the arguments and the keywords that you pass to it
#
# from functools import partial
# def add(x,y):
#     return x + y
#
# p_add = partial(add, 2)
# p_add(4)


# handy use case fo partials is to pass arguments to  callbacks

import wx
from functools import partial

class MainFrame(wx.Frame):
    """ This app shows a group of buttons
    """

    def __init__(self, *args, **kwargs):
        #constructor
        super(MainFrame, self).__init__(parent=None, title='Partial')
        panel= wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        btn_labels = ['one','two','three']
        for label in btn_labels:
            btn = wx.Button(panel, label=label)
            btn.Bind(wx.EVT_BUTTON, partial(self.onButton, label=label))

        panel.SetSizer(sizer)
        self.show()

    def onButton(self, event, label):
        print("YOu pressed " + str(label))

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
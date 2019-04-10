import wikipedia
import wolframalpha
import wx

# Main class for GUI App frame

class MyFrame(wx.Frame):
    def __init__(self):

# Create basic GUI info about the app

        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style= wx.DEFAULT_FRAME_STYLE,
            title="Sofia the Virtual Assistant")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(panel,
        label="Hello! I am Sofia, your Virtual Assistant. Ask me anything!")
        sizer.Add(label, 0, wx.ALL , 5)

# Simple text box with properties for input

        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(450, 30))
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(sizer)
        self.Show()

# Defines OnEnter function to allow user input. The textbox temprarily stores the input using self.txt.GetValue() and converts it to lowercase

    def OnEnter(self):
        input = self.txt.GetValue()
        input = input.lower()

# Try and Except tell the code to use the Wolfram Alpha API or Wikipedia to answer user questions. If it takes longer, it is using wikipedia
        try:
            app_id = "V4A828-6KPHLHK858"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print(answer)
        except:
            print(wikipedia.summary(input))
# this code runs the app 
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()

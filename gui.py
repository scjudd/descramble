#!/usr/bin/env python2

import wx

class SolutionsFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,200))

        self.canvas = wx.Panel(self, -1, (0, 0), (200,200))
        self.canvas.Bind(wx.EVT_PAINT, self.RepaintCanvas)

        self.listbox = wx.ListBox(self, -1, (200, 0), (200,200))
        self.listbox.Bind(wx.EVT_LISTBOX, self.RepaintCanvas)

    def RepaintCanvas(self, event):
        self.PaintBackground()
        self.DrawCurPath()

    def PaintBackground(self):
        bmp = wx.Bitmap('resources/images/background.png')

        dc = wx.PaintDC(self.canvas)
        dc.DrawBitmap(bmp, 0, 0)

    def DrawCurPath(self):
        cur_selection = self.listbox.GetSelection()
        cur_path = self.listbox.GetClientData(cur_selection)

        dc = wx.PaintDC(self.canvas)
        dc.SetPen(wx.Pen(wx.RED, 4))

        for i in xrange(0,len(cur_path)-1):
            path = cur_path[i:i+2]
            x1, y1 = map(lambda c: c*50+25, path[0])
            x2, y2 = map(lambda c: c*50+25, path[1])
            dc.DrawLine(x1, y1, x2, y2)

        x, y = map(lambda c: c*50+25, cur_path[0])
        dc.DrawCircle(x, y, 10)

    def SetResults(self, results):
        for r in results:
            self.listbox.Append('%s - %s' % (r[0], r[1]['score']),
                    clientData=r[1]['path'])

        self.listbox.SetSelection(0)

if __name__ == '__main__':
    from graph import build_graph
    from trie import build_trie
    from scramble import solve

    import sys
    graph = build_graph(sys.argv[1])

    with open('resources/word_lists/TWL_2006_ALPHA.txt') as word_list:
        trie = build_trie(word_list)

    results = solve(graph, trie)
    sorted_results = sorted(results.iteritems(), key=lambda w:w[1]['score'],
                            reverse=True)

    app = wx.App(False)
    frame = SolutionsFrame(None, 'Scramble Solver')
    frame.SetResults(sorted_results)
    frame.Show(True)
    app.MainLoop()

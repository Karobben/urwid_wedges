'''
https://github.com/bavanduong/urwid-example/blob/master/clock.py
'''
import urwid
import time
import sys


def Tim():
    A = str(time.time())
    return A

def keypress(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

def refresh(loop=None, data=None):
    #self.setup_view()
    #loop.widget = self.view
    loop.set_alarm_in(3, refresh)
    col.contents[0] = (urwid.Filler(urwid.Text(str(Tim()))), col.options())

clock_txt = urwid.Text(Tim())
view = urwid.Padding(clock_txt, 'center')
view = urwid.AttrMap(view, 'body')
view = urwid.Filler(view, 'middle')
view = urwid.Pile([view,view,view,view,view,view])
col = urwid.Columns([view,view])
col2 = urwid.Columns([view,view])
w = urwid.ListBox(urwid.SimpleListWalker([clock_txt]))

loop = urwid.MainLoop(col, palette=[('body', 'dark cyan', '')],
    unhandled_input=keypress)
loop.set_alarm_in(1, refresh)
loop.run()


class Refresh:

    def setup_view(self):
        A = Tim()
        self.view = w

    def main(self):
        #self.setup_view()
        loop = urwid.MainLoop(
            self.view, palette=[('body', 'dark cyan', '')],
            unhandled_input=self.keypress)
        loop.set_alarm_in(1, self.refresh)
        loop.run()

    def refresh(self, loop=None, data=None):
        #self.setup_view()
        loop.widget = self.view
        loop.set_alarm_in(3, self.refresh)
        #col.contents[0] = (urwid.Filler(urwid.Text(str(Tim()))), col.options())


#if __name__ == '__main__':
    #refresh = Refresh()
    #sys.exit(refresh.main())

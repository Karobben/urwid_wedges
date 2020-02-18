'''
https://github.com/bavanduong/urwid-example/blob/master/clock.py
'''
import urwid
import time
import sys


def Tim():
    A = str(time.time())
    return A

clock_txt = urwid.Text(Tim())
view = urwid.Padding(clock_txt, 'center')
view = urwid.AttrMap(view, 'body')
view = urwid.Filler(view, 'middle')

class Refresh:
    def keypress(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
    def setup_view(self):
        A = Tim()
        self.view = view

    def main(self):
        self.setup_view()
        loop = urwid.MainLoop(
            self.view, palette=[('body', 'dark cyan', '')],
            unhandled_input=self.keypress)
        loop.set_alarm_in(1, self.refresh)
        loop.run()

    def refresh(self, loop=None, data=None):
        self.setup_view()
        loop.widget = self.view
        loop.set_alarm_in(0.2, self.refresh)


if __name__ == '__main__':
    refresh = Refresh()
    sys.exit(refresh.main())

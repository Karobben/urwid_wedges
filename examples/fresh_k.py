'''
https://stackoverflow.com/questions/12044463/urwid-doesnt-update-screen-on-loop-draw-screen
'''

import urwid
from random import randint
import logging
from time import sleep
logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.CRITICAL, filename = u'mylog.log')

class ArRow (urwid.WidgetWrap):
    def __init__ (self):
        self.build_row()
        self._w = urwid.Columns(self.item)
        self.__super.__init__(self._w)
    def build_row(self):
        w=5
        self.item = [
            ('fixed',w,urwid.AttrWrap(urwid.Text(str(randint(1,100))), 'body', 'focus')),
            ('fixed',w,urwid.AttrWrap(urwid.Text(str(randint(1,100))), 'body', 'focus')),
            ('fixed',w,urwid.AttrWrap(urwid.Text(str(randint(1,100))), 'body', 'focus')),
        ]
    def refresh(self):
        self.build_row()
        self._w = urwid.Columns(self.item)
        #self.__super.__init__(w)
        logging.critical(str(self.item))
    def selectable (self):
        return True
    def keypress(self, size, key):
        return key

palette = [
    ('body','dark cyan', '', 'standout','#0f6',''),
    ('focus','dark red', '', 'standout','light red',''),
    ]

def keystroke (input):
    if input in ('q', 'Q'):
        raise urwid.ExitMainLoop()

items=[ArRow()]#,ArRow(),ArRow(),ArRow(),ArRow()]
listbox = urwid.ListBox(urwid.SimpleListWalker(items))
view = urwid.Frame(urwid.AttrWrap(listbox, 'body'))
loop = urwid.MainLoop(view, palette, unhandled_input=keystroke)
loop.screen.set_terminal_properties(colors=256)

def live_report(*a):
    while True:
        items[0].refresh()
        loop.draw_screen()
        sleep(2)
def refresh(_loop,_data):
    for item in items:
        item.refresh()
    #loop.draw_screen()
    _loop.set_alarm_in(2,refresh)

loop.set_alarm_in(2,refresh)
loop.run()

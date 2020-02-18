#!/usr/bin/env python

import urwid

def on_exit_clicked(button):
    raise urwid.ExitMainLoop()


class PopUpDialog(urwid.WidgetWrap):
    """A dialog that appears with nothing but a close button """
    signals = ['close']

    def __init__(self):
        # button 1
        close_button = urwid.Button("that's NOT COOL")
        urwid.connect_signal(close_button, 'click',
            lambda button:self._emit("close"))
        # button 2
        button = urwid.Button(u'Exit')
        urwid.connect_signal(button, 'click', on_exit_clicked)

        pile = urwid.Pile([urwid.Text(
            "^^  I'm attached to the widget that opened me. "
            "Try resizing the window!\n"),
            urwid.Columns([
                urwid.Padding(close_button, 'left'),
                urwid.Padding(button, 'right', 8),
            ]),
            ])
        fill = urwid.Filler(pile)
        self.__super.__init__(urwid.AttrWrap(fill, 'popbg'))


class ThingWithAPopUp(urwid.PopUpLauncher):
    def __init__(self):
        self.__super.__init__(urwid.Button("click-me"))
        urwid.connect_signal(self.original_widget, 'click',
            lambda button: self.open_pop_up())

    def create_pop_up(self):
        pop_up = PopUpDialog()
        urwid.connect_signal(pop_up, 'close',
            lambda button: self.close_pop_up())
        return pop_up

    def get_pop_up_parameters(self):
        return {'left':0, 'top':1, 'overlay_width':32, 'overlay_height':7}


button = urwid.Button(u'Exit')
urwid.connect_signal(button, 'click', on_exit_clicked)

body_A = [urwid.Padding(ThingWithAPopUp(), 'center', 15),button]

pile = urwid.Pile(body_A)
col = urwid.Columns([pile,urwid.Text("│"),('fixed',14,pile)])
fill = urwid.Filler(col)
loop = urwid.MainLoop(
    fill,
    [('popbg', 'white', 'dark blue')],
    pop_ups=True)
loop.run()

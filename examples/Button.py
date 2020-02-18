from __future__ import print_function, absolute_import, division
import urwid

'''
https://stackoverflow.com/questions/52252730/how-do-you-make-buttons-of-the-python-library-urwid-look-pretty
'''

PALETTE = [
    ('normal', '', ''),
    ('bold', 'bold', ''),
    ('blue', 'bold', 'dark blue'),
    ('highlight', 'black', 'dark blue'),
]


def show_or_exit(key):
    if key in ('q', 'Q', 'esc'):
        raise urwid.ExitMainLoop()


class CustomButton(urwid.Button):
    button_left = urwid.Text('[')
    button_right = urwid.Text(']')


def custom_button(*args, **kwargs):
    b = CustomButton(*args, **kwargs)
    b = urwid.AttrMap(b, '', 'highlight')
    b = urwid.Padding(b, left=4, right=4)
    return b


class BoxButton(urwid.WidgetWrap):
    _border_char = u'─'
    def __init__(self, label, on_press=None, user_data=None):
        padding_size = 2
        border = self._border_char * (len(label) + padding_size * 2)
        cursor_position = len(border) + padding_size

        self.top = u'┌' + border + u'┐\n'
        self.middle = u'│  ' + label + u'  │\n'
        self.bottom = u'└' + border + u'┘'

        # self.widget = urwid.Text([self.top, self.middle, self.bottom])
        self.widget = urwid.Pile([
            urwid.Text(self.top[:-1]),
            urwid.Text(self.middle[:-1]),
            urwid.Text(self.bottom),
        ])

        self.widget = urwid.AttrMap(self.widget, '', 'highlight')

        # self.widget = urwid.Padding(self.widget, 'center')
        # self.widget = urwid.Filler(self.widget)

        # here is a lil hack: use a hidden button for evt handling
        self._hidden_btn = urwid.Button('hidden %s' % label, on_press, user_data)

        super(BoxButton, self).__init__(self.widget)

    def selectable(self):
        return True

    def keypress(self, *args, **kw):
        return self._hidden_btn.keypress(*args, **kw)

    def mouse_event(self, *args, **kw):
        return self._hidden_btn.mouse_event(*args, **kw)


if __name__ == '__main__':
    header = urwid.Text('Header')
    footer = urwid.Text('Footer')
    onclick = lambda w: footer.set_text('clicked: %r' % w)
    widget = urwid.Pile([
        header,
        urwid.Text('Simple custom buttons:'),
        urwid.Columns([
            custom_button('OK', on_press=onclick),
            custom_button('Cancel', on_press=onclick),
        ]),
        urwid.Text('Box bordered buttons:'),
        urwid.Columns([
            urwid.Padding(BoxButton('OK', on_press=onclick), left=4, right=4),
            BoxButton('Cancel', on_press=onclick),
        ]),
        footer,
    ])
    widget = urwid.Filler(widget, 'top')
    loop = urwid.MainLoop(widget, PALETTE, unhandled_input=show_or_exit)
    loop.run()

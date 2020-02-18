import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def on_ask_change(edit, new_edit_text):
    Result =  new_edit_text


def on_Send(new_edit_text):
    Result = str(edit)[30:-31]


def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

edit = urwid.Edit(u"发送弹幕\n")
button = urwid.Button(u'发送')


fill = urwid.Pile([edit,button,button2])
fill = urwid.Filler(fill)


urwid.connect_signal(edit, 'change', on_ask_change)
urwid.connect_signal(button, 'click', on_Send)

loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()

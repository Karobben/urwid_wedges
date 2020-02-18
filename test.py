#!/usr/local/bin/python3.7


import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()



palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]

# Columns
txt1 = urwid.Text(('banner', u" Hello World "), align='center')
txt = urwid.Pile([txt1,txt1])
map1 = urwid.Columns([txt,('fixed',16,txt)], 3,focus_column=1)
fill = urwid.Filler(map1)

def on_ask_change(edit, new_edit_text):
    print(new_edit_text)

ask = urwid.Edit(('I say', u"What is your name?\n"))
urwid.connect_signal(ask, 'change', on_ask_change)

fill = urwid.ListBox(urwid.SimpleListWalker([ask,txt,map1]))
map2 = urwid.AttrMap(fill, 'header')

#header
hdr = urwid.Text("Urwid BigText example program - F8 exits.\nsdfsdfsdf\n523423")
hdr = urwid.AttrWrap(hdr, 'header')

W = urwid.Frame(header=hdr, body=map2)
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
loop.run()

'''
                     //
         \\         //
          \\       //
    ##DDDDDDDDDDDDDDDDDDDDDD##
    ## DDDDDDDDDDDDDDDDDDDD ##   ________   ___   ___        ___   ________   ___   ___        ___
    ## hh                hh ##   |\   __  \ |\  \ |\  \      |\  \ |\   __  \ |\  \ |\  \      |\  \
    ## hh    //    \\    hh ##   \ \  \|\ /_\ \  \\ \  \     \ \  \\ \  \|\ /_\ \  \\ \  \     \ \  \
    ## hh   //      \\   hh ##    \ \   __  \\ \  \\ \  \     \ \  \\ \   __  \\ \  \\ \  \     \ \  \
    ## hh                hh ##     \ \  \|\  \\ \  \\ \  \____ \ \  \\ \  \|\  \\ \  \\ \  \____ \ \  \
    ## hh      wwww      hh ##      \ \_______\\ \__\\ \_______\\ \__\\ \_______\\ \__\\ \_______\\ \__\
    ## hh                hh ##       \|_______| \|__| \|_______| \|__| \|_______| \|__| \|_______| \|__|
    ## MMMMMMMMMMMMMMMMMMMM ##
    ##MMMMMMMMMMMMMMMMMMMMMM##                             Release 2.6.1. Powered by jinkela-core 2.5.3.
         \/            \/
'''

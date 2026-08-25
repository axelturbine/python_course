import curses

def main(screen):
    screen.addstr(0, 0, "Curses is working!")
    screen.refresh()
    screen.getch()

curses.wrapper(main)
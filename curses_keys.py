import curses
import time

def main(screen):
    screen.nodelay(True)
    counter = 0
    
    while True:
        key = screen.getch()
        
        if key == ord('q'):
            break
        elif key == curses.KEY_LEFT:
            screen.addstr(2, 0, "You pressed LEFT! ")
        elif key == curses.KEY_RIGHT:
            screen.addstr(2, 0, "You pressed RIGHT!")
        
        counter += 1
        screen.addstr(0, 0, f"Counter: {counter}")
        screen.refresh()
        time.sleep(0.1)

curses.wrapper(main)
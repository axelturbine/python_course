import curses
import random
import time
import json

def load_scores():
    try:
        with open("car_scores.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_scores(scores):
    with open("car_scores.json", "w") as file:
        json.dump(scores, file)

def countdown(screen):
    for i in [3, 2, 1]:
        screen.clear()
        screen.addstr(4, 4, "GET READY!")
        screen.addstr(6, 5, f"    {i}    ")
        screen.refresh()
        time.sleep(1)
    screen.clear()
    screen.addstr(5, 4, "   GO!   ")
    screen.refresh()
    time.sleep(0.5)

def game(screen):
    curses.curs_set(0)
    screen.nodelay(True)
    
    car_position = 4
    obstacle_row = 0
    obstacle_col = random.randint(0, 9)
    score = 0
    high_scores = load_scores()
    
    countdown(screen)
    
    while True:
        key = screen.getch()
        
        if key == ord('q'):
            return False
        elif key == curses.KEY_LEFT and car_position > 0:
            car_position -= 1
        elif key == curses.KEY_RIGHT and car_position < 9:
            car_position += 1
        
        obstacle_row += 1
        if obstacle_row >= 10:
            obstacle_row = 0
            obstacle_col = random.randint(0, 9)
            score += 1
        
        if obstacle_row == 8 and obstacle_col == car_position:
            high_scores.append(score)
            high_scores = sorted(high_scores, reverse=True)[:3]
            save_scores(high_scores)
            
            screen.clear()
            screen.addstr(0, 0, "💥 GAME OVER!")
            screen.addstr(1, 0, f"Your score: {score}")
            screen.addstr(3, 0, "🏆 Top 3 High Scores:")
            for i, s in enumerate(high_scores):
                screen.addstr(4 + i, 0, f"{i + 1}. {s}")
            screen.addstr(8, 0, "Press R to play again or Q to quit")
            screen.nodelay(False)
            screen.refresh()
            while True:
                key = screen.getch()
                if key == ord('r'):
                    return True
                elif key == ord('q'):
                    return False
        
        screen.clear()
        screen.addstr(0, 0, f"Score: {score}")
        
        for row in range(10):
            if row == 8:
                screen.addstr(row, 0, "|" + " " * car_position + "🚙" + " " * (9 - car_position) + "|")
            elif row == obstacle_row:
                screen.addstr(row, 0, "|" + " " * obstacle_col + "🪨" + " " * (9 - obstacle_col) + "|")
            else:
                screen.addstr(row, 0, "|" + " " * 10 + "|")
        
        screen.addstr(10, 0, "-" * 12)
        screen.refresh()
        speed = max(0.05, 0.2 - (score * 0.005))
        time.sleep(speed)

def main(screen):
    while True:
        play_again = game(screen)
        if not play_again:
            break

def play():
    curses.wrapper(main)
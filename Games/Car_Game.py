import random
import os
import time

def draw_track(car_position, obstacle_row, obstacle_col, score):
    os.system("clear")
    print("Score:", score)
    track_width = 10

    for row in range(10):
        if row == 8:
            line = "|" + " " * car_position + "🚗" + " " * (track_width - car_position - 1) + "|"
        elif row == obstacle_row:
            line = "|" + " " * obstacle_col + "🪨" + " " * (track_width - obstacle_col - 1) + "|"
        else:
            line = "|" + " " * track_width + "|"
        print(line)

    print("-" * 12)

car_position = 4
obstacle_row = 0
obstacle_col = random.randint(0, 8)
score = 0

while True:
    draw_track(car_position, obstacle_row, obstacle_col, score)
    obstacle_row += 1
    if obstacle_row >= 10:
        obstacle_row = 0
        obstacle_col = random.randint(0, 8)
        score += 1

    move = input("Move (a = left, d = right, q = quit): ").lower()

    if move == "a" and car_position > 0:
        car_position -= 1
    elif move == "d" and car_position < 9:
        car_position += 1
    elif move == "q":
        print("Thanks for playing!")
        break

    if obstacle_row == 8 and obstacle_col == car_position:
        print("💥 GAME OVER! You crashed!")
        break
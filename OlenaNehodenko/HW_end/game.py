from tkinter import *
import random
import time

class Ball():
    def __init__(self, canvas, platform, color, score):
        self.canvas = canvas
        self.platform = platform
        self.score = score
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.dir = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(self.dir)
        self.y = -1
        self.touch_bottom = False

    def reset_score(self):
        self.score.reset_score()

    def draw(self):
        try:
            self.canvas.move(self.oval, self.x, self.y)
            pos = self.canvas.coords(self.oval)
            if pos[1] <= 0:
                self.y = 3
            if pos[3] >= 400:
                self.touch_bottom = True
                self.reset_score()
            if self.touch_platform(pos):
                self.y = -3
                self.score.increase_score()

            if pos[0] <= 0:
                self.x = 3
            if pos[2] >= 500:
                self.x = -3
        except TclError:
            pass

    def touch_platform(self, ball_pos):
        try:
            platform_pos = self.canvas.coords(self.platform.rect)
            if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
                if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                    return True
            return False
        except TclError:
            pass

class Platform():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0

    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2

    def draw(self):
        try:
            pos = self.canvas.coords(self.rect)
            if (self.x < 0 and pos[0] > 0) or (self.x > 0 and pos[2] < 500):
                self.canvas.move(self.rect, self.x, 0)
        except TclError:
            pass

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    def display_game_over(self):
        self.canvas.create_text(250, 120, text='Ви програли', font=('Courier', 30), fill='red')

    def increase_score(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

    def reset_score(self):
        self.score = 0
        self.canvas.itemconfig(self.id, text=self.score)

def restart_game():
    global platform, ball, score
    canvas.delete(ALL)
    platform = Platform(canvas, 'green')
    ball = Ball(canvas, platform, 'red', score)
    ball.touch_bottom = False

    window.bind('<Left>', platform.left)
    window.bind('<Right>', platform.right)

    score.reset_score()

    while True:
        if ball.touch_bottom == False:
            ball.draw()
            platform.draw()
        else:
            break

        window.update()
        time.sleep(0.01)

    score.display_game_over()
    window.update()

window = Tk()
window.title("Catch me")
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)

canvas = Canvas(window, width=500, height=400)
canvas.pack()

score = Score(canvas, 'green')
platform = Platform(canvas, 'green')
ball = Ball(canvas, platform, 'red', score)

window.bind('<Left>', platform.left)
window.bind('<Right>', platform.right)

restart_button = Button(window, text="Restart", command=restart_game)
restart_button.pack()

while True:
    if ball.touch_bottom == False:
        ball.draw()
        platform.draw()
    else:
        break

    window.update()
    time.sleep(0.01)

score.display_game_over()
window.update()
window.mainloop()
import random
from lookup import Lookup
import numpy
from PIL import Image, ImageDraw


class HigherLower:
    score = 0
    temp = 0
    win = 2
    state = 0

    def __init__(self):
        self.lookup = Lookup()
        print("Higher/Lower: Numbers between 1-13. Guess as many as you can!")

    def menu(self):
        a = input("| 1 = Play game | 2 = High Score | 3 = Back to menu |\n")
        while a not in ["1", "2", "3"]:
            print("Enter a valid input")
            a = input("| 1 = Play game | 2 = High Score | 3 = Back to menu |\n")
        if a == "1":
            self.start()
        elif a == "2":
            self.highscore()
        else:
            print("Returning...")
            self.state = 1

    def highscore(self):
        print("    HIGH SCORES")
        print("    NAME      SCORE")
        highscores = self.lookup.get_highscore()
        highscores = (sorted(highscores.items(), key=lambda x: x[1][1], reverse=True))
        n = 0
        for i in highscores:
            n += 1
            if n == 1:
                print(str(n) + "ST " + i[1][0] + "       " + str(i[1][1]))
            elif n == 2:
                print(str(n) + "ND " + i[1][0] + "       " + str(i[1][1]))
            elif n == 3:
                print(str(n) + "RD " + i[1][0] + "       " + str(i[1][1]))
            else:
                print(str(n) + "TH " + i[1][0] + "       " + str(i[1][1]))
        self.menu()

    def start(self):
        self.score = 0
        a = random.randint(1, 13)
        self.temp = a
        print("Starting number: " + str(a))
        self.loop()

    def loop(self):
        while self.state == 0:
            b = input("Higher(H) or Lower(L)? ")
            allow = ["h", "l", "H", "L"]
            while b not in allow:
                print("Enter a valid input (H,h,L,l)")
                b = input("Higher(H) or Lower(L)?")
            b = b.upper()
            c = random.randint(1, 13)
            print("Next number:" + str(c))
            if (c > self.temp and b == "L") or (c < self.temp and b == "H"):
                print("You lose")
                print("Your score: " + str(self.score))
                # update highscore
                high = 0
                n = 0
                for i in self.lookup.get_highscore().values():
                    n += 1
                    if int(i[1]) < self.score:
                        high = 1
                if (high == 1) or (n < 5):
                    print("Top 5!")
                    # top 5 only
                    name = input("Enter your name: ")
                    while len(name) != 3:
                        print("Name must be 3 chars")
                        name = input("Enter your name: ")
                    if len(name) == 0:
                        name = "UND"
                    self.lookup.add_name(name, self.score)
                self.endscreen()
            else:
                self.score += 1
                print("Correct!")
                self.temp = c

    def endscreen(self):
        a = input("| 1 = Play again | 2 = High Score | 3 = Go back |\n")
        allow = ["1", "2", "3"]
        while a not in allow:
            print("Enter a valid input")
            a = input("| 1 = Play again | 2 = High Score | 3 = Go back |\n")
        if a == "1":
            self.start()
        elif a == "2":
            self.highscore()
        else:
            self.menu()


class TwentyOneDares:
    end = 21
    state = 0
    x0 = 1
    x1 = 3

    def __init__(self):
        print("21 Dares: First to zero loses! Play against a bot or Player 2.")

    def menu(self):
        print("Current settings: " + str(self.end) + " Dares, range: (" + str(self.x0) + "-" + str(self.x1) + ")")
        p1 = input("| 1 = Play against bot | 2 = Two players | 3 = Settings | 4 = Back to menu |\n")
        while p1 not in ["1", "2", "3", "4"]:
            print("Enter a valid input (1,2,3,4)")
            p1 = input("| 1 = Play against bot | 2 = Two players | 3 = Settings | 4 = Back to menu |\n")
        if p1 == "1":
            self.menu2()
        elif p1 == "2":
            self.two_player()
        elif p1 == "3":
            self.settings()
        else:
            self.state = 1

    def menu2(self):
        p2 = input("| 1 = Easy | 2 = Medium | 3 = Hard | 4 = God | 5 = Go back |\n")
        while p2 not in ["1", "2", "3", "4", "5"]:
            print("Enter a valid input")
            p2 = input("| 1 = Easy | 2 = Medium | 3 = Hard | 4 = God | 5 = Go back |\n")
        if p2 == "5":
            self.menu()
        else:
            self.bot(p2)

    ''' def menu3(self):
      p2 = input("| 1 = Play game | 2 = Go back |\n")
      while p2 not in ["1","2"]:
        print("Enter a valid input")
        p2 = input("| 1 = Play game | 2 = Go back |\n")
      if p2 == "1":
        self.two_player()
      else:
        self.menu() '''

    def settings(self):
        p2 = input("| 1 = Change starting number | 2 = Change remove range | 3 = Go back |\n")
        while p2 not in ["1", "2", "3"]:
            print("Enter a valid input")
            p2 = input("| 1 = Change starting number | 2 = Change remove range | 3 = Go back |\n")
        if p2 == "1":
            print("Current starting number: " + str(self.end))
            a = input("New starting number: ")
            while self.state == 0:
                if a.isdecimal() == False:
                    print("Enter a valid input")
                    a = input("New starting number: ")
                elif int(a) not in range(11, 51):
                    print("Starting number can only be between 11-51")
                    a = input("New starting number: ")
                else:
                    self.end = int(a)
                    self.settings()
                    break
        elif p2 == "2":
            print("Current remove range: (" + str(self.x0) + "-" + str(self.x1) + ")")
            a = input("New bottom range: ")
            while self.state == 0:
                if a.isdecimal() == False:
                    print("Enter a valid input")
                    a = input("New bottom range: ")
                elif int(a) not in range(1, 10):
                    print("Bottom range can only be between 1-9")
                    a = input("New bottom range: ")
                else:
                    self.x0 = int(a)
                    break
            b = input("New top range: ")
            while self.state == 0:
                if b.isdecimal() == False:
                    print("Enter a valid input")
                    b = input("New top range: ")
                elif int(b) not in range(int(a) + 1, 11):
                    print("Top range must be greater than bottom range and lower than 11")
                    b = input("New top range: ")
                else:
                    self.x1 = int(b)
                    self.settings()
        else:
            self.menu()

    def two_player(self):
        originalend = self.end
        print("Starting number: " + str(self.end))
        while self.state == 0:
            # player 1 move
            print("Player 1's turn")
            a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
            while self.state == 0:
                if a.isdecimal() == False:
                    print("Enter a valid input")
                    a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                elif int(a) not in range(self.x0, self.x1 + 1):
                    print("Input not in range")
                    a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                else:
                    break
            self.end -= int(a)
            print("Player 1 removes " + a)
            if self.end <= 0:
                self.twoplayerendscreen(originalend, 0)
            else:
                print(str(self.end) + " left")
                # player 2 move
                print("Player 2's turn")
                a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                while self.state == 0:
                    if a.isdecimal() == False:
                        print("Enter a valid input")
                        a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                    elif int(a) not in range(self.x0, self.x1 + 1):
                        print("Input not in range")
                        a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                    else:
                        break
                self.end -= int(a)
                print("Player 2 removes " + a)
                if self.end <= 0:
                    self.twoplayerendscreen(originalend, 1)
                else:
                    print(str(self.end) + " left")

    def twoplayerendscreen(self, end, result):
        # reset end score
        self.end = end
        if result == 0:
            print("Player 2 wins!")
        else:
            print("PLayer 1 wins!")
        a = input("| 1 = Play again | 2 = Go back |\n")
        while a not in ["1", "2"]:
            print("Enter a valid input")
            a = input("| 1 = Play again | 2 = Go back |\n")
        if a == "1":
            self.two_player()
        else:
            self.menu()

    def bot_move(self, difficulty):
        if difficulty == "1":
            if self.end == 1:
                move = 1
            elif 1 < self.end < 4:
                move = random.randint(1, self.end - 1)
            else:
                move = random.randint(self.x0, self.x1)
        elif difficulty == "2":
            if self.end == 1:
                move = 1
            elif self.end in (4, 8, 12):
                moves = [3, 3, 3, 2, 1]
                n = random.randint(1, 5)
                move = moves[n - 1]
            elif self.end in (3, 7, 11):
                moves = [2, 2, 2, 3, 1]
                if self.end == 3:
                    move = 2
                else:
                    n = random.randint(1, 5)
                    move = moves[n - 1]
            elif self.end in (2, 6, 10):
                moves = [1, 1, 1, 2, 3]
                if self.end == 2:
                    move = 1
                else:
                    n = random.randint(1, 5)
                    move = moves[n - 1]
            else:
                move = random.randint(1, 3)
        elif difficulty == "3":
            if self.end == 1:
                move = 1
            elif self.end == 2:
                move = 1
            elif self.end == 3:
                move = 2
            elif self.end == 4:
                move = 3
            elif self.end in (8, 12):
                moves = [3, 3, 3, 3, 2, 1]
                n = random.randint(1, 5)
                move = moves[n - 1]
            elif self.end in (7, 11):
                moves = [2, 2, 2, 2, 3, 1]
                n = random.randint(1, 5)
                move = moves[n - 1]
            elif self.end in (6, 10):
                moves = [1, 1, 1, 1, 2, 3]
                n = random.randint(1, 5)
                move = moves[n - 1]
            elif self.end % 4 == 0:
                moves = [3, 3, 3, 2, 1]
                n = random.randint(1, 5)
                move = moves[n - 1]
            elif (self.end + 1) % 4 == 0:
                moves = [2, 2, 2, 3, 1]
                n = random.randint(1, 5)
                move = moves[n - 1]
            else:
                moves = [1, 1, 1, 2, 3]
                n = random.randint(1, 5)
                move = moves[n - 1]
        else:
            if self.end == 1:
                move = 1
            elif self.end % 4 == 0:
                move = 3
            elif (self.end + 1) % 4 == 0:
                move = 2
            else:
                move = 1
        return move

    def bot(self, prompt):
        originalend = self.end
        difficulty = prompt
        p3 = input("| 1 = You go first | 2 = Bot goes first | 3 = Go back |\n")
        while p3 not in ["1", "2", "3"]:
            print("Enter a valid input")
            p3 = input("| 1 = You go first | 2 = Bot goes first | 3 = Go back |\n")
        if p3 == "1":
            print("Starting number: " + str(self.end))
            while self.state == 0:
                # player move
                a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                while self.state == 0:
                    if a.isdecimal() == False:
                        print("Enter a valid input")
                        a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                    elif int(a) not in range(self.x0, self.x1 + 1):
                        print("Input not in range")
                        a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                    else:
                        break
                self.end -= int(a)
                if self.end <= 0:
                    self.botendscreen(originalend, 0, difficulty)
                else:
                    print(str(self.end) + " left")
                    # bot move
                    move = self.bot_move(difficulty)
                    print("Computer removes " + str(move))
                    self.end -= move
                    if self.end <= 0:
                        self.botendscreen(originalend, 1, difficulty)
                    else:
                        print(str(self.end) + " left")


        elif p3 == "2":
            print("Starting number: " + str(self.end))
            while self.state == 0:
                # bot move
                move = self.bot_move(difficulty)
                print("Computer removes " + str(move))
                self.end -= move
                if self.end <= 0:
                    self.botendscreen(originalend, 1, difficulty)
                else:
                    print(str(self.end) + " left")
                    # player move
                    a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                    while self.state == 0:
                        if a.isdecimal() == False:
                            print("Enter a valid input")
                            a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                        elif int(a) not in range(self.x0, self.x1 + 1):
                            print("Input not in range")
                            a = input("How many (" + str(self.x0) + "-" + str(self.x1) + ") do you want to remove? ")
                        else:
                            break
                    self.end -= int(a)
                    if self.end <= 0:
                        self.botendscreen(originalend, 0, difficulty)
                    else:
                        print(str(self.end) + " left")

        else:
            self.menu2()

    def botendscreen(self, end, result, difficulty):
        # reset end score
        self.end = end
        if result == 0:
            print("You lose!")
        else:
            print("You win!")
        a = input("| 1 = Play again | 2 = Go back |\n")
        while a not in ["1", "2"]:
            print("Enter a valid input")
            a = input("| 1 = Play again | 2 = Go back |\n")
        if a == "1":
            self.bot(difficulty)
        else:
            self.menu2()


class ConnectFour:
    state = 0
    connect = 4
    win = None
    xboard = 7
    yboard = 6
    height = 360
    width = int(height * (xboard / yboard))
    space = int(width / xboard)
    data = numpy.zeros((height, width, 3), dtype=numpy.uint8)
    image = Image.fromarray(data)
    # because list comprehensions are annoying, i can't input xboard or yboard into them, have to hardcode 6 and 7...
    board = []

    red = [255, 0, 0]
    green = [0, 255, 0]
    blue = [0, 0, 255]
    gold = [255, 215, 0]
    purple = [255, 0, 255]
    black = [0, 0, 0]
    white = [255, 255, 255]

    def __init__(self):
        # background
        # print(self.board)
        # self.resetboard()
        print("Connect 4: Connect four of the same color to win.")

    def menu(self):
        a = input("| 1 = Play game | 2 = Settings | 3 = Back to menu |\n")
        while a not in ["1", "2", "3"]:
            print("Enter a valid input")
            a = input("| 1 = Play game | 2 = High Score | 3 = Back to menu |\n")
        if a == "1":
            self.resetboard()
            self.play()
        elif a == "2":
            self.settings()
        else:
            print("Returning...")
            self.state = 1

    def returnimage(self):
        image = self.image
        return image

    def saveimage(self, image):
        # image = self.returnimage()
        image.save('whatever.png')
        self.image = image

    def resetboard(self):
        self.win = None
        self.width = int(self.height * (self.xboard / self.yboard))
        self.space = int(self.width / self.xboard)
        self.data = numpy.zeros((self.height, self.width, 3), dtype=numpy.uint8)
        self.image = Image.fromarray(self.data)
        self.board = [[0] * self.yboard for i in range(self.xboard)]
        # background
        for j in range(self.height):
            print("Canvas: " + str(j + 1) + "/" + str(self.height), end='\r')
            for i in range(self.width):
                self.data[j, i] = [0, 128, 255]
        print("\x1b[0K\r")  # to fix "\r", it doesn't delete, just replace. this clears it.
        # https://stackoverflow.com/questions/5419389/how-to-overwrite-the-previous-print-to-stdout-in-python
        # image = self.returnimage()
        image = Image.fromarray(self.data)
        for j in range(self.yboard):
            # print("Holes " + str(j+1) + "/" + str(self.yboard),end='\r')
            for i in range(self.xboard):
                draw = ImageDraw.Draw(image)
                s0 = self.space
                s = s0 / 12
                draw.ellipse((s0 * i + s, s0 * j + s, s0 * (i + 1) - s, s0 * (j + 1) - s), fill=(0, 102, 204),
                             outline=(0, 76, 153))
        self.saveimage(image)

    def move(self, i, color):
        # while True:
        if color == 1:
            fillcolor = (255, 255, 0)  # yellow
        else:
            fillcolor = (255, 0, 0)  # red
        image = self.returnimage()
        draw = ImageDraw.Draw(image)
        s0 = self.space
        s = s0 / 12
        # a = int(input("Enter: "))
        i -= 1
        j = self.updateboard(i, color)
        # j,i = a // self.xboard, a % self.xboard
        draw.ellipse((s0 * i + s, s0 * j + s, s0 * (i + 1) - s, s0 * (j + 1) - s), fill=fillcolor, outline=(0, 76, 153),
                     width=2)
        # image.save('whatever.png')
        self.saveimage(image)
        self.checkwin(i, j, color)

    def updateboard(self, i, color):
        # print(self.board[i])
        column = self.board[i]
        n = 0
        for j in range(len(column)):
            if column[j] == 0:
                # if entire column empty then place piece at bottom
                if j == len(column) - 1:
                    self.board[i][j] = color
                    n = j
                # if slot empty check slot below (above case stops when reach bottom)
                else:
                    continue
            else:
                # if entire column is full return None (error message)
                if j == 0:
                    n = None
                else:
                    self.board[i][j - 1] = color
                    n = j - 1
                    break
        # print(self.board)
        return n

    def checkwin(self, i, j, color):
        connect = self.connect
        check = 0
        for y in range(j - 1, j + 2):
            for x in range(i - 1, i + 2):
                check += 1
                pos = (y, x)
                if check > 4 or self.win != None:
                    break
                elif pos == (j, i):
                    continue
                else:
                    # print("\nChecking pos " + str(check))
                    n = 0
                    x0 = x
                    y0 = y
                    flip = 1
                    while n < connect:
                        if n == connect - 1:
                            # print("win")
                            self.win = color
                            break
                        elif ((not 0 <= x0 <= self.xboard - 1) or (not 0 <= y0 <= self.yboard - 1)):
                            # print("out of range")
                            if flip == 1:
                                # print("flip")
                                flip = -1
                                x0 = 2 * i - x
                                y0 = 2 * j - y
                            else:
                                break
                        elif self.board[x0][y0] != color:
                            # print(str(self.board[x0][y0]) + " not my color")
                            if flip == 1:
                                # print("flip")
                                flip = -1
                                x0 = 2 * i - x
                                y0 = 2 * j - y
                            else:
                                break
                        else:
                            n += 1
                            # print("ooh! " + str(n+1) + "/" + str(connect))
                            ydiff = (y - j) * flip
                            xdiff = (x - i) * flip
                            x0 += xdiff
                            y0 += ydiff

    def play(self):
        b = 1
        while self.win == None:
            a = input("Enter (1-7): ")
            if a.isdecimal() == False:
                print("Enter a valid input")
            elif not 1 <= int(a) <= self.xboard:
                print("Out of range")
            elif self.board[int(a) - 1][0] != 0:
                print("Column full!")
            else:
                self.move(int(a), b)
                if b == 1:
                    b = 2
                else:
                    b = 1
        self.endscreen()

    def settings(self):
        a = input("| 1 = Change connect number | 2 = Change board size | 3 = Render settings | 4 = Go back |\n")
        while a not in ["1", "2", "3", "4"]:
            print("Enter a valid input")
            a = input("| 1 = Change connecting number | 2 = Change board size | 3 = Render setting | 4 = Go back |\n")
        if a == "1":
            print("Current connecting number: " + str(self.connect))
            b = input("New connecting number: ")
            while self.state == 0:
                if b.isdecimal() == False:
                    print("Enter a valid input")
                    b = input("New connecting number: ")
                elif not 3 <= int(b) <= min(self.xboard, self.yboard):
                    print("Connecting number must be between 3-" + str(min(self.xboard, self.yboard)))
                    b = input("New connecting number: ")
                else:
                    self.connect = int(b)
                    self.settings()
        elif a == "2":
            print("Current board size: " + str(self.xboard) + "x" + str(self.yboard))
            b = input("New width: ")
            while self.state == 0:
                if b.isdecimal() == False:
                    print("Enter a valid input")
                    b = input("New width: ")
                elif not max(3, self.connect) <= int(b) <= max(self.connect, 30):
                    print("Width must be between " + str(max(3, self.connect)) + "-" + str(max(self.connect, 30)))
                    b = input("New width: ")
                else:
                    self.xboard = int(b)
                    break
            c = input("New height: ")
            while self.state == 0:
                if c.isdecimal() == False:
                    print("Enter a valid input")
                    c = input("New height: ")
                elif not max(3, self.connect) <= int(c) <= max(self.connect, 30):
                    print("Height must be between " + str(max(3, self.connect)) + "-" + str(max(self.connect, 30)))
                    c = input("New height: ")
                else:
                    self.yboard = int(c)
                    break
            self.settings()
        elif a == "3":
            q = None
            if self.height == 2160:
                q = "4K"
            elif self.height == 1080:
                q = "1080p"
            elif self.height == 360:
                q = "360p"
            else:
                q = "120p"
            print("Current render settings: " + q)
            b = input("| 1 = 120p | 2 = 360p | 3 = 1080p | 4 = 4K |\n")
            while b not in ["1", "2", "3", "4"]:
                print("Enter a valid input")
                b = input("| 1 = 120p | 2 = 360p | 3 = 1080p | 4 = 4K |\n")
            if b == "1":
                self.height = 120
            elif b == "2":
                self.height = 360
            elif b == "3":
                self.height = 1080
            else:
                self.height = 2160
            self.settings()
        else:
            self.menu()

    def endscreen(self):
        if self.win == 1:
            print("Yellow wins!")
        else:
            print("Red wins!")
        # a = input("Press ENTER to Restart")
        # if len(a)>=0:
        # self.resetboard()
        self.win = None
        self.menu()

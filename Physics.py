import time

from pynput.keyboard import Listener
import heapq
import threading


class Physics(object):
    gravity = -9.8

    def __init__(self):
        self.board = [[0] * 50 for i1 in range(50)]


class Human(object):

    def __init__(self, yloc, xloc, board):
        self.board = board
        self.yloc = yloc
        self.xloc = xloc
        self.humanlist = []
        self.width = 4
        self.height = 4
        self.setMainBody()
        self.setHeight()
        self.setObject()
        self.listen = threading.Thread(target=self.exist).start()
        self.binds = {
            '\'l\'': "jump",
            "\'p\'": "attack",
            "\'o\'": "special",
            "\'u\'": "grab",
            "\'w\'": "up",
            "\'s\'": " down",
            "\'a\'": "left",
            "\'d\'": "right",

        }

    def exist(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def setMainBody(self):
        self.board[self.yloc][self.xloc] = self

    def setObject(self):
        frommiddle = int(self.width / 2)
        for i in range(1, frommiddle):
            body = HumanBodyExtend(self.yloc, self.xloc - i, self.board, self)
            self.board[self.yloc][self.xloc - i] = body
            self.humanlist.append(body)
        for i in range(1, frommiddle):
            body1 = HumanBodyExtend(self.yloc, self.xloc + i, self.board, self)
            self.board[self.yloc][self.xloc + i] = body1
            self.humanlist.append(body1)

    def setHeight(self):
        for i in range(1, self.height):
            body1 = HumanLeg(self.yloc + i, self.xloc, self.board, self)
            self.board[self.yloc + i][self.xloc] = body1
            self.humanlist.append(body1)

    def on_press(self, key):
        self.testfunc(str(key))

    def testfunc(self, key):
        print(key)
        if key in self.binds.keys():
            getattr(self, self.binds[key])()

    def jump(self):
        self.board[self.yloc][self.xloc] = 0
        self.board[self.yloc - 1][self.xloc] = self
        self.yloc = self.yloc - 1
        self.airborne = True
        for item in self.humanlist:
            item.jump()
        for row in self.board:
            for val in row:
                print(val, end=' ')
            print()

    def left(self):
        self.board[self.yloc][self.xloc] = 0
        self.board[self.yloc][self.xloc - 1] = self
        self.xloc = self.xloc - 1
        for item in self.humanlist:
            item.left()
        for row in self.board:
            for val in row:
                print(val, end=' ')
            print()

    def right(self):
        self.board[self.yloc][self.xloc] = 0
        self.board[self.yloc][self.xloc + 1] = self
        self.xloc = self.xloc + 1
        for item in self.humanlist:
            item.right()
        for row in self.board:
            for val in row:
                print(val, end=' ')
            print()
    def special(self):
        lazer = Lazer(self.yloc, int(self.xloc+self.width/2), self.board)
    def __str__(self):
        return "FoxBody"


class Lazer(object):
    def __init__(self, yloc, xloc, board):
        self.yloc = yloc
        self.xloc = xloc
        self.board = board
        self.travel = threading.Thread(target=self.travelright).start()

    def travelright(self):
        while self.xloc < len(self.board[0])-1:

            self.board[self.yloc][self.xloc] = 0
            self.board[self.yloc][self.xloc + 1] = self
            self.xloc = self.xloc + 1

            time.sleep(0.5)
            print(self.xloc)
            for row in self.board:
                for val in row:
                    print(val, end=' ')
                print()

    def collide(self):
        pass
    def __str__(self):
        return("lazer")


class HumanBodyExtend(object):
    def __init__(self, yloc, xloc, board, mainbody):
        self.yloc = yloc
        self.xloc = xloc
        self.board = board
        self.parent = mainbody
        self.airborne = False

    def jump(self):
        self.board[self.yloc][self.xloc] = 0
        self.board[self.yloc - 1][self.xloc] = self
        self.yloc = self.yloc - 1
        self.airborne = True

    def right(self):
        self.board[self.yloc][self.xloc] = 0
        self.board[self.yloc][self.xloc + 1] = self
        self.xloc = self.xloc + 1

        for row in self.board:
            for val in row:
                print(val, end=' ')
            print()

    def left(self):
        self.board[self.yloc][self.xloc] = 0
        self.board[self.yloc][self.xloc - 1] = self
        self.xloc = self.xloc - 1

    def __str__(self):
        return "FoxBody2"


class HumanLeg(object):
    def __init__(self, yloc, xloc, board, mainbody):
        self.yloc = yloc
        self.xloc = xloc
        self.board = board
        self.parent = mainbody

    def right(self):
        self.board[self.yloc][self.xloc] = 0
        self.board[self.yloc][self.xloc + 1] = self
        self.xloc = self.xloc + 1

        for row in self.board:
            for val in row:
                print(val, end=' ')
            print()

    def jump(self):
        self.board[self.yloc][self.xloc] = 0
        self.board[self.yloc - 1][self.xloc] = self
        self.yloc = self.yloc - 1
        self.airborne = True

    def left(self):
        self.board[self.yloc][self.xloc] = 0
        self.board[self.yloc][self.xloc - 1] = self
        self.xloc = self.xloc - 1

    def __str__(self):
        return "FoxLeg"


def main():
    physics = Physics()
    fox = Human(46, 25, physics.board)
    for row in physics.board:
        for val in row:
            print(val, end=' ')
        print()

    print(physics.board[3][1])


if __name__ == '__main__':
    main()

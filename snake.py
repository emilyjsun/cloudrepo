import random
import curses
from curses import textpad

#https://www.youtube.com/watch?v=BvbqI6eDh0c

OPPOSITE_DIRECTION_DICT = {
	curses.KEY_UP: curses.KEY_DOWN,
	curses.KEY_DOWN: curses.KEY_UP,
	curses.KEY_RIGHT: curses.KEY_LEFT,
	curses.KEY_LEFT: curses.KEY_RIGHT
}

DIRECTIONS_LIST = [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]

def create_food(snake, box):
    food = None

    while food is None:
        #find position for food
        food = [random.randint(box[0][0]+1, box[1][0]-1),
                random.randint(box[0][1]+1, box[1][1]-1)]

        #cannot spawn food in snake
        if food in snake:
            food = None
    return food

def print_score(stdscr, score):
    #intialize score
    sh, sw = stdscr.getmaxyx()
    score_text = "Score: {}".format(score)
    stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)
    stdscr.refresh()

def main(stdscr):
    #create the rectangle area
    curses.curs_set(0)
    #let it keep moving
    stdscr.nodelay(1)
    stdscr.timeout(120)

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3, sw-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    #initialize the snake as ### going right
    #321 >>>
    #initialized in the middle of the screen
    snake = [[sh//2, sw//2+1], [sh//2, sw//2], [sh//2, sw//2-1]]
    direction = curses.KEY_RIGHT #snake is moving in right direction

    #visual of snake
    for y,x in snake:
        stdscr.addstr(y,x, '#')
    
    #create food
    food = create_food(snake, box)
    stdscr.addstr(food[0], food[1], '0')

    score = 0
    print_score(stdscr, score)

    
    #infinite loop for snake to move
    while 1:

        #check what key has been pressed by user
        #also makes sure it isnt opposite of current direction
        key = stdscr.getch()

        if key in DIRECTIONS_LIST and key != OPPOSITE_DIRECTION_DICT[direction]:
            direction = key

        #update the snake so that it moves
        head = snake[0]


        #creating the new head
        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
        elif direction == curses.KEY_UP:
            new_head = [head[0]-1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0]+1, head[1]]

        #insert head into snake's body at new position
        snake.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], '#')



        #check if head is on food
        if snake[0] == food:
            #increase length of snake
            food = create_food(snake, box)
            stdscr.addstr(food[0], food[1], '0')

            #increase score
            score += 1
            print_score(stdscr, score)
            
        else:
            #replace last element from previous snake with blank
            stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()

        #conditions to lose the game
        #hitting the sides of the box or snake hits itself
        if(snake[0][0] in [box[0][0], box[1][0]] 
        or snake[0][1] in [box[0][1], box[1][1]]
        or snake[0] in snake[1:]):
            msg = "Game Over!"
            stdscr.addstr(sh//2, sw//2 - len(msg)//2, msg)
            #keep waiting until user presses something to stop
            stdscr.timeout(-1)
            stdscr.getch()
            break

        stdscr.refresh()


curses.wrapper(main)
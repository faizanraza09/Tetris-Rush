import random
import os 

path = os.getcwd()

NUM_ROWS = 20
NUM_COLS = 10
BOARD_WIDTH=200
BOARD_HEIGHT=400

class Block():
    def __init__(self,options):
        self.w = 20
        self.h = 20
        self.options=options
        self.x=random.choice(self.options)
        self.y=0
        self.colors = {"Red":(255,51,52), "Blue":(12,150,228), "Green":(30,283,66), "Yellow":(246,187,0), "Purple":(76,0,153), "White":(255,255,255), "Black":(0,0,0)}
        self.block_color = self.colors[random.choice(self.colors.keys())]
        self.speed = 0
        self.delta_x=0
        self.delta_y=20
        self.falling=True
        
    def move(self):
        #if self.y==BOARD_HEIGHT-self.h:
        if self.y==BOARD_HEIGHT-self.h or game.grid[self.x/self.w][(self.y+self.h)/self.h]!=None :
            self.delta_y=0
            self.falling=False
            
        self.x += self.delta_x
        self.y += self.delta_y
        if self.falling==False:
            game.speed+=0.25
            game.add_to_grid()
            game.check_pop()

        
        
        
        
    
    def display(self):
        fill(self.block_color[0], self.block_color[1], self.block_color[2])
        rect(self.x,self.y,self.w,self.h)
        


class Game(list):
    def __init__(self):
        self.grid=[[None for i in range(NUM_ROWS)] for i in range(NUM_COLS)]
        self.options=[i*NUM_ROWS for i in range(NUM_COLS)]
        self.append(Block(self.options))
        self.score=0
        self.end=False
        self.speed=True
        
        
    def drop_blocks(self):
        if self[-1]==None or self[-1].falling==False:
            self.append(Block(self.options))
            
    def add_to_grid(self):
        self.grid[self[-1].x/self[-1].w][self[-1].y/self[-1].h]=self[-1]
        
    def check_pop(self):
        counter=0
        poppings=[]
        for i in self.grid[self[-1].x/self[-1].w]:
            if i and i.block_color==self[-1].block_color:
                counter+=1
                poppings.append(i)
                if counter==4:
                    self.pop_blocks(poppings)
                    self.speed=0
                    break
            else:
                counter=0
                poppings=[]
                
    def pop_blocks(self,poppings):
        self.score+=1
        for i in range(len(self)):
            for j in poppings:
                if self[i]:
                    if self[i].x==j.x and self[i].y==j.y:
                        self[i]=None
                        
        for i in poppings:
            self.grid[i.x/i.w][i.y/i.h]=None
            
            
    def check_empty_cols(self):
        options2=self.options[:]
        for i in self.options:
            counter=0
            for x in self.grid[i/20]:
                if x!=None:
                    counter+=1
            if counter==NUM_ROWS:
                options2.remove(i)
        self.options=options2
                
  
    def check_end(self):
        if len(self.options)==0:
            self.end=True

            
            
        
    def move(self):
        if self[-1]:
            self[-1].move()
    def display(self):    
        for i in self:
            if i!=None:
                i.display()
        fill(0,0,0)
        textSize(20)
        text('Score: '+str(self.score),BOARD_WIDTH-100,20)    

game = Game()

def setup():
    size(BOARD_WIDTH,BOARD_HEIGHT)
    background(210)
    
    
    
def draw():
    if game.end==False:
        if frameCount%(max(1, int(8 - game.speed)))==0 or frameCount==1:
            background(210)
            stroke(180)   
            for i in range(NUM_ROWS):
                line(0, 20*i, 200, 20*i) 
            for c in range(NUM_COLS):
                line(20*c, 0, 20*c, 400)
            
            game.display()
            game.move()
            game.check_empty_cols()
            game.check_end()
            
            if game.end==False:
                game.drop_blocks()
            
    else:
        background(0,0,0)
        textSize(12)
        fill(255,0,0)
        text('Your score was '+ str(game.score),10,BOARD_HEIGHT/2-30)
        text('Click anywhere to play again',10,BOARD_HEIGHT/2-10)
        
        
        
def keyPressed():    
    if keyCode==LEFT and game[-1].x>0 and game[-1].y<BOARD_HEIGHT-20 and game.grid[game[-1].x/game[-1].w-1][game[-1].y/game[-1].h]==None:
        game[-1].x-=20
    elif keyCode==RIGHT and game[-1].x<BOARD_WIDTH-20 and game[-1].y<BOARD_HEIGHT-20 and game.grid[game[-1].x/game[-1].w+1][game[-1].y/game[-1].h]==None:
        game[-1].x+=20
        
def mouseClicked():
    if game.end==True:
        global game
        game=Game()
        
            
        
        
    """if frameCount%(max(1, int(8 - Game.speed)))==0 or frameCount==1:
        background(210)
    #this calls the display method of the game class 
        Game.display()"""

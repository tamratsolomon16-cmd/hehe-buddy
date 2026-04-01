import sys
import pygame
import random
DEFAULT_BGCOLOR = (0,0,100)
DEFAULT_WIDTH   = 809
DEFAULT_HEIGHT  = 500 # if you're wondering, 809x500 is roughly the golden ratio

# type synonym for convenience
rgb = tuple[int,int,int]

class Roller:

    bgcolor : rgb
    width   : int
    height  : int
    surface : pygame.Surface
    clock   : pygame.time.Clock
    U = {'pygame.K_1':0,'pygame.K_2':1,'pygame.K_3':2,'pygame.K_4':3,'pygame.K_5':4}
    def __init__(self, frozen =[],
                 bgcolor : rgb = DEFAULT_BGCOLOR,
                 width   : int = DEFAULT_WIDTH,
                 height  : int = DEFAULT_HEIGHT,
                 ) -> None:
        self.bgcolor = bgcolor if bgcolor else DEFAULT_BGCOLOR
        self.width   = width if width else DEFAULT_WIDTH
        self.height  = height if height else DEFAULT_HEIGHT
        self.values = [1,1,1,1,1]
        self.frozen = frozen
    def un_freeze(self,x)-> None:
        if x in self.frozen:
            self.frozen.remove(x)
        else: 
            self.frozen.append(x)

        
    def reroll(self):
        for x in range(5):
            if x not in self.frozen:
                self.values[x] = random.randint(1,6)


    def run_app(self) -> None:
        pygame.init()
        pygame.display.set_caption("Roller")
        self.surface = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.run_event_loop()

    def quit_app(self) -> None:
        pygame.quit()
        sys.exit()

    def draw_window(self) -> None:
        self.surface.fill(self.bgcolor)
        pygame.draw.rect(self.surface, (255,255,255), (0,200,120,120))
        pygame.draw.rect(self.surface, (255,255,255), (140,200,120,120))
        pygame.draw.rect(self.surface, (255,255,255), (280,200,120,120))
        pygame.draw.rect(self.surface, (255,255,255), (420,200,120,120))
        pygame.draw.rect(self.surface, (255,255,255), (560,200,120,120))
        for i,x in enumerate(self.values):
            if x > 1:
                pygame.draw.circle(self.surface,(0,0,0),((0+140*i)+30,230),15,3)
                pygame.draw.circle(self.surface,(0,0,0),((0+140*i)+90,290),15,3)
            if x > 3:
                pygame.draw.circle(self.surface,(0,0,0),((0+140*i)+90,230),15,3)
                pygame.draw.circle(self.surface,(0,0,0),((0+140*i)+30,290),15,3)
            if x == 6:
                pygame.draw.circle(self.surface, (0,0,0),((0+140*i)+30,260),15,3)
                pygame.draw.circle(self.surface, (0,0,0),((0+140*i)+90,260),15,3)

            if x%2 != 0:
                pygame.draw.circle(self.surface, (0,0,0),((0+140*i)+60,260),15,3)
        pygame.display.update()
    def run_event_loop(self) -> None:
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quit_app()
                elif event.type == pygame.MOUSEMOTION:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.quit_app()
                    if event.key == pygame.K_r:
                        self.reroll()
                    if event.key == pygame.K_1:
                        self.un_freeze(0)
                    if event.key == pygame.K_2:
                        self.un_freeze(1)
                    if event.key == pygame.K_3:
                        self.un_freeze(2)
                    if event.key == pygame.K_4:
                        self.un_freeze(3)
                    if event.key == pygame.K_5:
                        self.un_freeze(4)
                elif event.type == pygame.KEYUP:
                    pass
            self.draw_window()
            self.clock.tick(24) # throttle redraws at 24fps (frames per second)

# ========

if __name__ == "__main__":
    q = Roller()
    q.run_app()

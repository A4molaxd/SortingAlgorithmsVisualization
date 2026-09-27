import pygame
import random
from math import floor

pygame.init()

HEIGHT = 800
WIDTH = 800

n = 100

screen = pygame.display.set_mode((HEIGHT, WIDTH))

class Bar():
    def __init__(self, x, val):
        self.x = x
        self.val = val
    
    def draw(self, screen):
        pygame.draw.rect(screen, "white", (self.x * WIDTH / n + (WIDTH / n - WIDTH / (n + n/10))/1.75, HEIGHT - ((self.val + 0.5) * HEIGHT / n), WIDTH / (n + n/10), (self.val + 0.5) * HEIGHT / n))

def checkSorted(bars):
    for i in range(n):
        if not i == bars[i].val:
            return False
    return True

def swap(bar1, bar2):
    tmp = bar1.val
    bar1.val = bar2.val
    bar2.val = tmp

def combsort(bars):
    gap = len(bars)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = floor(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        elif gap == 9 or gap == 10:
            gap == 11
        i = 0
        while i + gap < len(bars):
            if bars[i].val > bars[i + gap].val:
                swap(bars[i], bars[i + gap])
                sorted = False
                updateScreen(bars)
            i += 1



def updateScreen(bars):
    if checkSorted(bars): 
        color = "purple"
    else:
        color = "black" 

    screen.fill(color)
            
    for bar in bars:
        bar.draw(screen)

    pygame.display.flip()

def shuffle(bars):
    for i in range(n * 10):
        b1 = random.randint(0, n - 1)
        b2 = random.randint(0, n - 1)
        while b1 == b2:
            b2 = random.randint(0, n - 1)
        swap(bars[b1], bars[b2])

def main():
    run = True

    # Spawn bars
    bars = []
    for i in range(n):
        bars.append(Bar(i, i))

    # Desort bars
    shuffle(bars)

    while run:
        pygame.display.set_caption(("Comb Sort"))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if not run:
            break

        combsort(bars)
        print()
        print(pygame.time.get_ticks() / 1000)
        run = False

    pygame.quit()

if __name__ == '__main__':
    main()
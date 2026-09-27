import pygame
import random

pygame.init()

HEIGHT = 800
WIDTH = 800

n = 100

screen = pygame.display.set_mode((HEIGHT, WIDTH))

class Bar():
    def __init__(self, x, val):
        self.x = x
        self.val = val
    
    def draw(self, screen, i):
        pygame.draw.rect(screen, "white", (i * WIDTH / n + (WIDTH / n - WIDTH / (n + n/10))/1.75, HEIGHT - ((self.val + 0.5) * HEIGHT / n), WIDTH / (n + n/10), (self.val + 0.5) * HEIGHT / n))

def checkSorted(bars):
    if len(bars) == n:
        for i in range(n):
            if not i == bars[i].val:
                return False
        return True
    else: return False

def swap(bar1, bar2):
    tmp = bar1.val
    bar1.val = bar2.val
    bar2.val = tmp

def merge(left, right, clock):
    result = []

    while left != [] and right != []:
        if left[0].val <= right[0].val:
            result.append(left[0])
            updateScreen(result, clock)
            left.pop(0)
        else:
            result.append(right[0])
            updateScreen(result, clock)
            right.pop(0)
    while left != []:
        result.append(left[0])
        updateScreen(result, clock)
        left.pop(0)
    while right != []:
        result.append(right[0])
        updateScreen(result, clock)
        right.pop(0)
    return result

def mergesort(bars, clock):
    if len(bars) <= 1:
        return bars
    left = []
    right = []
    for i, x in enumerate(bars):
        if i < len(bars)/2:
            left.append(x)
        else:
            right.append(x)
    left = mergesort(left, clock)
    right = mergesort(right, clock)

    return merge(left, right, clock)

def updateScreen(bars, clock):
    if checkSorted(bars): 
        color = "purple"
    else:
        color = "black" 

    screen.fill(color)
            
    for i, bar in enumerate(bars):
        bar.draw(screen, i)

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
    clock = pygame.time.Clock()

    # Spawn bars
    bars = []
    for i in range(n):
        bars.append(Bar(i, i))

    # Desort bars
    shuffle(bars)

    while run:
        pygame.display.set_caption(("Merge Sort"))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if not run:
            break

        mergesort(bars, clock)
        print()
        print(pygame.time.get_ticks() / 1000)
        run = False

    pygame.quit()

if __name__ == '__main__':
    main()
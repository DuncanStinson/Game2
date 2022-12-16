import pygame
import pygame.mouse
import math

pygame.init()

WIDTH, HEIGHT = 1000, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

x=WIDTH/2
y=HEIGHT/2

l = False

class Hero:	
	counter = 0
	def __init__(self, x, y,lives):
		self.x = x
		self.y = y
		self.lives = lives

	def draw(self):

		self.counter+=1

		if self.counter % 5 == 1:
			screen.fill((0,90,250))

		
		if self.lives <= 0:
			screen.fill((0,90,250))

			text1 = pygame.font.SysFont('Verdana', 80)
			line1 = "GAMEOVER"
			text1 = pygame.font.Font.render(text1,line1,True, (255,0,0))

			rect = text1.get_rect()

			rect.center = (WIDTH/2,HEIGHT/2)

			screen.blit(text1,rect)

		else:
			text2 = pygame.font.SysFont('Verdana', 100)
			line2 = f"Lives: {self.lives}"
			text2 = pygame.font.Font.render(text2,line2,True, (255,130,0))

			rect = text2.get_rect()

			rect.center = (WIDTH/2,HEIGHT/2)

			screen.blit(text2,rect)

		#Character
		pygame.draw.rect(screen, (0,0,0), (self.x-1, self.y-1, 52, 52))
		pygame.draw.rect(screen, (60,60,60), (self.x, self.y, 50, 50))
		pygame.draw.circle(screen, (0,0,0), (self.x+25, self.y+25),25)
		pygame.draw.circle(screen, (255,0,135), (self.x+25, self.y+25),24)
		pygame.draw.circle(screen, (0,0,0), (self.x+25, self.y+25),16)
		pygame.draw.circle(screen, (60,60,60), (self.x+25, self.y+25),15)



def movement(h1):
	global l
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	if h1.lives != 0:
		x, y = pygame.mouse.get_pos()
		
		if x > h1.x:
			if h1.x != WIDTH-50 and h1.y == y:
				h1.x+=2
			elif h1.x != WIDTH-50:
				h1.x+=1
		else:
			if h1.x != -WIDTH-50 and h1.y == y:
				h1.x-=2
			elif h1.x != -WIDTH-50:
				h1.x-=1

		if y > h1.y:
			if h1.y != WIDTH-50 and h1.x == x:
				h1.y+=2
			elif h1.y != WIDTH-50:
				h1.y+=1
		else:
			if h1.y != -WIDTH-50 and h1.x == x:
				h1.y-=2
			elif h1.y != -WIDTH-50:
				h1.y-=1

		p1 = (x,y)
		p2 = (h1.x,h1.y)
		
		#Using pythagorean theorem
		distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

		if distance > 100:
			l = True

		if distance < 25 and l == True:
			l = False
			h1.lives-=1
			pygame.mouse.set_visible(False)

		else:
			pygame.mouse.set_visible(True)
		
		h1.draw()

		pygame.display.update()
		pygame.event.pump()
	


h1 = Hero(x,y,3)

while True:
	movement(h1)




	


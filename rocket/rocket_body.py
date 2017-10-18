import pygame

class Rocket():
	def __init__(self,ai_settings,screen):
		self.screen=screen
		self.ai_settings=ai_settings
		

		self.image=pygame.image.load('images/rocket.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		self.rect.centerx=self.screen_rect.centerx
		self.rect.centery=self.screen_rect.centery

		self.center=float(self.rect.centerx)
		self.center1=float(self.rect.centery)

		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False

	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center+=self.ai_settings.rocket_speed
		if self.moving_left and self.rect.left>0:
			self.center-=self.ai_settings.rocket_speed

		if self.moving_up and self.rect.top>0:
			self.center1-=self.ai_settings.rocket_speed
		if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
			self.center1+=self.ai_settings.rocket_speed

		self.rect.centerx=self.center
		self.rect.centery=self.center1

	def blitme(self):
		self.screen.blit(self.image,self.rect)



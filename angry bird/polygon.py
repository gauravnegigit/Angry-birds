import math 
import pymunk 
import pygame
from pymunk import Vec2d

from constants import ELASTICITY , FRICTION , WOOD , WOOD2


class Polygon :
    def __init__(self , pos , width , height , space , mass = 5) -> None:
        moment = 1000
        body = pymunk.Body(mass , moment)
        body.position = pos 
        shape = pymunk.Poly.create_box(body , (width , height ))
        shape.color = (0 , 0 , 255 , 100)
        shape.friction = FRICTION
        shape.elasticity = 0.5
        shape.collision_type = 2
        space.add(body , shape)
        rect = pygame.Rect(251 , 357 , 86 , 22)
        self.beam_image = WOOD.subsurface(rect).copy()
        rect = pygame.Rect(16 , 252 , 22 , 84)
        self.column_image = WOOD2.subsurface(rect).copy()

        self.shape , self.body = shape , body
        
    def to_pygame(self, p):
        """Convert pymunk to pygame coordinates"""
        return int(p.x), int(-p.y+600)
    
    def draw_poly(self , element , screen):
        """Blittinhg beams and columns on the screen """

        poly = self.shape
        ps = poly.get_vertices()
        ps.append(ps[0])
        #ps = map(self.to_pygame, ps)
        ps = list(ps)
        color = (255, 0, 0)
        pygame.draw.lines(screen, color, False, ps)

        p = poly.body.position
        p = Vec2d(*p)
        angle_degrees = 180 - math.degrees(poly.body.angle) 

        if element == 'beams':

            rotated_logo_img = pygame.transform.rotate(self.beam_image,
                                                       angle_degrees)

        if element == 'columns':

            rotated_logo_img = pygame.transform.rotate(self.column_image,
                                                       angle_degrees)
        
        offset = Vec2d(*rotated_logo_img.get_size()) / 2.
        p = p - offset
        np = p
        screen.blit(rotated_logo_img, (np.x, np.y))      

import random
from typing import Iterator, Tuple

from world.game_map import GameMap
from world import tile_types

import tcod

class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
    
        # define points on rectangle
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height
        
    @property
    def center(self) -> Tuple[int,int]:
        '''Returns the coordinates of the center of the room'''
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        
        return center_x, center_y
    
    @property
    def inner(self) -> Tuple[slice,slice]:
        '''Returns the inner area of the room as a 2D array index'''
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

def tunnel_between(start: Tuple[int,int], end: Tuple[int,int]) -> Iterator[Tuple[int,int]]:
    """Return an L-shaped tunnel between these two points"""
    x1, y1 = start
    x2, y2 = end
    
    # randomly decide whether to move horizontically or vertically first
    if random.random() < 0.5:
        # move horizontally, then vertically
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally
        corner_x, corner_y = x1, y2 
        
    # Generate coordinates for this tunnel
    # First yield coordinates between start and corner
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    # Then yield coordinates between corner and end
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y
        
def generate_dungeon(map_width, map_height) -> GameMap:
    dungeon = GameMap(map_width, map_height)
    
    room_1 = RectangularRoom(x=20, y=30, width=10, height=10)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)
    
    dungeon.tiles[room_1.inner] = tile_types.floor
    dungeon.tiles[room_2.inner] = tile_types.floor
    
    for x, y in tunnel_between(room_1.center, room_2.center):
        dungeon.tiles[x, y] = tile_types.floor
    
    return dungeon
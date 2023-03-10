import numpy as np # type: ignore
from tcod.console import Console

from world import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        
        # initialize map with floor tiles. Order F is important for coordinates
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")
        
        
    def in_bounds(self, x: int, y: int) -> bool:
        '''
        Checks if a given x and y coordinate are inside the bounds of the map
        Return True if x and y are inside bounds of the map
        '''
        return 0 <= x < self.width and 0 <= y < self.height
    
    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
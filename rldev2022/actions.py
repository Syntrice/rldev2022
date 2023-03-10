from __future__ import annotations
from typing import TYPE_CHECKING

# Type checking only imports
if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:
        """Perform this action with the objects needed to determine its scope.

        `engine` is the scope this action is being performed in.
        `entity` is the object performing the action.
        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()

class EscapeAction(Action):
    '''
    Exits the game
    '''
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()

class MovementAction(Action):
    '''
    Moves an entity by a given amount
    '''
    def __init__(self, dx: int, dy: int):
        super().__init__()
        
        self.dx = dx
        self.dy = dy
        
    def perform(self, engine: Engine, entity: Entity) -> None:
        
        # destination to move too
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        
        # check if movement is possible
        if not engine.game_map.in_bounds(dest_x, dest_y):
            return # destination is out of bounds
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return # destination is blocked
        
        entity.move(self.dx, self.dy)
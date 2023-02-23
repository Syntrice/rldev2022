from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from entity import Entity
from world.game_map import GameMap
from input_handlers import EventHandler

class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player
    
    def handle_events(self, events: Iterable[Any]) -> None:
        '''
        Takes in a list of events and dispatches them to the appropriate action
        '''
        
        # events carried out by player
        for event in events:
            action = self.event_handler.dispatch(event)
            
            if action is None:
                continue
            
            action.perform(self, self.player)
    
    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)
        
        for entity in self.entities:
            console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)

        context.present(console)
        
        # clear console ready for next frame
        console.clear()
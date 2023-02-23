import tcod
from engine import Engine
from entity import Entity
from world.game_map import GameMap
from input_handlers import EventHandler
from world.procgen import generate_dungeon

def main() -> None:
    
    # Window Dimensions
    screen_width = 80
    screen_height = 50
    
    map_width = 80
    map_height = 45
    
    # Load Tileset
    tileset = tcod.tileset.load_tilesheet("rldev2022/assets/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    # Event Handler
    event_handler = EventHandler()
    
    # create entities and default properties
    player = Entity(int(screen_width/2), int(screen_height/2), "@", (255,255,255))
    npc = Entity(int(screen_width/2 - 5), int(screen_height/2), "@", (255,255,0))
    
    entities = {npc, player}
    
    # create game map
    game_map = generate_dungeon(map_width, map_height)
    
    # create engine
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player) 
    
    with tcod.context.new_terminal(
        screen_width, 
        screen_height, 
        tileset=tileset, 
        title="rldev2022", 
        vsync=True
    ) as context:
        # order F allows numpy to access 2D arrays in [x,y] order as apposed to [y,x]
        root_console = tcod.Console(screen_width, screen_height, order="F") 
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait() # parse events
            engine.handle_events(events)

if __name__ == "__main__":
    main()

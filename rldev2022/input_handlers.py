from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

# Dispatch events to methods, which can then be used to return objects of type Action
class EventHandler(tcod.event.EventDispatch[Action]):
    
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        
        action: Optional[Action] = None
        
        key = event.sym
        
        # Movement actions
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)
        
        # Escape action
        elif key == tcod.event.K_ESCAPE:
            return EscapeAction()
    
        return action
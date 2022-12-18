import tcod

# main method (entrypoint)
# the arrow is metadata which indicates return type
def main() -> None: 
    
    # define window title
    title = "rldev2022"
    
    # define window dimensions
    screen_width, screen_height = 80, 50
    
    # load tileset
    tileset = tcod.tileset.load_tilesheet("rldev2022/assets/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    
    # setup new window, and use its context
    with tcod.context.new_terminal(screen_width,screen_height,tileset=tileset,title=title,vsync=True,) as context:
        
        # create and setup a console
        # order F allows numpy to access 2D arrays in [x,y] order as apposed to [y,x]
        root_console = tcod.Console(screen_width,screen_height, order="F")
        
        # game loop (basically the 'engine' of the game)
        while True:
            
            # print to console
            root_console.print(x=1,y=1, string="@")
            
            # update the screen
            context.present(root_console)
            
            # wait for input, then loop through each event that happend
            for event in tcod.event.wait():
                
                # determine if exit event occurred
                if event.type == "QUIT":
                    raise SystemExit()   
                
# only executed if the script is explicitily run
if __name__ == "__main__":
    main()
    

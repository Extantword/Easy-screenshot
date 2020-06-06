import pynput
from pynput.mouse import Listener
import pyscreenshot as ImageGrab

#List for storing where you clicked in yout screen
mouse_positions = []

def on_click(x, y, button, pressed):
    if pressed:
        
        #Checks wheter is the first or second clic
        if(mouse_positions == []):

            mouse_positions.append([x,y])

        else:
            mouse_positions.append([x,y])
            
            #Allows to choose any corners of the rectangle to take the screenshot
            
            im = ImageGrab.grab(bbox=(min(mouse_positions[0][0], mouse_positions[1][0]),
                                      min(mouse_positions[0][1], mouse_positions[1][1]),
                                      max(mouse_positions[0][0], mouse_positions[1][0]),
                                      max(mouse_positions[0][1], mouse_positions[1][1])))

            im.save('screenshot.png')
            listener.stop()


with Listener(on_click=on_click) as listener:

    listener.join()

exit()

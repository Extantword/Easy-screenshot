import pynput
from pynput.mouse import Listener
import pyscreenshot as ImageGrab


mouse_positions = []

def on_click(x, y, button, pressed):
    if pressed:
        if(mouse_positions == []):

            mouse_positions.append([x,y])

        else:
            mouse_positions.append([x,y])
            im = ImageGrab.grab(bbox=(min(mouse_positions[0][0], mouse_positions[1][0]),
                                      min(mouse_positions[0][1], mouse_positions[1][1]),
                                      max(mouse_positions[0][0], mouse_positions[1][0]),
                                      max(mouse_positions[0][1], mouse_positions[1][1])))

            im.save('screenshot.png')
            listener.stop()


with Listener(on_click=on_click) as listener:

    listener.join()

exit()

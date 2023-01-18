  </t> The python file provides with a function to produce human-like mouse movement from initial cursor position to final cursor position. </br>
  ## Methods
  
  # 1. mouse_move
  Function to be called to move the mouse and click on the target location.</br>
  
  Function parameters:</br>
  1. x_target : x-coordinate of target; integer
  2. y_target : y-coordinate of target; integer
  
  # 2. wind_mouse
  Helper function for mouse_move method. Implements Wind Mouse Movement algorithm (https://ben.land/post/2021/04/25/windmouse-human-mouse-movement/) to mimic non-machine
   like movement.</br>
   
   Function parameters:</br>
   1. start_x : Initial x-coordinate of cursor; int
   2. start_y : Initial y-coordinate of cursor; int
   3. dest_x : Target x-coordinate; int
   4. dest_y : Target y-coordinate; int
   5. G_0 - magnitude of the gravitational force; int
   6. W_0 - magnitude of the wind force fluctuations; int
   7. M_0 - maximum step size (velocity clip threshold); int
   8. D_0 - distance where wind behavior changes from random to damped; int
  
  
    

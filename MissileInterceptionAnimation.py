#!/usr/bin/python3
#-*- coding: utf-8 -*- 

from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import numpy as np
import random

def _measure_position_():
    global Measurement
    X = random.gauss(X_Missile,standard_deviation)
    Y = random.gauss(Y_Missile,standard_deviation)
    Measurement.append([X,Y,t])

    # drawing of the measured points :

    # X-axis error bars
    ax.add_patch(Rectangle((X - 0.0002*Width + standard_deviation, Y - 0.005*Height), 0.0004*Width, 0.01*Height,color="black"))
    ax.add_patch(Rectangle((X - 0.0002*Width - standard_deviation, Y - 0.005*Height), 0.0004*Width, 0.01*Height,color="black"))
    # Y-axis errors bars
    ax.add_patch(Rectangle((X - 0.005*Width, Y - 0.0002*Height  + standard_deviation), 0.01*Width, 0.0004*Height,color="black"))
    ax.add_patch(Rectangle((X - 0.005*Width, Y - 0.0002*Height  - standard_deviation), 0.01*Width, 0.0004*Height,color="black"))
    # cross of the error bars
    ax.add_patch(Rectangle((X - 0.0002*Width, Y - standard_deviation), 0.0004*Width, 2*standard_deviation,color="black"))
    ax.add_patch(Rectangle((X - standard_deviation, Y - 0.0002*Height), 2*standard_deviation, 0.0004*Height,color="black"))
    # point
    ax.add_patch(Rectangle((X - 0.005*Width, Y - 0.005*Width), 0.01*Width, 0.01*Height,color="blue"))

    print(Measurement)
    
def _launch_missile_():
    """ Launch the counter-measure  
    """
    
def Animate():
	"""
	Move the missile and update the canvas with the method update().
	"""
	# access to these variables
	global X_Missile, Y_Missile, VX_Missile, VY_Missile
	global X0_Missile, Y0_Missile, VX0_Missile, VY0_Missile
	global t
	global Missile


	iterations = 0      #Nbr of iterations
	tstep = 1       #time step

	print (" runme = ", runme.get() )
	#while the checkbutton 'Stop' is not checked, animate
	while( not runme.get() ):
		# slow down the animation : 0, 1/10 de seconde .. 
		#time.sleep(0.0)
		X_Missile = VX0_Missile * t + X0_Missile
		Y_Missile = VY0_Missile * t + Y0_Missile
		
		print(iterations, " ", X_Missile, " ", Y_Missile)
		# Update the coordinates of the missile
		Missile.set_offsets(np.c_[X_Missile,Y_Missile])
		
		t += tstep 
		# slow down the animation : 0, 1/10 de seconde .. 
		plt.pause(0.1)
		#Update the canvas
		can1.get_tk_widget().update()
		can1.draw()
		
		iterations += 1 
		
	print (" Total number of iterations : ", iterations )
    
    
def _set_missile_():
	"""
	Set missile parameters based on the input values on the interface.
	"""
	global SizeOfMissile
	global X_Missile, Y_Missile, VX_Missile, VY_Missile
	global X0_Missile, Y0_Missile, VX0_Missile, VY0_Missile
	global Missile
	global Height, Width

	# Get the values of the spinboxes
	# The values are string by default, so we need to convert them
	Spinbox_x0_value        = int(Spinbox_x0    .get())
	Spinbox_y0_value        = int(Spinbox_y0    .get())
	Spinbox_Vx0_value       = int(Spinbox_Vx0   .get())
	Spinbox_Vy0_value       = int(Spinbox_Vy0   .get())

	X_Missile   = Spinbox_x0_value
	Y_Missile   = Spinbox_y0_value
	VX_Missile  = Spinbox_Vx0_value
	VY_Missile  = Spinbox_Vy0_value

	X0_Missile   = Spinbox_x0_value
	Y0_Missile   = Spinbox_y0_value
	VX0_Missile  = Spinbox_Vx0_value
	VY0_Missile  = Spinbox_Vy0_value

	#Draw enemy base
	ax.add_patch(Rectangle((X0_Missile, Y0_Missile), X0_Missile+0.03*Width, Y0_Missile+0.03*Height,color="red"))

	Missile.set_offsets(np.c_[Spinbox_x0_value,Spinbox_y0_value])
	can1.draw()



#_________________________________________________________________________________________________________________________
#      ||||        ||||||||||||||||||||           ||||             |||||||||||||       ||||||||||||||||||||
#    ||    ||              ||||                   ||||             ||          ||              ||||        
#  ||        ||            ||||                  ||  ||            ||           ||             ||||        
#||          ||||          ||||                 ||    ||           ||            ||            ||||        
#  ||                      ||||                ||      ||          ||           ||             ||||        
#    ||                    ||||               ||        ||         ||          ||              ||||        
#      ||||                ||||              ||          ||        |||||||||||||               ||||        
#          ||              ||||             ||||||||||||||||       ||||||||                    ||||        
#            ||            ||||            ||              ||      ||     ||                   ||||        
#||||          ||          ||||           ||                ||     ||      ||                  ||||        
#  ||        ||            ||||          ||                  ||    ||       ||                 ||||        
#    ||    ||              ||||         ||                    ||   ||        ||                ||||        
#      ||||                ||||        ||                      ||  ||         ||               ||||        
#_________________________________________________________________________________________________________________________

#--------------------------------------------------------------------------------
# Set up the interface controlling and displaying the animation
#--------------------------------------------------------------------------------

# Start tk and set a title
#
win1 = Tk()
win1.title("My animation")


Height  = 1e+5
Width   = 1e+5

fig = Figure(figsize=(6, 6), dpi=100)
ax = fig.add_subplot()
fig.subplots_adjust(left=0.15, bottom=0.15)
ax.grid(linestyle='dotted')
ax.axis([0, Width, 0, Height])
line, = ax.plot(0, 0)
ax.set_xlabel("x [ ]")
ax.set_ylabel("y [ ]")
can1 = FigureCanvasTkAgg(fig, master=win1)  # A tk.DrawingArea.

#pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(can1, win1)#, pack_toolbar=False)
toolbar.update()

# Set the size of the missile
SizeOfMissile = 250    

# Create containers for the position and velocity of the missile at the time t of the animation
X_Missile    = 0
Y_Missile    = 0
VX_Missile   = 0
VY_Missile   = 0

X0_Missile    = 0
Y0_Missile    = 0
VX0_Missile   = 0
VY0_Missile   = 0

# Since the animation have not started, set the timer to 0
t = 0

#Draw the missile
Missile = ax.scatter( X_Missile , Y_Missile , s = SizeOfMissile, color="red", marker ="^")

#Draw you
ax.add_patch(Rectangle((0.97*Width, 0), 0.03*Width, 0.03*Height,color="skyblue"))


#Set off of the Measurement list
Measurement = []

#Stadard Deviation :
standard_deviation = 1000

#--------------------------------------------------------------------------------
# Setting up the canvas 
#--------------------------------------------------------------------------------

# All widgets have the method pack, in order to place the slave widget on the master widget (or daughter widget on the parent widget)
#   'pack' can take several options
#       expand : if True fill any space not otherwise used in the parent widget
#       fill : 'none' (default), 'x', 'y', 'both'. Fills any extra space only horizontally ('x'), vertically ('y') or both ('both'), or keep the minimal dimensions
#       side : TOP (default), BOTTOM, LEFT, RIGHT. Describe on which side of the parent widget the daughter widget is drawn.
#       padx =  extra space (in pixels) on the left and right sides of the widget
#       pady =  same thing as padx but on the top and bottom sides of the widget
can1.get_tk_widget().pack()
toolbar.pack(side=TOP, fill="x")

# Create a label frame in which there will be the button to control the missile parameters.
#   first parameter = parent window, here it is win1
#   text = text to be printed out on top of the frame
MissileFrame = LabelFrame(win1, text="Missile parameter")

# Create new label frame, each one will contain a button to control parameters the missile
# Each new label frame should be built upon the main label frame, here it is MissileFrame
#   first parameter : parent window, here it is MissileFrame
#   text = text to be printed out on top of the frame
Frame_x0    = LabelFrame(MissileFrame, text="x0 = "         )
Frame_y0    = LabelFrame(MissileFrame, text="y0 = "         )
Frame_Vx0   = LabelFrame(MissileFrame, text="vx0 = "        )
Frame_Vy0   = LabelFrame(MissileFrame, text="vy0 = "        )


# Create spinboxes : they are boxes with arrows that you can scroll to set the value of the corresponding parameter.
# There is one spinbox per initial parameter
# Also, each spinbox should be built on the corresponding aforecreated label frame
#   first parameter : parent window, here it is AddBallFrame
#   from_ = minimal value
#   to = maximal value
#   wrap = if True, once we pass the min/max value, we arrive at the max/min value.
#   values = tuple with all the possible values
Spinbox_x0      = Spinbox(Frame_x0      , from_=0 , to=1e+5  , wrap = True )
Spinbox_y0      = Spinbox(Frame_y0      , from_=0 , to=1e+5 , wrap = True )
Spinbox_Vx0     = Spinbox(Frame_Vx0     , from_=0 , to=100  , wrap = True )
Spinbox_Vy0     = Spinbox(Frame_Vy0     , from_=0 , to=100 , wrap = True )
button_set_missile 	= Button(master=MissileFrame, text="Add missile", command=_set_missile_)

# Packing order is important. Widgets are processed sequentially and if there
# is no space left, because the window is too small, they are not displayed.
# The canvas is rather flexible in its size, so we pack it last which makes
# sure the UI controls are displayed as long as possible.

#canvas.get_tk_widget().pack(side=TOP, fill="x", expand=1)
#toolbar.pack(side=TOP, fill="x")

MissileFrame.pack(ipadx=0, ipady=0, side='left')

Frame_x0    .pack(fill="y", expand="yes")
Frame_y0    .pack(fill="y", expand="yes")
Frame_Vx0   .pack(fill="y", expand="yes")
Frame_Vy0   .pack(fill="y", expand="yes")

Spinbox_x0      .pack(padx = 10, pady = 10)
Spinbox_y0      .pack(padx = 10, pady = 10)
Spinbox_Vx0     .pack(padx = 10, pady = 10)
Spinbox_Vy0     .pack(padx = 10, pady = 10)
button_set_missile.pack(padx = 10, pady = 10)

# Create buttons to control the animation
#   master  = indicates the parent window, here it is win1
#   text    = Printed text on the button
#   command = command to be executed

# Create a button to exit the animation
Button(master=win1,text='Exit',command=win1.destroy).pack(side=BOTTOM, pady=50)
# Create a button to launch the animation
#   The animation is managed by the function 
Button(master=win1,text='Go',command= Animate).pack(pady=20,  side=TOP)

# Tkinter have its own variables : they are called 'control variables'.
# There are : IntVar(), DoubleVar(), and StringVar() which create control variables of an integer, a float or a string
# One can set the value of such a variable using the function set(value). Ex: runme.set(0)
# Variable value can be accessed with the function get(). Ex : runme.get()
# These variables are useful because they can be used with a button, meaning that the button can change directly the variable #

# runme is an integer which will be equal to 0 or 1 :
#   - 0 : stop the animation
#   - 1 : run the animation
runme = IntVar() 
runme.set(0)

# Create a checkbutton 
#   first parameter : parent window, here it is win1
#   text        = text to be printed out on the button
#   variable    = tell the variable that will be changed when ticking or unticking the box. (set to 0/1 if 1/0 before)

Checkbutton(master=win1, text="Stop", variable=runme).pack()

# Create a button to make a measurement of the missile position
Button(master=win1, text="Measure", command=_measure_position_).pack(pady=20,  side=TOP)
# Create a button to launch the counter-measure
Button(master=win1, text="Launch", command=_launch_missile_).pack(pady=20,  side=TOP)

# Start the main loop, wait for user instructions.
#
win1.mainloop()

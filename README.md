# Tiny_polybar
Hello everyone to create a tiny polybar we need to do few steps

# create a second bar in polybar conf

[bar/tray]

monitor-strict = false

width = 20

height = 25

offset-x = 98% ######### offset values only dtermine the position of bar in the screen set it accordingly to your need

offset-y = 35   



override-redirect = true  ############### to make offset vales to work override-direct value must be true

fixed-center = true

background = ${colors.modules-right-background}

;foreground = ${colors.foreground}

radius = 8

line-size = 0

line-color = #f00


padding-left = 0

padding-right = 1

module-margin-left = 0

module-margin-right = 0


modules-right =  sep

tray-position = right

tray-detached = false

tray-offset-x = 0

tray-offset-y = 0

tray-padding = 1

tray-maxsize = 20

tray-scale = 1.0

tray-background = ${colors.background}

############################################################################

# create a module to access the bar

[module/arrow]

type = custom/script

exec = echo ""

click-left = bash $HOME/.config/polybar/tinybar.sh

click-right = bash $HOME/.config/polybar/killbar.sh


############################################################################

# finally create two scripts to use the bar
First script to launch the bar...

Second script to kill the bar...

the kill script only kill the newly created bar not the whole bar



######################################

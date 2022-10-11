## Tiny_polybar
A tiny polybar for hiding tray icons and modules that are rarely used.

![Tiny_bar](https://user-images.githubusercontent.com/45850093/195213025-12aa73b8-aac4-4cfa-b4b7-3f2aadad7ce9.gif)



## Installation
Clone this repository and move the files to your polybar config location.

Example:
```bash
git clone https://github.com/phon31x/Tiny_polybar
cd Tiny_polybar
cp tinybar.sh killbar.sh ~/.config/polybar
```

## Usage example
1. Change a polybar name in tinybar.sh

```bash
polybar tray (name of your bar here instead of tray) >> /tmp/polybar2.log 2>&1
```

2. Create a second bar in your polybar config. Example of a bar:


```ini
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
```

3. Create a module to access the bar 

```ini

[module/arrow]

type = custom/script

exec = echo ""

click-left = bash $HOME/.config/polybar/tinybar.sh

click-right = bash $HOME/.config/polybar/killbar.sh
```

4. Click left (tinybar) is used to launch the bar. Click right (kill bar) is used to close tiny bar.

##

- Tinybar.sh a script to launch the bar.
- Killbar.sh a script to kill the bar.
- The kill script only kill the newly created bar not the whole bar.

'''
Created on Jul 13, 2018
@author: scy
@IDE: eclipse
'''
import os
import getch

def standard():
    os.system('''
    sudo ufw enable                                             >&/dev/null &  \
    sudo /home/scy/Documents/Scripts/hosts.sh                   >&/dev/null &  \
    sudo /home/scy/Documents/Scripts/veracrypt.sh               >&/dev/null &  \
    twmnd                                                       >&/dev/null &  \
    setxkbmap -layout de                                        >&/dev/null &  \
    xbindkeys                                                   >&/dev/null &  \
    xrdb /home/scy/.Xresources                                  >&/dev/null &  \
    feh --bg-max /home/scy/Pictures/destroyer.jpg               >&/dev/null &  \
    polybar --config=/home/scy/.config/polybar/config scy       >&/dev/null &  \
    nm-applet                                                   >&/dev/null &  \
    compton --config /home/scy/.config/compton/compton.conf     >&/dev/null &  \
    /home/scy/Documents/Scripts/keepass.sh                      >&/dev/null &  \
    signal-desktop                                              >&/dev/null &  \
    discord                                                     >&/dev/null &  \
    cantata                                                     >&/dev/null &  \
    ''')


def programming():
    standard()    
    os.system('''
    eclipse         >&/dev/null &          \  
    ''')    

def pirate():
    standard()    
    os.system('''
    qbittorrent     >&/dev/null &          \
    soulseekqt      >&/dev/null &          \
    ''')   

def surfing():
    standard()    
    os.system('''
    firefox         >&/dev/null &          \
    ''')   
 
 
def gaming():
    standard()    
    os.system('''
    steam           >&/dev/null &          \
    playonlinux     >&/dev/null &          \
    ''')   
           
    
print('PC booted up, what do you want to do')
while True:
    print('''
    1. Programming
    2. Be a pirate
    3. Surfing
    4. Gaming
    ''')
    
    choice = getch.getch()
    if choice in ['1', '2', '3', '4']:
        break
        
        
if choice.upper() == '1':
    programming()

elif choice.upper() == '2':
    pirate()
    
elif choice.upper() == '3':
    surfing()
    
elif choice.upper() == '4':
    gaming()

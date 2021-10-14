#this file controls web browsers, any change to this file may break whole program
import keyboard

def zoomJoin():
    time.sleep(5)
    obj = driver.switch_to.alert
    obj.accept()


def googleJoin():
    time.sleep(6) # takes time to load cam and glitches sometimes so i set it higher
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True) #turning off mic
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True) #turning off cam
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True) #join
 

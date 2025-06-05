import pynput.keyboard

log = ""

def process_key_process(key):
    global log
    try:
        log += key.char
    except AttributeError:
        log += f" [{key}]"

def report():
    print(log)

keyboard_listener = pynput.keyboard.Listener(on_press = process_key_process)
keyboard_listener.start()

input("Press Enter to STOP...\n")
report()

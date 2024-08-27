
import time, sys, keyboard

target = int(sys.argv[1])

for counter in range(1, target + 1):
    if keyboard.is_pressed('space'):
        print("Counter stopped by pressing space key.")
        break

    print(counter)
    time.sleep(1)


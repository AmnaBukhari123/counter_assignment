import time
import keyboard
import argparse

def main():
  parser = argparse.ArgumentParser( prog="Commandline app",
                                  description="Counter interruption by space key")

  parser.add_argument('--target', type=int, required=True)
    
  args = parser.parse_args()
  target = args.target

  for counter in range(1, target + 1):
        if keyboard.is_pressed('space'):
            print("Counter stopped by pressing space key.")
            break

        print(counter)
        time.sleep(1)


if __name__ ==  '__main__':
      main()

from pyfiglet import Figlet
import time

if __name__ == "__main__":
    f = Figlet(font='big')
    
    while True:
        print(f.renderText('CARRIER'))
        time.sleep(0.5)

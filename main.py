import eel
import os

def main() -> None:
    eel.init("web")
    eel.start('index.html')
   
if __name__ == "__main__":
    main()
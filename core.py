import time
import os

def breathe_fire(duration=0.5, cycles=None):
    fire1 = """
     ***
    *****
   *******
  *********
 ***********
    """.strip()
    
    fire2 = """
     ***
    *****
   *******
  *********
 ***********
    FLAME
    """.strip()
    
    count = 0
    while cycles is None or count < cycles:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(fire1)
        time.sleep(duration)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(fire2)
        time.sleep(duration)
        if cycles:
            count += 1

import argparse
from .core import breathe_fire

def main():
    parser = argparse.ArgumentParser(description="PyFire: Terminal fire animation")
    parser.add_argument("-d", "--duration", type=float, default=0.5)
    parser.add_argument("-c", "--cycles", type=int)
    args = parser.parse_args()
    try:
        breathe_fire(duration=args.duration, cycles=args.cycles)
    except KeyboardInterrupt:
        print("\n🔥 Fire out!")

if __name__ == "__main__":
    main()

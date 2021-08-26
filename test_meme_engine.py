"""Test Script that should not be turned in, for dev porpises only."""

from MemeEngine import MemeEngine

def main():
    """Do Some simple smoke tests."""
    # meme_path = MemeEngine.make_mem("./_data/photos/dog/xander_1.jpg", "Lol", "Nick")
    meme_path = MemeEngine.make_mem("./_data/photos/dog/rofl.jpg", "Lol", "Nick")
    print(meme_path)

if __name__ == "__main__":
    main()
import argparse

from prime_one.poems import get_random_poem, declaim

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('declaim', help='Declaim a random poem')
    args = parser.parse_args()

    if args.declaim:
        poem = get_random_poem()
        declaim(poem['title'], poem['poem'], poem['author'])
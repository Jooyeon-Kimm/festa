import argparse
from videoShowing import *

def run():
    parser = argparse.ArgumentParser(description="Deagu Startup Festa 2023")
    parser.add_argument("--exercise-type", type=str, default="squat", help="exercise type")

    args = parser.parse_args()

    exercise_type = args.exercise_type

    if args.exercise_type in ['lunge', 'plank', 'squat']:
        video_showing(exercise_type)
    else:
        raise ValueError('This exercise has not yet been added to the function.')


if __name__ == "__main__":
    # type "python main.py --exercise-type=squat" for example
    run()
    

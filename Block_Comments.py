# The main function will parse arguments via the parser variable.  These
# arguments will be defined by the user on the console.  This will pass
# the word argument the user wants to parse along with the filename the
# user wants to use, and also provide help text if the user does not
# correctly pass the arguments.

import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "word",
        help="the word to be searched for in the text file."
    )
    parser.add_argument(
        "filenames",
        nargs='+',
        help="the paths to the text files to be searched through"
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Access the arguments
    word_to_search = args.word.casefold()
    filenames = args.filenames
    
    # Implement logic to search for the word in the files
    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                content = file.read().casefold()
                if re.search(r'\b' + re.escape(word_to_search) + r'\b', content):
                    print(f"'{word_to_search}' found in {filename}.")
                else:
                    print(f"'{word_to_search}' not found in {filename}.")
        except (FileNotFoundError, PermissionError, IOError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
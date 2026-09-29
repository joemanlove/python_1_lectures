"""
File Path Solutions Lecture written by Joe Manlove

This has been revised on 9/22/2026 from a number of previous scripts and uses a solution that is more modern than using os.path.join.
"""

from pathlib import Path

# Make a Path object out of the script's location.
SCRIPT_PATH = Path(__file__)
print(f"The script is at: {SCRIPT_PATH}")

# Make a Path object for the Folder the script is in.
DIRECTORY_PATH = SCRIPT_PATH.resolve().parent
print(f"The parent folder is: {DIRECTORY_PATH}")

# Make a Path object for the output file. This is a clever way someone used the fact that you can control how division acts.
OUTPUT_PATH = DIRECTORY_PATH / "output.txt"
print(OUTPUT_PATH)

# Create a file at OUTPUT_FILE_PATH, will work regardless of the working directory and operating system.
with open(OUTPUT_PATH, 'w') as output_stream:
    output_stream.write("This is a test string...")

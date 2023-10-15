

# Open all the .nanorc files in the current directory
import glob

# Get a list of all .nanorc files in the current directory
nanorc_files = glob.glob("*.nanorc")

# Open each .nanorc file, except for nanorc.nanorc
files = []
for file in nanorc_files:
    if file == "nanorc.nanorc":
        continue
    f = open(file, "r")
    files.append((file, f, f.read()))

# Replace "black" with "blue" in each .nanorc file
for filename, file, content in files:
    with open(filename, "w") as f:
        f.truncate()
        f.write(content.replace("black", "blue"))
        f.close()

import os

# Define the root directory where README files are located
root_directory = "./"

# Define a function that recursively finds all README files in subdirectories
def find_readme_files(directory):
    readme_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "README.md":
                readme_files.append(os.path.join(root, file))
    return readme_files

# Call the function to find all README files
readme_files = find_readme_files(root_directory)

# Define a function to merge multiple README files into one file
def merge_readme_files(readme_files):
    merged_content = ""
    for file in readme_files:
        with open(file, "r") as f:
            content = f.read()
            merged_content += content + "\n\n"
    return merged_content

# Call the function to merge all README files
merged_content = merge_readme_files(readme_files)

# Write the merged content to a new file called "MERGED_README.md" in the root directory
with open(os.path.join(root_directory, "MERGED_README.md"), "w") as f:
    f.write(merged_content)

import os

readme_files = [f for f in os.listdir() if f.startswith('README') and f.endswith('.md')]

with open('README.md', 'w') as outfile:
    for fname in readme_files:
        with open(fname) as infile:
            outfile.write(infile.read())

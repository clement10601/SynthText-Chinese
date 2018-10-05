import os

target_dir = 'cht'
output_file = 'fontlist.txt'
dirs = os.listdir(target_dir)

with open(output_file, 'w') as f:
    for d in dirs:
        f.write('{}\n'.format(os.path.join(target_dir, d)))
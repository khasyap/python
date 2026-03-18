with open("readme.md", 'r') as fp_in, open("numbered.txt", 'w') as fp_out:
    for i, line in enumerate(fp_in, 1):
        fp_out.write(f"{i} {line}")

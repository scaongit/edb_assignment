# edb assignment, rotate a matrix 90 degrees
def rotate(filename, rotation_degree):
    if rotation_degree != 90:
        return "cannot rotate image"
    if not filename.endswith('.pbm'):
        return "invalid file provided"

    with open(filename, "r") as f:
        arr = [list(map(int, line.strip().split())) for line in f.readlines()[3:]]

    rotate_mt = list(list(x)[::-1] for x in zip(*arr))
    rows = len(rotate_mt)
    cols = len(rotate_mt[0])
    with open('output.pbm', 'w') as fw:
        fw.write("P1\n#comment\n{rows} {cols} \n".format(rows=rows, cols=cols))
        fw.write("\n".join(" ".join(str(i) for i in j) for j in rotate_mt))


if __name__ == '__main__':
    rotate('test01.pbm', 90)


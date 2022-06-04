# edb assignment, rotate a matrix 90 degrees clockwise and anticlockwise without external libraries

def rot_90_clockwise(matrix):
    # rotate 90 degree a matrix
    return list(list(x)[::-1] for x in zip(*matrix))


def rot_90_anticlockwise(matrix):
    # transpose a matrix
    rows = len(matrix)
    cols = len(matrix[0])

    mtx_t = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        mtx_t.append(row)

    return mtx_t


def rotate(filename, rotation_degree):

    if not filename.endswith('.pbm'):
        return "invalid file provided"

    if rotation_degree not in (90, -90, 180, -180):
        return "cannot rotate image"

    # open the file and put content in arr
    with open(filename, "r") as f:
        arr = [list(map(int, line.strip().split())) for line in f.readlines()[3:]]

    # check the rotation degree
    if rotation_degree == 90 or rotation_degree == -180:
        rotate_mt = rot_90_clockwise(arr)
    elif rotation_degree == 180 or rotation_degree == -90:
        rotate_mt = rot_90_anticlockwise(arr)

    rows = len(rotate_mt)
    cols = len(rotate_mt[0])

    # write the output file with matrix rotated
    with open('output.pbm', 'w') as fw:
        fw.write("P1\n#comment\n{rows} {cols} \n".format(rows=rows, cols=cols))
        fw.write("\n".join(" ".join(str(i) for i in j) for j in rotate_mt))
        return "rotation completed"


if __name__ == '__main__':
    print(rotate('test01.pbm', 180))



def raw_file(file_handle: str) -> list:
    with open(file_handle) as f:
        return f.readlines()


def remove_n(file: list) -> list:
    output: list = []
    for element in file:
        output.append(element[:-1])
    return output

#
# p = raw_file("valid-wordle-words.txt")
# g = remove_n(p)
# print(g)




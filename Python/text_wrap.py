import textwrap


def wrap(string, max_width):
    res = textwrap.wrap(string, max_width)
    return "\n".join([r for r in res])


string = input()
max_width = int(input())
wrap(string, max_width)

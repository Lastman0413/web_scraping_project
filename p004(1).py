import re
p = re.compile("ca.e")

def print_match(m):

    if m:
        print(m.group())
    else:
        print("매칭되지 않았습니다.")

m = p.match("cafe")
print_match(m)
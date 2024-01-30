#!/usr/bin/python3
for f in range(10):
    for i in range(f, 10):
        if f < i:
            print("{:d}{:d}".format(f, i),
                  end="\n" if f == 8 and i == 9 else ", ")

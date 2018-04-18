#!/usr/bin/env python3

with open("cik-lookup-data.html") as file:
    for line in file:
        try:
            with open("cik.txt", "a") as f:
                f.write(line[-12:-2] + '\n')
                f.close()
        except:
            pass



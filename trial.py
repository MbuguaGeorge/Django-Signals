def initial():
        first = input()
        last = input()
        aid = first +' '+ last
        print(aid)
        xs = aid
        new = xs.split()

        first = ''
        last = ''
        for namec in new:
                first += new[0][0]
                last += new[1][0]

                initials = first + last

                return (initials)
print(initial())
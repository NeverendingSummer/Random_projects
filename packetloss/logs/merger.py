filenames = ['01-52-28 26_04 100b.txt',
             '02-03-16 26_04 100b.txt',
             '13-37-12 27_04 100b.txt',
             '16-51-38 26_04 100b.txt',
             '17-06-06 27_04 100b.txt',
             '17-21-44 25_04 100b.txt',
             '17-54-25 27_04 100b.txt',
             '18-30-03 27_04 100b.txt',
             '20-45-22 01_05 100b.txt',
             '22-40-39 26_04 100b.txt',
             '23-34-43 27_04 100b.txt'
             ]
with open('one_for_all_new_100b.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

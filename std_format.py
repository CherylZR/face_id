inname = '.\\files\ori\person-id-name_utf8.txt'
outname = '.\\files\ori\person-id-name-std2.txt'

with open(inname, 'r', encoding='utf8') as infile:
    i = 0
    for line in infile.readlines():
        # i +=1
        # if i>5:
        #     break
        # print(line)
        newline = line.strip().replace('\t', ' ')
        # print(newline)
        outfile = open(outname, 'a', encoding='utf8')
        outfile.write(newline + '\n')
        outfile.close()

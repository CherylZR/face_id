import csv

if __name__=='__main__':
    oriname = '.\\files\\namelist.txt'
    overlapname = '.\\files\overlap_trans.txt'
    outname = '.\\files\overlap_ori.txt'
    outfile = open(outname, 'a', encoding='utf8')
    name_dict = {}
    overlap_dict = {}

    with open(oriname, 'r', encoding='utf8') as orifile:
        spamreader = csv.reader(orifile, delimiter=' ')
        i = 0
        for line in spamreader:
            i += 1
            if i == 1:
                continue
            id_ori = line[0]
            name_ori = '_'.join(line[1:])
            name_dict[id_ori] = name_ori.strip('_')

    with open(overlapname, 'r', encoding='utf8') as overlapfile:
        spamreader = csv.reader(overlapfile, delimiter=' ')
        for line_list in spamreader:
            if len(line_list) < 100:
                print(line_list)
            else:
                print('this line is too long to print')
            for i in range(1, len(line_list), 2):
                name_ori = name_dict.get(line_list[i])
                line_list[i-1] = name_ori
            line_list += '\n'
            outfile.write(' '.join(line_list))

    outfile.close()

import csv

# def is_number(uchar):
#     return uchar >= u'0' and uchar<=u'9'
#
# def find_idx(name):
#     idx = 0
#     for uchar in name:
#         if is_number(uchar):
#             idx += 1
#         else:
#             return idx

if __name__=='__main__':
    inname = '.\\files\checked_entity_list_20180612.txt'
    overlapname = '.\\files\entity_overlap.txt'
    outname = '.\\files\entity_overlap_ori.txt'
    # infile = open(inname, 'r', encoding='utf8')
    outfile = open(outname, 'a', encoding='utf8')
    name_dict = {}
    overlap_dict = {}

    # for line in infile.readlines():
    #     strip_line = line.strip().replace(' ', '')
    #     idx = find_idx(strip_line)
    #     id_ori = strip_line[:idx]
    #     name_ori = strip_line[idx:]
    #     name_dict[id_ori] = name_ori

    with open(inname, 'r', encoding='utf8') as infile:
        spamreader = csv.reader(infile, delimiter=' ')
        i = 0
        for line in spamreader:
            i += 1
            if i == 1:
                continue
            id_ori = line[0]
            name_ori = '_'.join(line[1:-1])
            name_dict[id_ori] = name_ori.strip()

    with open(overlapname, 'r', encoding='utf8') as overlapfile:
        spamreader = csv.reader(overlapfile, delimiter=' ')
        for line_list in spamreader:
            print(line_list)
            for i in range(1, len(line_list), 2):
                name_ori = name_dict.get(line_list[i])
                line_list[i-1] = name_ori
            line_list += '\n'
            outfile.write(' '.join(line_list))

    outfile.close()
    # infile.close()

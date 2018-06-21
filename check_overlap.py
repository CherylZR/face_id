import csv

def inverse_name(name):
    full_name = name.split()
    full_name[0], full_name[-1] = full_name[-1], full_name[0]
    name_inv = '_'.join([subword for subword in full_name])

def is_number(uchar):
    return uchar >= u'0' and uchar<=u'9'

def find_idx(name):
    idx = 0
    for uchar in name:
        if is_number(uchar):
            idx += 1
        else:
            return idx

if __name__=='__main__':
    inname = '.\\files\\translist_all.txt'
    outname = '.\\files\\overlap_trans1.txt'
    # infile = open(inname, 'r', encoding='utf8')
    outfile = open(outname, 'a', encoding='utf8')
    name_dict = {}
    overlap_dict = {}
    i=0

    with open(inname, 'r', encoding='utf8') as infile:
        spamreader = csv.reader(infile, delimiter=' ')
        for line in spamreader:
            # i += 1
            # if i>5:
            #     break
            id = line[0]
            name = line[1].lower()
            id_dict = name_dict.get(name)
            if id_dict:
                if overlap_dict.get(name):
                    overlap_dict[name] = overlap_dict[name] + ' %s %s' % (name, id)
                else:
                    overlap_dict[name] = ' '.join([id_dict, name, id])
                print('%s have ids [%s, %s]' % (name, id_dict, id))
            else:
                name_dict[name] = id
                print('[id:%s name:%s] is added' % (id, name))

            name_inv = inverse_name(name)
            id_inv = name_dict.get(name_inv)
            if id_inv:
                if overlap_dict.get(name_inv):
                    overlap_dict[name_inv] = overlap_dict[name_inv] + ' %s %s' % (name, id)
                else:
                    overlap_dict[name_inv] = ' '.join([id_inv, name, id])
                print('%s have ids [%s, %s]' % (name_inv, id_inv, id))

                # TODO: search wiki for single-word name

        for key, val in overlap_dict.items():
            outfile.write(key + ' ' + val + '\n')
        outfile.close()
        #
        # name_inv = inverse_name(name)
        # id_inv = name_dict.get(name_inv, -1)
        # if id_same != -1:

    # for line in infile.readlines():
    #     # i+=1
    #     # if i>5000:
    #     #     break
    #     strip_line = line.strip().replace(' ','')
    #     idx = find_idx(strip_line)
    #     name = strip_line[idx:].lower()
    #     id = strip_line[:idx]
    #     id_dict = name_dict.get(name)
    #     if id_dict:
    #         if overlap_dict.get(name):
    #             overlap_dict[name] = overlap_dict[name] + ' %s %s' %(name, id)
    #         else:
    #             overlap_dict[name] = ' '.join([id_dict, name, id])
    #         print('%s have ids [%s, %s]' % (name, id_dict, id))
    #     else:
    #         name_dict[name] = id
    #         print('[id:%s name:%s] is added' % (id, name))
    #
    #     name_inv = inverse_name(name)
    #     id_inv = name_dict.get(name_inv)
    #     if id_inv:
    #         if overlap_dict.get(name_inv):
    #             overlap_dict[name_inv] = overlap_dict[name_inv] + ' %s %s' % (name, id)
    #         else:
    #             overlap_dict[name_inv] = ' '.join([id_inv, name, id])
    #         print('%s have ids [%s, %s]' % (name_inv, id_inv, id))
    #
    #     #TODO: search wiki for single-word name
    #
    # for key, val in overlap_dict.items():
    #     outfile.write(key + ' ' + val + '\n')
    # outfile.close()
        #
        # name_inv = inverse_name(name)
        # id_inv = name_dict.get(name_inv, -1)
        # if id_same != -1:
        #     overlap_dict[]

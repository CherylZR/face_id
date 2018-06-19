
def inverse_name(name):
    full_name = name.split()
    full_name[0], full_name[-1] = full_name[-1], full_name[0]
    name_inv = ' '.join([subword for subword in full_name])

if __name__=='__main__':
    inname = '.\\files\out_entity\entity_list_all.txt'
    outname = '.\\files\out_entity\entity_overlap_new.txt'
    infile = open(inname, 'r', encoding='utf8')
    outfile = open(outname, 'a', encoding='utf8')
    name_dict = {}
    overlap_dict = {}
    i=0
    for line in infile.readlines():
        # i+=1
        # if i>5000:
        #     break
        strip_line = line.strip().replace(' ','').replace('_',' ')
        name = strip_line[9:].lower()
        id = strip_line[:9]
        id_dict = name_dict.get(name)
        if id_dict:
            if overlap_dict.get(name):
                overlap_dict[name] = overlap_dict[name] + ' %s %s' %(name, id)
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

        #TODO: search wiki for single-word name

    for key, val in overlap_dict.items():
        outfile.write(key + ' ' + val + '\n')
    outfile.close()
        #
        # name_inv = inverse_name(name)
        # id_inv = name_dict.get(name_inv, -1)
        # if id_same != -1:
        #     overlap_dict[]


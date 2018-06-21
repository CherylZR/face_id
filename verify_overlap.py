import csv
import wikipedia

if __name__ == '__main__':
    # oriname = '.\\files\\namelist_all.txt'
    inname = '.\\files\overlap_ori.txt'
    outname = '.\\files\overlap_conf1.txt'

    # ori_dict = {}
    # with open(oriname, 'r', encoding='utf8') as orifile:
    #     spamreader = csv.reader(orifile, delimiter=' ')
    #     for line in spamreader:
    #         id = line[0]
    #         name = '_'.join(line[1:-1])
    #         ori_dict[id] = name
    #
    # all_dict = {}
    wikipedia.set_lang('zh')

    j = 0
    with open(inname, 'r', encoding='utf8') as infile:
        spamreader = csv.reader(infile, delimiter=' ')
        for line in spamreader:

            # if j>7:
                # break
            line_dict = {}
            overlap_dict = {}
            distinc_dict = {}
            if len(line)>=10:
                j += 1
                for i in range(0, len(line)-1, 2):
                    name = line[i]
                    id = line[i+1]
                    if line_dict.get(name):
                        if overlap_dict.get(name):
                            overlap_dict[name] = overlap_dict[name] + ' %s %s'%(name, id)
                        else:
                            overlap_dict[name] = name + line_dict[name] + ' %s %s'%(name, id)
                    else:
                        line_dict[name] = id
                for key, val in overlap_dict.items():
                    outfile = open(outname, 'a', encoding='utf8')
                    write_line = val + '\n'
                    outfile.write(write_line)
                    outfile.close()
                print('line %s finished'%j)
            else:
                j+=1
                for i in range(0, len(line)-1, 2):
                    name = line[i]
                    id = line[i+1]
                    search_name = wikipedia.search(name)[0]
                    if overlap_dict.get(search_name):
                        overlap_dict[search_name] += ' %s %s'%(name, id)
                    else:
                        overlap_dict[search_name] = name + ' ' + id
                for key, val in overlap_dict.items():
                    val_list = val.split(' ')
                    if len(val_list) <= 2:
                        continue
                    else:
                        write_line = val + '\n'
                        outfile = open(outname, 'a', encoding='utf8')
                        outfile.write(write_line)
                        outfile.close()
                print('line %s finished'%j)



    #         for i in range(0, len(line)-1, 2):
    #             name = line[i]
    #             id = line[i+1]
    #             search_result = wikipedia.search(name)
    #             if all_dict.get(search_result[0]):
    #                 all_dict[search_result[0]] = all_dict[search_result[0]] + ' %s %s' % (name, id)
    #                 print('ref_name %s has another name %s and id %s' % (search_result[0], name, id))
    #             else:
    #                 all_dict[search_result[0]] = id
    #                 print('id %s ref_name %s is added' % (id, search_result[0]))
    #
    # for key, val in all_dict.items():
    #     outfile = open(outname, 'a', encoding='utf8')
    #     item_list = val.split(' ')
    #     id_replace = item_list[0]
    #     name_replace = ori_dict.get(id_replace)
    #     write_line = [name_replace,] + item_list + ['\n',]
    #     outfile.write(' '.join(write_line))
    #     outfile.close()



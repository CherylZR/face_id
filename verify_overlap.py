import csv
import wikipedia

if __name__ == '__main__':
    oriname = '.\\files\checked_entity_list_20180612.txt'
    inname = '.\\files\entity_overlap_ori.txt'
    outname = '.\\files\entity_overlap_final.txt'
    infile = open(inname, 'r', encoding='utf8')

    ori_dict = {}
    with open(oriname, 'r', encoding='utf8') as orifile:
        spamreader = csv.reader(orifile, delimiter=' ')
        for line in spamreader:
            id = line[0]
            name = '_'.join(line[1:-1])
            ori_dict[id] = name

    all_dict = {}
    wikipedia.set_lang('zh')
    j = 0
    with open(inname, 'r', encoding='utf8') as infile:
        spamreader = csv.reader(infile, delimiter=' ')
        for line in spamreader:
            # j += 1
            # if j>4:
            #     break
            for i in range(0, len(line)-1, 2):
                name = line[i]
                id = line[i+1]
                search_result = wikipedia.search(name)
                if all_dict.get(search_result[0]):
                    all_dict[search_result[0]] = all_dict[search_result[0]] + ' %s %s' % (name, id)
                    print('ref_name %s has another name %s and id %s' % (search_result[0], name, id))
                else:
                    all_dict[search_result[0]] = id
                    print('id %s ref_name %s is added' % (id, search_result[0]))

    for key, val in all_dict.items():
        outfile = open(outname, 'a', encoding='utf8')
        item_list = val.split(' ')
        id_replace = item_list[0]
        name_replace = ori_dict.get(id_replace)
        write_line = [name_replace,] + item_list + ['\n',]
        outfile.write(' '.join(write_line))
        outfile.close()



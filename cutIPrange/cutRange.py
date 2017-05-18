#!/usr/bin/env python
# coding=utf-8

import sys

if __name__ == '__main__':

    read_path = sys.path[0] + "/range.txt"
    range_list = []
    temp_count = 0
    page_index = 0
    try:
        file_object = open(read_path)
        for line in file_object:
            range_list.append(line)
            temp_count += 1
            if temp_count == int(sys.argv[1]):
                temp_count = 0
                page_index += 1
                write_path = sys.path[0] + "/rangeFiles/range" + str(page_index) + ".txt"

                with open(write_path, 'wb') as f:
                    for host in range_list:
                        f.write(host)
                    f.flush()
                    f.close()

                range_list = []
        if temp_count > 0:
            page_index += 1
            write_path = sys.path[0] + "/rangeFiles/range" + str(page_index) + ".txt"
            with open(write_path, 'wb') as f:
                for host in range_list:
                    f.write(host)
                f.flush()
                f.close()
        file_object.close()
    except Exception, e:
        print e
import urllib
import os


dir = "C:\\Users\\staho\\Desktop\\stefan"

def open_file_fetch_files_save_to_disk(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        size = len(lines)
        current = 0
        for e in lines:
            start_pos = e.find('https://serwer1438043.home.pl') + len('https://serwer1438043.home.pl')
            file = os.path.abspath(e[start_pos:])
            path = (dir + file[2:]).strip()
            dir_path = path[:path.rfind("\\")]
            try:
                os.makedirs(dir_path)
            except:
                pass
            resource = urllib.urlopen(e.strip())
            output = open(path, "wb")
            output.write(resource.read())
            output.close()
            current += 1
            print(str(current) + "/" + str(size))
        print "finished"

file_chujek_alles = 'C:\\Users\\staho\\Desktop\\stefan\\all_urls_euro-teile-kfz'
file_chujek_unique = 'C:\\Users\\staho\\Desktop\\stefan\\unique_urls_euro-teile-kfz'
file_name = "C:\\Users\\staho\\Desktop\\stefan\\files"

open_file_fetch_files_save_to_disk(file_chujek_unique)
open_file_fetch_files_save_to_disk(file_chujek_alles)
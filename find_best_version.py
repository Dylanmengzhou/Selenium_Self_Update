import minimum_edit_distance
import platform
import os

def find_version(dic,chromePath):
    chrome_version = os.popen(f"{chromePath} --version").read().strip('Google Chrome ').strip()
    operating_system = platform.system()
    mini = []
    for i in dic.keys():
        mini.append(minimum_edit_distance.min_distance(i, chrome_version))
    version_index = mini.index(min(mini))
    keys_list = list(dic)
    final_url = dic[keys_list[version_index]]
    final_version = keys_list[version_index]
    return final_version, operating_system

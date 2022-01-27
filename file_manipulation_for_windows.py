import shutil
import os
def unzip_direct(inputPath):
    os.system('cd {}'.format(inputPath))

    a = os.system('del {}chromedriver'.format(inputPath))
    if a == 0:
        print('Deleting the exist file')
    else:
        print('There is no such file, safe to move')
    shutil.unpack_archive("chromedriver_win32.zip",extract_dir=inputPath)
    os.system('del chromedriver.zip')
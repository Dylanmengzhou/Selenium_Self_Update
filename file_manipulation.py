import os


def unzip_direct(inputPath):
    os.system('cd {}'.format(inputPath))

    a = os.system('rm {}chromedriver'.format(inputPath))
    if a == 0:
        print('Deleting the exist file')
    else:
        print('There is no such file, safe to move')
    os.system('unzip chromedriver.zip -d {}'.format(inputPath))
    os.system('rm chromedriver.zip')

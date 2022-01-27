import os


def get_download_url(final_version, operating_system):
    base_url = "https://chromedriver.storage.googleapis.com/"
    if operating_system == "Windows":
        download_url = base_url + "{}/chromedriver_win32.zip".format(final_version)
    elif operating_system == "Darwin":
        version = os.popen('uname -m').readlines()[0].strip("\n")
        if version == 'arm64':

            download_url = base_url + "{}/chromedriver_mac64_m1.zip".format(final_version)
        elif version == 'x86_64':
            download_url = base_url + "{}/chromedriver_mac64.zip".format(final_version)

    elif operating_system == "Linux":
        download_url = base_url + "{}/chromedriver_linux64.zip".format(final_version)
    return download_url

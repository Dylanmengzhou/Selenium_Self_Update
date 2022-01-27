import crawling
import requests
import file_manipulation
import download_url
import file_manipulation_for_windows
import find_best_version
import read_default_variable
import install_requirement

if __name__ == '__main__':
    default = read_default_variable.read("Default_package.json")

    user_agent = {
        "User-Agent": "{}".format(default['User_agent'])
    }
    url = "https://chromedriver.chromium.org/downloads"
    dic = crawling.get_all_version(url, user_agent)
    final_version, operating_system = find_best_version.find_version(dic, default['Chrome_install_path'])
    download_url = download_url.get_download_url(final_version, operating_system)
    res = requests.get(download_url, headers=user_agent, stream=True)
    with open("chromedriver.zip", "wb") as f:
        f.write(res.content)
    f.close()
    if operating_system == "Windows":
        file_manipulation_for_windows.unzip_direct(default['Python_install_path'])
    else:
        file_manipulation.unzip_direct(default['Python_install_path'])
    import test_selenium

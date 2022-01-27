from lxml import etree
import requests


def get_all_version(url, user_agent):
    re = requests.get(url, headers=user_agent)
    html = etree.HTML(re.text)
    dic = {}
    all_p_path = "/html/body/div[1]/div/div[2]/div[2]/div[1]/section[2]/div[2]/div/div/div/div/div/div/div/div/p"
    all_p = html.xpath(all_p_path)
    for version in all_p:
        try:
            version_name = version.xpath('./span/a/strong/text()')[0]
            version_url = version.xpath("./span/a/@href")[0]
            sub_dic = {'{}'.format(version_name.replace("ChromeDriver ", "")): '{}'.format(version_url)}
            dic.update(sub_dic)
        except:
            pass
    return dic

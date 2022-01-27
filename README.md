# selenium_self_update

## 项目简介

此项目一共有十二个文件，主要功能是能自动找到与自己chrome版本向匹配的selenium版本

## 用法

首先需要配置Default_package.json文件，在这里需要将:

`User_agent` ：UA头

`Chrome_install_path`: Chrome安装路径

`Python_install_path`: python安装路径

三个变量根据自己的电脑配置好。这其中`Python_install_path`需要配置当前用的python路径

## 文件

1. crawling.py
2. download_url.py
3. file_manipulation.py
4. file_manipulation_for_windows.py
5. find_best_version.py
6. install_requirement.py
7. minimum_edit_distance.py
8. read_default_variable.py
9. test_selenium.py
10. main.py
11. Default_package.json
12. requirements.txt

## 1. crawling.py

### 功能

爬取selenium chromedriver官网的版本号以及版本链接

### 输入

url (字符串)
例：https://chromedriver.chromium.org/downloads

user_agent (字典)
例：

``` python
user_agent = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3_7) AppleWebKit/527.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/527.36",
	}
```

### 输出

dic (字典)
例：

``` python
{'98.0.4758.48': 'https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.48/', '97.0.4692.71': 'https://chromedriver.storage.googleapis.com/index.html?path=97.0.4692.71/'}
```

## 2. download_url.py

### 功能

根据最终版本以及操作系统获得下载链接

### 输入

final_version (字符串)
例：'98.0.4758.48'

operating_system (字符串)

例：'Darwin'

### 输出

download_url (字符串)

例：'https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.48/'



## 3. file_manipulation.py

### 功能

删除python安装路径下原有的chromedriver文件并将下载好的版本解压到该目录，完成后删除原zip文件（只针对于macOS以及Linux）

### 输入

inputPath (字符串)

例："/Library/Frameworks/Python.framework/Versions/3.10/bin/"

### 无输出



## 4. file_manipulation_for_windows.py

### 功能

删除python安装路径下原有的chromedriver文件并将下载好的版本解压到该目录，完成后删除原zip文件（只针对于Windows）

## 输入

inputPath (字符串)

例："D:\Download\Compression\Selenium_Self_Update-main\venv\Scripts\"

## 无输出



## 5. find_best_version.py

### 功能

根据chrome版本查找最接近的chromedriver版本

### 输入

dic (字典)

例：

``` python
{'98.0.4758.48': 'https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.48/', '97.0.4692.71': 'https://chromedriver.storage.googleapis.com/index.html?path=97.0.4692.71/'}
```

chromePath (字符串)

例："/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome"

### 输出

final_version (字符串)
例：'98.0.4758.48'

operating_system (字符串)

例：'Darwin'



## 6. install_requirement.py

### 功能

检查并安装依赖的库

### 输入

requirements.txt (文本文件)

### 无输出





## 7. minimum_edit_distance.py

### 功能

检查两个版本的最短距离

### 输入



### 输出



## 8. read_default_variable.py

### 功能

读取Default_package.json里的变量



### 输入

file (文本)

例："Default_package.json"

### 输出

variables (字典)

例：

``` python
{
    "User_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Chrome_install_path":"/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome",
    "Python_install_path":"/Library/Frameworks/Python.framework/Versions/3.10/bin/"
}
```

## 9. test_selenium.py

### 功能

检查此项目是否成功



## 10. main.py

### 功能

主函数入口

## 11. requirements.txt

### 功能

将所有的模块包的名称以及版本存放到里边

![202201286B7LaY](https://raw.githubusercontent.com/Dylanmengzhou/picbed/master/uPic/202201286B7LaY.png)



## 12. Default_package.json

### 功能

存放`UA头`,`Chrome安装路径`,`python安装路径`变量的文件

![20220128tulgee](https://raw.githubusercontent.com/Dylanmengzhou/picbed/master/uPic/20220128tulgee.png)



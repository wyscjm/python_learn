# python_learn
learn python



# selenium exe
When you use selenium you should do this as below

1. download python3.4.4 and install it
2. pip install selenium
3. pip instatl py2exe
4. download the https://github.com/mozilla/geckodriver/releases 's exe
then copy to root of python.exe,if you use firefox.
5. python setup.py py2exe generate the exe software.

```
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

#driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver = webdriver.Firefox()
driver.get('http://blog.csdn.net/huilan_same')
time.sleep(5)
driver.quit()
```

``` python
# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe, sys
sys.argv.append('py2exe')

options = {"py2exe": {
    "compressed": 1,  # 压缩
    "optimize": 2,
    "bundle_files": 1,  # 所有文件打包成一个exe文件
}}

setup(
    console=[{'script': "blog.py", "icon_resources": [(1, "robot.ico")]}],
    options=options,
    zipfile=None
)
```

# PyQt官网
官网：https://www.riverbankcomputing.com/software/pyqt/download5
pip install PyQt5

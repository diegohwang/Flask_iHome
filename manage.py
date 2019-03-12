#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: DreamyHwang
# @Time: 2019/3/12 18:29

from flask import Flask

"""在单一文件中构建所有依赖工具"""

app = Flask(__name__)

@app.route("/index")
def index():
    return "index page"



if __name__ == "__main__":
    app.run()

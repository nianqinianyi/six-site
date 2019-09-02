"""
Copyright (c) [2019] [sixlab.cn]
[https://github.com/PatrickRoot/six-site] is licensed under the Mulan PSL v1.
You can use this software according to the terms and conditions of the Mulan PSL v1.
You may obtain a copy of Mulan PSL v1 at:
    http://license.coscl.org.cn/MulanPSL
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
PURPOSE.
See the Mulan PSL v1 for more details.
"""

from flask import Blueprint, render_template

from config.config import page_size
from config.db import run_select

app_posts = Blueprint('app_posts', __name__)


# 分页
@app_posts.route("/")
def index():
    posts_list = posts_by_num(1)
    return render_template('posts/list.html', posts_list=posts_list)


@app_posts.route("/<int:page_num>")
def pages_page(page_num):
    posts_list = posts_by_num(page_num)
    return render_template('posts/list.html', posts_list=posts_list)


# 查询
def posts_by_num(page_num):
    limit_begin = (page_num - 1) * page_size

    return run_select('''
select *
from app_posts
where post_status = '1'
order by create_time desc 
limit %d,%d
    ''' % (limit_begin, page_size))

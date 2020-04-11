# FofaSpider
fofa爬虫，支持高级查询语句批量获取域名和ip
### 依赖安装
pip install -r requirements.txt
### 使用方法
python3 Spider.py -c '你的fofaCookie' -q 'domain="baidu.com"||title="百度"' -p 需要爬取的页数默认为5
ps：普通用户高级语法查询只支持第一页，非高级语法搜索支持前5页，上面的例子是高级语法查询

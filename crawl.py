# coding:utf-8

import requests
import json
from xlwt import Workbook

book = Workbook()
sheet1 = book.add_sheet("全国院校")

for page in range(1, 100):
    url = "https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=jsonp&page={}&size=30".format(page)
    response = requests.get(url)
    response.encoding = 'utf-8'
    content = json.loads(response.text[5:-2])
    school_list = content["school"]
    for index, school in enumerate(school_list):
        schoolid = school["schoolid"]
        schoolname = school["schoolname"]
        clicks = school["clicks"]
        monthclicks = school["monthclicks"]
        weekclicks = school["weekclicks"]
        province = school["province"]
        schooltype = school["schooltype"]
        schoolproperty = school["schoolproperty"]
        edudirectly = school["edudirectly"]
        f985 = school["f985"]
        f211 = school["f211"]
        level = school["level"]
        autonomyrs = school["autonomyrs"]
        library = school["library"]
        membership = school["membership"]
        schoolnature = school["schoolnature"]
        shoufei = school["shoufei"]
        jianjie = school["jianjie"]
        schoolcode = school["schoolcode"]
        ranking = school["ranking"]
        rankingCollegetype = school["rankingCollegetype"]
        guanwang = school["guanwang"]
        oldname = school["oldname"]
        ads = school["ads"]
        center = school["center"]
        master = school["master"]
        num = school["num"]
        firstrate = school["firstrate"]
        firstrateclass = school["firstrateclass"]

        result = (
            schoolid, schoolname, clicks, monthclicks, weekclicks, province, schooltype, schoolproperty, edudirectly,
            f985, f211, level, autonomyrs, library, membership, schoolnature, shoufei, jianjie, schoolcode, ranking,
            rankingCollegetype, guanwang, oldname, ads, center, master, num, firstrate, firstrateclass)
        print(result)
        for i, j in enumerate(result):
            if i == 0:
                sheet1.write(30 * page - 30 + index, i, 30 * page - 30 + index)
            sheet1.write(30 * page - 30 + index, i + 1, j)

        book.save('院校库.xls')

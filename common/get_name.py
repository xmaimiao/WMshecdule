import time
import re
from common.do_config import config
class GetName:
    def __init__(self):
        now_time = time.strftime('%Y-%m-%d')
        name = now_time  + '澳科大-日程测试1'
        if now_time not in config.get('api','oaname'):
            config.set('api','oaname',name)

    def replace_name(self,prename):
        before_code = re.match('^.*?(\d+)$', config.get('api', 'oaname')).group(1)
        # print("提取出來的測試編號：{}".format(before_code))
        keywords= re.search('(.*[\u4e00-\u9fa5]+)',config.get('api','oaname')).group(1)
        # print(提取出來的測試前綴：{}".format(keywords))
        name = keywords + str(int(before_code) + 1)
        config.set('api', 'oaname', name)

        if prename is not None:
            config.set('api','prename',name)

        return name

if __name__ == '__main__':
    user =GetName()
    print(user.replace_name('按日循环（每X天，开始-结束日期）'))
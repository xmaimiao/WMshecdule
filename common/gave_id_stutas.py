from common.do_config import config
def gettype(title,data):
    if title == "獲取部門id":
        ids=getid(config.get('api','group'),data)
        try:
            config.set("api", "groupid", ids[0])
        except Exception as e:
            print("列表爲空，ids[0]溢出！")
            raise e


    elif title=="獲取hr通知部門id":
        ids=getid(config.get('api', 'hrgroups'), data)
        config.set("api", "hrgroupsid", ids)


    elif title=="獲取教師id":
        ids=getid(config.get('api', 'teachers'), data)
        try:
            config.set("api", "teacherid", ids[0])
            config.set("api","teacher",eval(config.get('api', 'teachers'))[0])
        except Exception as e:
            print("列表爲空，ids[0]溢出！")
            raise e

def getid(conf_data,data):
    ids = []
    for i in eval(conf_data):
        for j in data:
            if i == j['name']:
                id = j['id']
                ids.append(id)
    return ids


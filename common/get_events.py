from common.do_config import config
from common.context import Context
class GetEvents:
    def get_events(self,title,name,result,event):
        if event == "once":
            model = result['model']
            if model != []:
                data=model[0]
                events=data["events"]
            else:
                return False
        else:
            events = result["data"]
            print(events)

        if events != []:
            for i in events:
                print(i)
                print("name:{}".format(name))

                if i["title"] == name:
                    if title == "獲取事件id":
                        config.set("api",'eventid',i["id"])
                    print("要編輯的事件id是：{}".format(config.get("api",'eventid')))
                    return True
                else:
                    return False
        else:
            return False


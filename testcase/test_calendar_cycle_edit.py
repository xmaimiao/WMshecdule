import unittest
from ddt import ddt,data
from common.do_excel import Doexcel
from common.do_http import Dohttp
from common import contants
from common.context import replace,Context
from common.do_config import config
from common.get_name import GetName
from common.get_events import GetEvents
from common.setting import Setting
@ddt
class TestEdit(unittest.TestCase):
    unit = unittest.TestCase()
    do_excel = Doexcel(contants.case_dir, 'calendarcycle')
    cases = do_excel.read_excel()
    getname = GetName()
    getevents =GetEvents()
    setting=Setting()

    @classmethod
    def setUpClass(cls):
        cls.dohttp = Dohttp()

    @data(*cases)
    def test_edit(self,case):

        case.url = replace(case.url)
        if case.data:
            case.data = replace(case.data)
        if case.json is not None:
            self.getname.replace_name(case.prename)
            self.setting.get_time()
            case.json = replace(case.json)

        case.headers = replace(case.headers)
        resp =self.dohttp.dohttp(json=case.json,data=case.data,url=case.url,method=case.method,headers=case.headers)
        actual = resp.json()['success']
        print("傳入的json：{}".format(case.json))
        print("傳入的headers：{}".format(case.headers))
        print("傳入的url：{}".format(case.url))
        print("傳入的title：{}".format(case.title))

        if case.check_noexist is None:
            try:
                self.unit.assertEqual(case.expect,actual)
                self.do_excel.write_excel(case.id+1,actual,'PASS')
            except AssertionError as e:
                msg = resp.json()['errorMsg']
                print("報錯信息：{}".format(msg))
                self.do_excel.write_excel(case.id+1,actual,'FALSE')
                raise e

        if  case.data is not None:
            config.set('api','token',resp.json()['model']['accessToken'])

        if  case.check_exist is not None:
            if case.prename is not None:
                result = self.getevents.get_events(case.title, config.get("api","prename"),resp.json(),case.event)
            else:
                result = self.getevents.get_events(case.title, config.get("api", "oaname"), resp.json(),case.event)
            try:
                self.assertEqual(True,result)
                self.do_excel.write_excel(case.id + 1, result, 'PASS')
            except Exception as e:
                self.do_excel.write_excel(case.id + 1, result, 'FALSE')
                print("無法獲取事件id/事件存在，检查prename参数是否正确！")
                raise e

        if case.check_noexist is not None:
            result = self.getevents.get_events(case.title, config.get("api","prename"), resp.json(),case.event)
            try:
                self.assertEqual(False, result)
                self.do_excel.write_excel(case.id + 1, result, 'PASS')
            except Exception as e:
                self.do_excel.write_excel(case.id + 1, result, 'FALSE')
                print("事件不存在，检查prename参数是否正确！")
                raise e


    @classmethod
    def tearDownClass(cls):
        cls.dohttp.close()



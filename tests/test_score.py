from django.test import TestCase
from apps.client.models import ClientTest
import random


class SimpleTest(TestCase):
    # 测试函数执行前执行
    def setUp(self):
        print("======setUp======")

    def test_demo(self):
        # 新增客户端
        client_name = "客户端{}"
        for count in range(1, 10):
            response = self.client.post('/score/index/',
                                        {'name': client_name.format(count), 'score': random.randint(1, 10000000)})
            self.assertEqual(response.status_code, 200)
            json_data = response.json()
            print('json_response:{}'.format(json_data))
            self.assertEqual(json_data['status'], 200)
        # 查询客户端
        print(ClientTest.objects.all())
        response_new = self.client.get('/score/chart/'+'?name=客户端2&page=1')
        self.assertEqual(response_new.status_code, 200)
        json_data_new = response_new.json()
        print('新json_response:{}'.format(json_data_new))
        self.assertEqual(json_data_new['status'], 200)

    # 测试函数执行后执行
    def tearDown(self):
        print("======tearDown======")


"""
python manage.py test tests/
"""

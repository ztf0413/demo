from django.http import JsonResponse
from django.views import View


# Create your views here.
from apps.client.models import ClientTest


class IndexView(View):
    """
    客户端上传客户端号和分数
    """

    def post(self, request):
        name = request.POST.get("name", "")
        score = request.POST.get("score", "")
        if not name or not score:
            return JsonResponse({'status': 401, 'message': '客户端名称/分数不能为空', 'data': {}})
        client = ClientTest.objects.filter(name=name).first()
        # 校验客户端是否存在
        if client:
            client.score = score
            client.save(update_fields=['score'])
        else:
            ClientTest.objects.create(name=name, score=score)
        return JsonResponse({'status': 200, 'message': 'ok', 'data': {}})


class ChartsView(View):
    """
    客户端查询排行榜
    """

    def get(self, request):
        name = request.GET.get("name", "")
        page = request.GET.get("page", "0")
        page = int(page) if page.isdigit() else 1
        client = ClientTest.objects.filter(name=name).first()
        client_obj, result_list, data = {}, [], {}
        if client:
            obj_list = ClientTest.objects.order_by("score")
            rank = 0
            for obj in obj_list:
                rank += 1
                obj_json = {"rank": rank, "name": obj.name, "score": obj.score}
                result_list.append(obj_json)
                if obj.name == name and obj_json:
                    client_obj = obj_json
            # 分页
            if page:
                result_list = result_list[(page-1)*10: page*10]
            result_list.append(client_obj)
            data["result_list"] = result_list
        else:
            return JsonResponse({'status': 401, 'message': '客户端不存在', 'data': {}})
        return JsonResponse({'status': 200, 'message': '', 'data': data})

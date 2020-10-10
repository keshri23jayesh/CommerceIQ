from rest_framework.views import APIView
from django.http import JsonResponse

from json_app.json_app_config import JsonModifier
from utills.common_utill import query_set_to_dict

json_modifier_instance = JsonModifier()


class postCurdAPI(APIView):
    """
        Retrieve, update or delete a post instance.
    """
    response = {}

    def get(self, request, entity=None, pk=None):
        """

        :param request:
        :param pk:
        :return:
        """

        query_params = query_set_to_dict(request.query_params.copy())



        response = {}
        if entity is None:
            response["message"] = "Please Pass Some entity in Url. eg, http://127.0.0.1:8000/abc/"
            response['status'] = 410
        else:
            pk = int(pk) if pk is not None else pk
            if len(query_params):
                if '_sort' in query_params.keys():
                    response = json_modifier_instance.sort_entity(entity, query_params)
                elif 'q' in query_params.keys():
                    response = json_modifier_instance.search_basic_entity(entity, query_params)
                else:
                    response = json_modifier_instance.sort_entity(entity, query_params)
            else:
                response = json_modifier_instance.get_entity(entity, pk)

        if response['status']:
            status = 200
        else:
            status = 410
        return JsonResponse(response, status=status, safe=False)

    def post(self, request, entity):
        data = request.data
        result = json_modifier_instance.post_entity(data, entity)
        return JsonResponse(result, status=200, safe=False)

    def put(self, request, entity, pk=None):
        data = request.data
        pk = int(pk) if pk is not None else pk
        result = json_modifier_instance.put_or_patch_entity(pk, data, entity)
        return JsonResponse(result, status=200, safe=False)

    def patch(self, request, entity, pk=None):
        data = request.data
        pk = int(pk) if pk is not None else pk
        result = json_modifier_instance.put_or_patch_entity(pk, data, entity)
        return JsonResponse(result, status=200, safe=False)

    def delete(self, request, entity, pk=None):
        pk = int(pk) if pk is not None else pk
        result = json_modifier_instance.delete_entity(entity, pk)
        return JsonResponse(result, status=200, safe=False)

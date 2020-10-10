import json, os
from json_mock.settings import BASE_DIR
from utills.common_utill import check_key

file_path = os.path.join(BASE_DIR, 'json_app/store.json')


class JsonModifier:
    def __init__(self):
        pass

    """
        CRUD Operation for Posts
    """
    def sort_entity(self, entity, query_params):
        response = {}
        response['status'] = False
        with open(file_path) as json_file:
            data = json.load(json_file)

        if check_key(data, entity):
            rows = data[entity]
            response[entity] = []
            if len(rows):
                sort_value = query_params['_sort']
                for row in rows:
                    if sort_value in row.keys():
                        response[entity].append(row)
                if len(response[entity]):
                    sort_order = query_params['_order']
                    reverse = False if sort_order == 'asc' else True
                    response[entity] = sorted(response[entity], key = lambda i: i[sort_value], reverse=reverse)
            response['status'] = True
        else:
            response["message"] = "No Entity is present with Name " + entity
        return response

    def search_entity(self, entity, query_params):
        response = {}
        response['status'] = False
        with open(file_path) as json_file:
            data = json.load(json_file)

        query_params_len = len(query_params)
        if check_key(data, entity):
            rows = data[entity]
            response[entity] = []
            if len(rows):
                for row in rows:
                    param_mathced = 0
                    for key in query_params:
                        if key in row.keys() and query_params[key] == row[key]:
                            param_mathced+=1
                    if param_mathced == query_params_len:
                        response[entity].append(row)
            response['status'] = True
        else:
            response["message"] = "No Entity is present with Name " + entity
        return response

    def search_basic_entity(self, entity, query_params):
        response = {}
        response['status'] = False
        with open(file_path) as json_file:
            data = json.load(json_file)

        if check_key(data, entity):
            rows = data[entity]
            response[entity] = []
            if len(rows):
                for row in rows:
                    if query_params['q'] in row.keys():
                        response[entity].append(row)
            response['status'] = True
        else:
            response["message"] = "No Entity is present with Name " + entity
        return response

    def get_entity(self, entity, key=None):
        """

        :param key:
        :param entity:
        :return:
        """
        response = {}
        response['status'] = False

        with open(file_path) as json_file:
            data = json.load(json_file)
        if check_key(data, entity):
            rows = data[entity]
            response[entity] = []
            if key is not None and len(rows):
                for row in rows:
                    if row['id'] == key:
                        response[entity].append(row)
                        break
            else:
                response[entity] = rows
            response['status'] = True
            return response
        else:
            response["message"] = "No Entity is present with Name " + entity
        return response

    def post_entity(self, new_elemnt, entity):
        """

        :param key:
        :return:
        """
        response = {}
        response['status'] = True
        with open(file_path, 'r') as data_file:
            data = json.load(data_file)
        if check_key(data, entity):
            rows = data[entity]
            entity_id = new_elemnt['id']
            existing_entity = list(filter(lambda x: (x['id'] == entity_id), rows))
            if len(existing_entity) == 0:
                data[entity].append(new_elemnt)
                with open(file_path, 'w') as data_file:
                    json.dump(data, data_file)
                response["message"] = "SuccessFully Added new Post"
            else:
                response['status'] = False
                response["message"] = "Please Try with diffrent Key"
        else:
            data[entity] = []
            data[entity].append(new_elemnt)
            with open(file_path, 'w') as data_file:
                json.dump(data, data_file)
            response["message"] = "SuccessFully Added new Post"
        return response

    def put_or_patch_entity(self, key, patch_data, entity):
        """

        :param key:
        :param data:
        :return:
        """
        response = {}
        response['status'] = False
        with open(file_path, 'r') as data_file:
            data = json.load(data_file)
        if check_key(data, entity):
            is_updated = False
            if len(data[entity]):
                for row in data[entity]:
                    if row['id'] == key:
                        for key, value in patch_data.items():
                            row[key] = value
                        is_updated = True
                        break
            if is_updated:
                response["message"] = "Successfully Updated Post Data"
                response['status'] = True
                with open(file_path, 'w') as data_file:
                    json.dump(data, data_file)
            else:
                response["message"] = "No Value for this id."
        else:
            response["message"] = "No Entity with this Name "+ entity
        return response

    def delete_entity(self, entity, key):
        response = {}
        response['status'] = False
        with open(file_path, 'r') as data_file:
            data = json.load(data_file)
        if check_key(data, entity):
            is_deleted = False
            if len(data[entity]):
                for row in data[entity]:
                    if row['id'] == key:
                        data[entity].remove(row)
                        is_deleted = True
                        break
            if is_deleted:
                response["message"] = "Successfully Deleted Data"
                response['status'] = True
                with open(file_path, 'w') as data_file:
                    json.dump(data, data_file)
            else:
                response["message"] = "No Elements for this id."
        else:
            response["message"] = "No Elements for this Entity"
        return response

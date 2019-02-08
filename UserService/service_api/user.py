from flask import request, jsonify
from flask_restful import Resource
from UserService.service_api_handler import user_post_handler, user_get_handler, user_delete_handler,user_put_handler
from UserService.util.user_related_method import get_user_dict_response


class User(Resource):
    def post(self):
        request_data = request.get_json()
        result = user_post_handler.create_user(request_data)

        if result:
            print(result.UserName)
            return jsonify({"user:",get_user_dict_response(result)})
        else:
            return None

    def get(self, username=None):
        if username:
            user_object = user_get_handler.get_single_user(username)
            if user_object:
                return jsonify({"user": get_user_dict_response(user_object)})
            else:
                return {"success", False}
        else:
            user_objects = user_get_handler.get_all_user()
            user_object_dict = [get_user_dict_response(user_object for user_object in user_objects)]
            return jsonify({"user": user_object_dict})

    def delete(self, firstname):
        user_object = user_delete_handler.delete_user(firstname)
        if user_object:
            return jsonify({"user", user_object})
        else:
            return {"success", False}

    def put(self, firstname):
        user_object = user_get_handler.get_single_user(firstname)
        if user_object:
            request_data = request.get_json()
            update_user_object = user_put_handler.update_user(user_object, request_data)

        return jsonify({"user", get_user_dict_response(update_user_object)})

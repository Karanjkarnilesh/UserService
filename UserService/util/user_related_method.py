from UserService.db.user_model.models import USERS

def get_user_dict_response(user_object):
    response_dict = {
        "username" :user_object.UserName,
        "email" : user_object.Email,
        "phone" :user_object.Phone,
        "password" :user_object.Password,
    }
    return response_dict
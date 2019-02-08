from UserService.db.user_model.models import USERS


def get_single_user(firstname):
    try:
        user_object = USERS.objects.get(FirstName=firstname)
        return  user_object
    except Exception as e:
        print e
        return None

def get_all_user():
    user_object = USERS.objects.all()
    return user_object
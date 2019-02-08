from UserService.db.user_model.models import USERS


def delete_user(firstname):
    try:
        user_object = USERS.objects.filter(FirstName=firstname).first()
        user_object.delete()
        return user_object
    except Exception as e:
        print e
        return None
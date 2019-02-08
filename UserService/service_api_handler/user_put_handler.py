from UserSERVICE.db.user_model.models import USERS


def update_user(user_object,data):
    if "firstname" in data:
        user_object.FirstName = data['firstname']

    if "email" in data:
        user_object.Email = data['email']
    if "phone" in data:
        user_object.phone = data['phone']

    user_object.save()
    return user_object
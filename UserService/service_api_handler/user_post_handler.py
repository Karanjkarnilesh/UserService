from UserService.db.user_model.models import USERS


def create_user(request_data):
    UsrName = request_data['username']
    mail = request_data['email']
    phone = request_data['phone']
    password = request_data['password']
    print("before creating user data :",UsrName,mail,phone,password )
    try:
        user_object = USERS.objects.create(
                                           Email=mail,
                                           Phone=phone,
                                           Password=password)
        user_object.save()
        print("after inserting ::::: ", user_object)
        return user_object
    except Exception as e:
        print e
        return None
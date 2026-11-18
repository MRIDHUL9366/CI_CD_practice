def authentication(function):

    def wrapper(name, password):
        if name == 'admin' and password == '1234':
            return function(name, password)
        else:
            return "Authentication Failed"

    return wrapper




@authentication
def admin_page(name, password):
    return "Authentication Successful"



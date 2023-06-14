from .models import Test


def find_test(data):
    login = data.get('login')
    test_obj = Test.objects.get(login=login)
    return test_obj

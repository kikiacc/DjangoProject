from django.contrib.auth.models import User
class EmailBackend(object):
    def authenticate(self, request, **credentials):
        #获取邮箱的认证信息即邮箱账号实例
        email = credentials.get('email', credentials.get('username'))
        try:
            user = User.objects.get(email=email)
        except Exception as error:
            print(error)
        else:
            #检查用户密码
            if user.check_password(credentials["password"]):
                return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except Exception as e:
            print(e)
            return None
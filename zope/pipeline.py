__author__ = 'ads'
from social.exceptions import AuthException


def user_password(strategy, user, is_new=False, *args, **kwargs):
    if "email" in kwargs['backend'].redirect_uri:
        password = strategy.request_data()['password']
        if is_new:
            user.set_password(password)
            user.save()
        # elif password != :
            # # return {'user': None, 'social': None}
            #    raise AuthException(strategy.backend)

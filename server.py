from hashlib import md5
import tornado.ioloop
import tornado.web
from db_functions import login_exists, user_check, create_user


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class SignUpHandler(tornado.web.RequestHandler):
    def get(self, login, password):
        if login_exists(login):
            self.write('This login currently exists!')
        else:
            create_user(login, password)
            self.write('You have signed up!')


class SignInHandler(tornado.web.RequestHandler):
    def get(self, login, password):
        if login_exists(login):
            if user_check(login, password):
                self.write('You have signed in!')
            else:
                self.write('Wrong password!')
        else:
            self.write('This user does not exist!')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login/([a-zA-Z]+)/(.+)", SignInHandler),
        (r"/register/([a-zA-Z]+)/(.+)", SignUpHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
tornado-celery
==============

tornado-celery is a non-blocking Celery client for Tornado web framework


Hello, world
------------

Here is a simple "Hello, world" example web app for Tornado::

    import tornado.ioloop
    import tornado.web
    import tcelery
    from tornado.gen import coroutine
    from tasks import test
    
    
    class MainHandler(tornado.web.RequestHandler):
        @coroutine
        def get(self):
            result = yield tcelery.celery_task(test, "hello world")
            self.write("%s" % result )

    application = tornado.web.Application([
        (r"/", MainHandler),
    ])

    if __name__ == "__main__":
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()

Here is tasks.py::

    from celery import Celery
    import time 

    celery = Celery('tasks', backend='redis://localhost', broker='amqp://')


    @celery.task
    def test(strs):
        return strs


run 
---------------

start a worker:

    celery -A tasks worker --loglevel=info -n new

and start tornado server.    
# -*- coding: utf-8 -*-
"""
    torncelery
    ~~~~~~~~~~

    assign celery task to Future and get task result async.

"""


from tornado.concurrent import TracebackFuture
from tornado.ioloop import IOLoop

def async(task, *args, **kwargs):
    future = TracebackFuture()
    callback = kwargs.pop("callback", None)
    if callback:
        IOLoop.instance().add_future(future,
                                     lambda future: callback(future.result()))
    result = task.delay(*args, **kwargs)
    IOLoop.instance().add_callback(_on_result, result, future)
    return future

def _on_result(result, future):
    # if result is not ready, add callback function to next loop,
    if result.ready():
        future.set_result(result.result)
    else:
        IOLoop.instance().add_callback(_on_result, result, future)

from tornado.concurrent import TracebackFuture
from tornado.ioloop import IOLoop

def celery_task(task, *args, **kwargs):
    future = TracebackFuture()
    callback = kwargs.pop("callback", None)
    if callback:
        IOLoop.instance().add_future(future,
                                     lambda future: callback(future.result()))
    result = task.delay(*args, **kwargs)
    IOLoop.instance().add_callback(_on_result, result, future)
    return future

def _on_result(result, future):
    if result.ready():
        future.set_result(result.result)
    else:
        IOLoop.instance().add_callback(_on_result, result, future)

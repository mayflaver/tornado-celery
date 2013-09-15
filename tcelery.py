from tornado.concurrent import TracebackFuture
from tornado.ioloop import IOLoop

def celery_task(task, *args, **kwargs):
    future = TracebackFuture()
    callback = kwargs.pop("callback", None)
    if callback:
        IOLoop.instance().add_future(future,
                                     lambda future: callback(future.result()))
    result = task.delay(*args, **kwargs)
    IOLoop.instance().add_callback(self._on_result, result, futurn)
    return future

def _on_result(self, result, future):
    if result.ready():
        future.set_result(result.result)
    else:
        IOLoop.instance().add_callback(self._on_result, result, future)

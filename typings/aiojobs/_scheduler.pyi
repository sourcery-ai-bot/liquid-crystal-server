"""
This type stub file was generated by pyright.
"""

class Scheduler(bases):
    def __init__(self, *, close_timeout, limit, pending_limit, exception_handler, loop):
        ...
    
    def __iter__(self):
        ...
    
    def __len__(self):
        ...
    
    def __contains__(self, job):
        ...
    
    def __repr__(self):
        ...
    
    @property
    def limit(self):
        ...
    
    @property
    def pending_limit(self):
        ...
    
    @property
    def close_timeout(self):
        ...
    
    @property
    def active_count(self):
        ...
    
    @property
    def pending_count(self):
        ...
    
    @property
    def closed(self):
        ...
    
    async def spawn(self, coro):
        ...
    
    async def close(self):
        ...
    
    def call_exception_handler(self, context):
        ...
    
    @property
    def exception_handler(self):
        ...
    
    def _done(self, job):
        ...
    
    async def _wait_failed(self):
        ...
    



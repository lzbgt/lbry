import logging

__version__ = "0.9.2rc3"
version = tuple(__version__.split('.'))

logging.getLogger(__name__).addHandler(logging.NullHandler())

# Python 2 and 3 compatibility packages
from six import with_metaclass

# base class for abstract inheritance
from abc import ABCMeta

class BaseConfig(with_metaclass(ABCMeta)):
    pass

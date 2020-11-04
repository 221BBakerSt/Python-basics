__all__ = ["second"] # in order to be called, __all__ must include that module file,
from . import second # and import that module in this __init__ file
# from . import first # this won't work because first is excluded in __all__

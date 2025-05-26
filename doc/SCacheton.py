class SCacheton:
    cachetons = {}
    cachevars = {}

    @staticmethod
    def get(cls, *args, **kwargs):

        cls_multitons = SCacheton.cachetons.get(cls, None)
        if cls_multitons is None:
            cls_multitons = SCacheton.cachetons[cls] = {}

        key = (args, tuple(kwargs.items()) )

        data = cls_multitons.get(key, None)
        if data is None:
            data = cls_multitons[key] = cls(*args, **kwargs)

        return data

    @staticmethod
    def set_var(key, value):

        SCacheton.cachevars[key] = value

    @staticmethod
    def get_var(key):

        return SCacheton.cachevars.get(key, None)

    @staticmethod
    def cleanup():

        SCacheton.cachetons = {}
        SCacheton.cachevars = {}
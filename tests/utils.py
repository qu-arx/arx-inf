# Just to be able to test it like the real result objects
# used in: test_format_meta.py :: MetaTestSuite
# via: https://stackoverflow.com/a/14620633/2668831
class AttrDict(dict):
    """
    Helper class for faking an API paper metadata object.
    """
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

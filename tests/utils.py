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

test_metadata = AttrDict(dict(
    authors = ["Arthur Welt", "Foo B. Baz", "Homer J. Simpson"],
    title = "Testing",
    arxiv_primary_category = {'term': "CS.AI"},
    arxiv_url = "http://arxiv.org/abs/2001.12345v1",
    published_parsed = AttrDict(dict(tm_year = 2020)),
))

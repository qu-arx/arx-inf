from arxiv import query as q
from .format_meta import FormatMeta

def QueryID(arx_id: str, to) -> str:
    """
    Query the arXiv API for a given ID, returning a formatted string
    representation of the author(s), title, category, and URL.
    """
    p = q(id_list=[arx_id])
    assert len(p) > 0
    f = FormatMeta(p[0], to)
    return f

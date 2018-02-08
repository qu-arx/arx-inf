from .format_unicode import YearConvert

def FormatAuth(auth: list) -> str:
    """
    Format the list of authors into surname-only, using et al.
    if applicable.
    """
    assert len(auth) > 0
    auth = [x.split(' ')[-1] for x in auth]
    if len(auth) > 2:
        f_auth = f"{auth[0]} et al."
    else:
        f_auth = ' & '.join(auth)
    return f_auth

# NOTE: 07/02/18: removed ``p: dict`` type for testing with AttrDict class
def FormatMeta(p) -> str:
    """
    Format the metadata for a given paper, from the Dict
    returned from the arxiv API module.
    """
    auth = FormatAuth(p.authors)
    t = p.title
    cat = p.arxiv_primary_category['term']
    u = p.arxiv_url
    arx_id = u.split('/abs/')[1]
    y = YearConvert(p.published_parsed.tm_year)
    f_meta = f"{auth} ({y}) {t} (arX⠶{arx_id}［{cat}］) {u}"
    return f_meta

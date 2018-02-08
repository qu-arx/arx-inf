from .format_unicode import YearConvert

def FormatAuth(auth: list, style: str="summary") -> str:
    """
    Format the list of authors:
    
    - when ``style`` is set to [default] ``summary``, give a
      surname-only citation, using et al. for 3 or more names
    - when ``style`` is set to ``filename``, simply coerce the
      first author's surname to lower case
    """
    assert len(auth) > 0
    if style == "summary":
        auth = [x.split(' ')[-1] for x in auth]
        if len(auth) > 2:
            f_auth = f"{auth[0]} et al."
        else:
            f_auth = ' & '.join(auth)
    elif style == "filename":
        f_auth = auth[0].split(' ')[-1].lower()
    else:
        raise ValueError(f"Style '{style}' not recognised.")
    return f_auth

# NOTE: 07/02/18: removed ``p: dict`` type for testing with AttrDict class
def FormatMeta(p, to: str="tw") -> str:
    """
    Format the metadata for a given paper, from the Dict
    returned from the arxiv API module.

    The ``to`` parameter sets the output format, with default ``tw`` for
    tweet format, and ``log`` for [naiveoculus] log format.
    """
    if to in ['tw']:
        # May add more scholarly use cases for this style in future
        authstyle = "summary"
    elif to in ['log']:
        authstyle = "filename"
    else:
        raise ValueError(f"Format '{to}' not recognised.")
    auth = FormatAuth(p.authors, style=authstyle)
    t = p.title
    cat = p.arxiv_primary_category['term']
    u = p.arxiv_url
    arx_id = u.split('/abs/')[1]
    y = YearConvert(p.published_parsed.tm_year, to=to)
    if to == "tw":
        f_meta = f"{auth} ({y}) {t} (arX⠶{arx_id}［{cat}］) {u}"
    elif to == "log":
        f_meta = f"- [ ] {auth}{y} ⠶ [{t}]({u})"
    else:
        raise ValueError(f"Format '{to}' not recognised.")
    return f_meta

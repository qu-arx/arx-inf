# arx-inf

Obtaining human-readable, bot-tweetable representations of arXiv metadata from the arXiv API.

- Python 3
- uses [arxiv.py](https://pypi.python.org/pypi/arxiv) by Lukas Schwab
  - TODO: maybe work with [pyArXiv](https://github.com/devArtoria/pyArXiv)
- to execute the test suite run `python -m unittest`

## Simple example

- Non-interactive use:

  ```sh
  python -c "from arx_inf.inf import QueryID; p = QueryID('1705.03239'); print(p)" | xclip -sel clip
  ```

  copies `Papyan et al. (⑰) Convolutional Dictionary Learning via Local Processing (arX⠶1705.03239v1［cs.CV］) http://arxiv.org/abs/1705.03239v1` to the clipboard

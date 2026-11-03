# helpdesk-knowledge-gap-finder

Compare ticket categories against KB topics and surface the uncovered ones, most frequent first, so the next article written is the one users need most.

## How to run

```sh
python3 main.py tickets.csv kb-topics.txt
```

## Example output

```
VPN: 14 ticket(s), no KB article
1 knowledge gap(s).
```

Standard library only. Run the tests with `python3 -m unittest discover`.

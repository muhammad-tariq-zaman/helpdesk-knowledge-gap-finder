"""Find ticket categories with no knowledge-base article.

Usage: python3 main.py tickets.csv kb-topics.txt
tickets.csv columns: ticket,category. kb-topics.txt holds one KB
article topic per line. Categories appearing in tickets but missing
from the KB are reported with their ticket counts, most frequent first.
"""
import argparse, csv, sys
from collections import Counter


def gaps(tickets, kb_topics):
    counts = Counter(t["category"].strip() for t in tickets)
    known = {t.strip() for t in kb_topics if t.strip()}
    return sorted(((c, n) for c, n in counts.items() if c not in known),
                  key=lambda kv: -kv[1])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tickets")
    parser.add_argument("kb_topics")
    args = parser.parse_args(argv)
    with open(args.tickets, newline="", encoding="utf-8") as f:
        tickets = list(csv.DictReader(f))
    with open(args.kb_topics, encoding="utf-8") as f:
        kb_topics = f.read().splitlines()
    found = gaps(tickets, kb_topics)
    for category, count in found:
        print(f"{category}: {count} ticket(s), no KB article")
    print(f"{len(found)} knowledge gap(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

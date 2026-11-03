import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import gaps


def t(c):
    return {"ticket": "T1", "category": c}


class TestKnowledgeGaps(unittest.TestCase):
    def test_covered_category_excluded(self):
        self.assertEqual(gaps([t("VPN")], ["VPN"]), [])

    def test_missing_category_counted(self):
        self.assertEqual(gaps([t("VPN"), t("VPN"), t("Printer")], ["Printer"]),
                         [("VPN", 2)])

    def test_most_frequent_first(self):
        result = gaps([t("A"), t("B"), t("B")], [])
        self.assertEqual(result[0], ("B", 2))

    def test_blank_kb_lines_ignored(self):
        self.assertEqual(gaps([t("VPN")], ["", "  "]), [("VPN", 1)])

import unittest
from tap_adyen.cleaners import clean_row


class TestCleaners(unittest.TestCase):
    def test_clean_row_with_missing_columns(self):
        row = {"existing_column": "1"}
        mappers = {
            "missing_column": {"type": int, "null": True},
            "existing_column": {"type": int, "null": True},
        }

        cleaned_row = clean_row(row, mappers)

        self.assertEqual(cleaned_row.get("existing_column"), 1)
        self.assertEqual(cleaned_row.get("missing_column"), None)


if __name__ == "__main__":
    unittest.main()

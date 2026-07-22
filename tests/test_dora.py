"""Tests specific to the DORA compliance module."""

from collections import Counter


class TestDORA:
    """Tests specific to DORA's intentional multi-entry-per-code structure."""

    def setup_method(self):
        """Load the DORA module once per test."""
        import ak_vendor.compliances.dora as dora_module

        self.data = dora_module.data
        self.DORA = dora_module.DORA
        self.DORA_DATA = dora_module.DORA_DATA

    # -- data list -----------------------------------------------------------

    def test_entry_count(self):
        """Catalog must have exactly 15 entries."""
        assert len(self.data) == 15

    def test_all_entries_have_non_empty_title(self):
        """Every entry must carry a non-empty title string."""
        for item in self.data:
            assert "title" in item, f"Entry {item['id']} missing 'title'"
            assert item["title"], f"Entry {item['id']} has empty 'title'"

    def test_id_format(self):
        """All ids must follow the 'dora_' prefix naming convention."""
        for item in self.data:
            assert item["id"].startswith("dora_"), (
                f"Entry id '{item['id']}' does not follow the 'dora_' prefix convention"
            )

    def test_codes_are_intentionally_non_unique(self):
        """DORA maps multiple sub-clauses to the same article; at least one
        code must appear more than once so a future collapse is caught."""
        codes = [item["code"] for item in self.data]
        duplicated = {c for c in codes if codes.count(c) > 1}
        assert duplicated, (
            "Expected DORA to have repeated article codes (multiple sub-clauses "
            "per article), but all codes are unique — verify the data was not "
            "accidentally collapsed."
        )

    def test_known_repeated_codes(self):
        """Pin the specific articles known to have multiple sub-clause entries."""
        counts = Counter(item["code"] for item in self.data)
        expected_repeated = {
            "Art. 9(2)": 3,
            "Art. 9(3)(b)-(c)": 3,
            "Art. 9(4)(d)": 2,
            "Art. 25(1)": 3,
        }
        for code, expected_count in expected_repeated.items():
            assert counts[code] == expected_count, (
                f"Expected {expected_count} entries for '{code}', "
                f"got {counts[code]}"
            )

    # -- DORA class ----------------------------------------------------------

    def test_class_attributes(self):
        """DORA instance exposes pk, id, code, and title with correct values."""
        entry = self.DORA(id="dora_9_3_a", code="Art. 9(3)(a)", title="Test title")
        assert entry.pk == "dora_9_3_a"
        assert entry.id == "dora_9_3_a"
        assert entry.code == "Art. 9(3)(a)"
        assert entry.title == "Test title"

    def test_str(self):
        """__str__ returns 'id - code - title'."""
        entry = self.DORA(id="dora_9_3_a", code="Art. 9(3)(a)", title="Test title")
        assert str(entry) == "dora_9_3_a - Art. 9(3)(a) - Test title"

    def test_repr(self):
        """__repr__ wraps __str__ in angle brackets."""
        entry = self.DORA(id="dora_9_3_a", code="Art. 9(3)(a)", title="Test title")
        assert repr(entry) == "<DORA: dora_9_3_a - Art. 9(3)(a) - Test title>"

    # -- DORA_DATA dict ------------------------------------------------------

    def test_dora_data_has_all_entries(self):
        """DORA_DATA must contain one key per data entry."""
        assert len(self.DORA_DATA) == len(self.data)

    def test_dora_data_keyed_by_id(self):
        """Every data id must be a key in DORA_DATA."""
        for item in self.data:
            assert item["id"] in self.DORA_DATA, (
                f"'{item['id']}' missing from DORA_DATA"
            )

    def test_dora_data_values_are_dora_instances(self):
        """All DORA_DATA values must be DORA instances with correct attributes."""
        for item in self.data:
            obj = self.DORA_DATA[item["id"]]
            assert isinstance(obj, self.DORA)
            assert obj.id == item["id"]
            assert obj.pk == item["id"]
            assert obj.code == item["code"]
            assert obj.title == item["title"]

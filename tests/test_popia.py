"""Tests specific to the POPIA compliance module."""

from collections import Counter


class TestPOPIA:
    """Tests for POPIA catalogue structure and helpers."""

    def setup_method(self):
        """Load the POPIA module once per test."""
        import ak_vendor.compliances.popia as popia_module

        self.data = popia_module.data
        self.POPIA = popia_module.POPIA
        self.POPIA_DATA = popia_module.POPIA_DATA

    def test_entry_count(self):
        """Catalog must have exactly 10 entries."""
        assert len(self.data) == 10

    def test_all_entries_have_non_empty_title(self):
        """Every entry must carry a non-empty title string."""
        for item in self.data:
            assert "title" in item, f"Entry {item['id']} missing 'title'"
            assert item["title"], f"Entry {item['id']} has empty 'title'"

    def test_id_format(self):
        """All ids must follow the 'popia_' prefix naming convention."""
        for item in self.data:
            assert item["id"].startswith("popia_"), (
                f"Entry id '{item['id']}' does not follow the "
                f"'popia_' prefix convention"
            )

    def test_codes_are_unique(self):
        """Each POPIA section maps to exactly one catalogue entry."""
        codes = [item["code"] for item in self.data]
        duplicated = {c for c in codes if codes.count(c) > 1}
        assert not duplicated, (
            f"Expected unique POPIA codes, found duplicates: {duplicated}"
        )

    def test_known_clause_ids(self):
        """Pin the expected section ids from the mapping document."""
        expected_ids = {
            "popia_19_1_a",
            "popia_19_1_b",
            "popia_19_2_b",
            "popia_19_2_d",
            "popia_19_3",
            "popia_6_1_b",
            "popia_10",
            "popia_11",
            "popia_12",
            "popia_18",
        }
        assert {item["id"] for item in self.data} == expected_ids

    def test_code_counts(self):
        """Every code appears exactly once."""
        counts = Counter(item["code"] for item in self.data)
        assert all(count == 1 for count in counts.values())

    def test_class_attributes(self):
        """POPIA instance exposes pk, id, code, and title with correct values."""
        entry = self.POPIA(
            id="popia_19_1_b",
            code="s 19(1)(b)",
            title="Test title",
        )
        assert entry.pk == "popia_19_1_b"
        assert entry.id == "popia_19_1_b"
        assert entry.code == "s 19(1)(b)"
        assert entry.title == "Test title"

    def test_str(self):
        """__str__ returns 'id - code - title'."""
        entry = self.POPIA(
            id="popia_19_1_b",
            code="s 19(1)(b)",
            title="Test title",
        )
        assert str(entry) == "popia_19_1_b - s 19(1)(b) - Test title"

    def test_repr(self):
        """__repr__ wraps __str__ in angle brackets."""
        entry = self.POPIA(
            id="popia_19_1_b",
            code="s 19(1)(b)",
            title="Test title",
        )
        assert (
            repr(entry) == "<POPIA: popia_19_1_b - s 19(1)(b) - Test title>"
        )

    def test_popia_data_has_all_entries(self):
        """POPIA_DATA must contain one key per data entry."""
        assert len(self.POPIA_DATA) == len(self.data)

    def test_popia_data_keyed_by_id(self):
        """Every data id must be a key in POPIA_DATA."""
        for item in self.data:
            assert item["id"] in self.POPIA_DATA, (
                f"'{item['id']}' missing from POPIA_DATA"
            )

    def test_popia_data_values_are_popia_instances(self):
        """All POPIA_DATA values must be POPIA instances with correct attributes."""
        for item in self.data:
            obj = self.POPIA_DATA[item["id"]]
            assert isinstance(obj, self.POPIA)
            assert obj.id == item["id"]
            assert obj.pk == item["id"]
            assert obj.code == item["code"]
            assert obj.title == item["title"]

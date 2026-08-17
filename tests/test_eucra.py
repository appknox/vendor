"""Tests specific to the EU CRA compliance module."""

from collections import Counter


class TestEUCRA:
    """Tests for EU CRA catalogue structure and helpers."""

    def setup_method(self):
        """Load the EUCRA module once per test."""
        import ak_vendor.compliances.eucra as eucra_module

        self.data = eucra_module.data
        self.EUCRA = eucra_module.EUCRA
        self.EUCRA_DATA = eucra_module.EUCRA_DATA

    # -- data list -----------------------------------------------------------

    def test_entry_count(self):
        """Catalog must have exactly 10 entries."""
        assert len(self.data) == 10

    def test_all_entries_have_non_empty_title(self):
        """Every entry must carry a non-empty title string."""
        for item in self.data:
            assert "title" in item, f"Entry {item['id']} missing 'title'"
            assert item["title"], f"Entry {item['id']} has empty 'title'"

    def test_id_format(self):
        """All ids must follow the 'cra_' prefix naming convention."""
        for item in self.data:
            assert item["id"].startswith("cra_"), (
                f"Entry id '{item['id']}' does not follow the 'cra_' prefix convention"
            )

    def test_codes_are_unique(self):
        """Each annex point maps to exactly one catalogue entry."""
        codes = [item["code"] for item in self.data]
        duplicated = {c for c in codes if codes.count(c) > 1}
        assert not duplicated, (
            f"Expected unique EU CRA codes, found duplicates: {duplicated}"
        )

    def test_known_clause_ids(self):
        """Pin the expected annex clause ids from the mapping document."""
        expected_ids = {
            "cra_i_2_a",
            "cra_i_2_b",
            "cra_i_2_d",
            "cra_i_2_e",
            "cra_i_2_f",
            "cra_i_2_g",
            "cra_i_2_h",
            "cra_i_2_j",
            "cra_i_2_k",
            "cra_ii_2",
        }
        assert {item["id"] for item in self.data} == expected_ids

    def test_code_counts(self):
        """Every code appears exactly once."""
        counts = Counter(item["code"] for item in self.data)
        assert all(count == 1 for count in counts.values())

    # -- EUCRA class ---------------------------------------------------------

    def test_class_attributes(self):
        """EUCRA instance exposes pk, id, code, and title with correct values."""
        entry = self.EUCRA(
            id="cra_i_2_d",
            code="Annex I, Part I, point (2)(d)",
            title="Test title",
        )
        assert entry.pk == "cra_i_2_d"
        assert entry.id == "cra_i_2_d"
        assert entry.code == "Annex I, Part I, point (2)(d)"
        assert entry.title == "Test title"

    def test_str(self):
        """__str__ returns 'id - code - title'."""
        entry = self.EUCRA(
            id="cra_i_2_d",
            code="Annex I, Part I, point (2)(d)",
            title="Test title",
        )
        assert str(entry) == "cra_i_2_d - Annex I, Part I, point (2)(d) - Test title"

    def test_repr(self):
        """__repr__ wraps __str__ in angle brackets."""
        entry = self.EUCRA(
            id="cra_i_2_d",
            code="Annex I, Part I, point (2)(d)",
            title="Test title",
        )
        assert (
            repr(entry)
            == "<EUCRA: cra_i_2_d - Annex I, Part I, point (2)(d) - Test title>"
        )

    # -- EUCRA_DATA dict -----------------------------------------------------

    def test_eucra_data_has_all_entries(self):
        """EUCRA_DATA must contain one key per data entry."""
        assert len(self.EUCRA_DATA) == len(self.data)

    def test_eucra_data_keyed_by_id(self):
        """Every data id must be a key in EUCRA_DATA."""
        for item in self.data:
            assert item["id"] in self.EUCRA_DATA, (
                f"'{item['id']}' missing from EUCRA_DATA"
            )

    def test_eucra_data_values_are_eucra_instances(self):
        """All EUCRA_DATA values must be EUCRA instances with correct attributes."""
        for item in self.data:
            obj = self.EUCRA_DATA[item["id"]]
            assert isinstance(obj, self.EUCRA)
            assert obj.id == item["id"]
            assert obj.pk == item["id"]
            assert obj.code == item["code"]
            assert obj.title == item["title"]

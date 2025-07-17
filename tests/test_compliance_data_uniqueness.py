"""
Tests to verify that ID and code values in compliance data are unique.
"""

import importlib
from pathlib import Path

import pytest


def get_compliance_modules():
    """Get all compliance modules from the compliances directory."""
    compliance_dir = Path(__file__).parent.parent / "ak_vendor" / "compliances"
    modules = []
    
    for file_path in compliance_dir.glob("*.py"):
        if file_path.name.startswith("__"):
            continue
            
        module_name = f"ak_vendor.compliances.{file_path.stem}"
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, 'data'):
                modules.append((file_path.stem, module))
        except ImportError:
            # Skip modules that can't be imported
            continue
    
    return modules


class TestComplianceUniqueness:
    """Test class for compliance data uniqueness."""
    
    @pytest.mark.parametrize("module_name,module", get_compliance_modules())
    def test_id_uniqueness(self, module_name, module):
        """Test that all IDs in the data list are unique."""
        data = module.data
        ids = [item['id'] for item in data]
        
        # Check for duplicates
        duplicates = []
        seen = set()
        for item_id in ids:
            if item_id in seen:
                duplicates.append(item_id)
            seen.add(item_id)
        
        assert not duplicates, (
            f"Duplicate IDs found in {module_name}: {duplicates}"
        )
        assert len(ids) == len(set(ids)), (
            f"ID uniqueness check failed for {module_name}"
        )
    
    @pytest.mark.parametrize("module_name,module", get_compliance_modules())
    def test_code_uniqueness(self, module_name, module):
        """Test that all codes in the data list are unique."""
        data = module.data
        codes = [item['code'] for item in data]
        
        # Check for duplicates
        duplicates = []
        seen = set()
        for code in codes:
            if code in seen:
                duplicates.append(code)
            seen.add(code)
        
        assert not duplicates, (
            f"Duplicate codes found in {module_name}: {duplicates}"
        )
        assert len(codes) == len(set(codes)), (
            f"Code uniqueness check failed for {module_name}"
        )
    
    @pytest.mark.parametrize("module_name,module", get_compliance_modules())
    def test_data_structure(self, module_name, module):
        """Test that each item in data has required fields."""
        data = module.data
        
        for i, item in enumerate(data):
            assert isinstance(item, dict), (
                f"Item {i} in {module_name} is not a dictionary"
            )
            assert 'id' in item, (
                f"Item {i} in {module_name} is missing 'id' field"
            )
            assert 'code' in item, (
                f"Item {i} in {module_name} is missing 'code' field"
            )
            assert item['id'], (
                f"Item {i} in {module_name} has empty 'id' field"
            )
            assert item['code'], (
                f"Item {i} in {module_name} has empty 'code' field"
            )
    
    def test_all_compliance_modules_have_data(self):
        """Test that all compliance modules have data attribute."""
        modules = get_compliance_modules()
        
        # Ensure we found some modules
        assert len(modules) > 0, "No compliance modules found"
        
        # Print information about found modules for debugging
        module_names = [name for name, _ in modules]
        print(f"Found {len(modules)} compliance modules: {module_names}")
        
        for module_name, module in modules:
            assert hasattr(module, 'data'), (
                f"Module {module_name} does not have 'data' attribute"
            )
            assert isinstance(module.data, list), (
                f"Module {module_name} data is not a list"
            )
            assert len(module.data) > 0, (
                f"Module {module_name} has empty data list"
            )


if __name__ == "__main__":
    # Allow running the test directly
    pytest.main([__file__, "-v"])

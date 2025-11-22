from vouchvault.tools import calculate_tax_compliance, fuzzy_match_vendor

def test_tax_mismatch_detection():
    """Test that the tool correctly flags wrong tax calculations."""
    # Invoice: Subtotal 1000, Tax 100 (Should be 180 at 18%)
    result = calculate_tax_compliance(subtotal=1000.0, tax_amount=100.0, tax_rate=0.18)
    
    assert result["is_compliant"] is False
    assert result["status"] == "MISMATCH"
    assert result["difference"] == 80.0

def test_fuzzy_match_typo():
    """Test if the fuzzy matcher catches slight misspellings."""
    invoice_vendor = "TechSolutions Inc"
    # Bank statement has a typo ("Solutons")
    bank_statement = "NEFT Transfer to TechSolutons Inc for Nov"
    
    match = fuzzy_match_vendor(invoice_vendor, bank_statement)
    
    # If you applied Upgrade #1 (difflib), this should be True!
    assert match["match_found"] is True

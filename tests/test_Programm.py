import src.Programm


def test_add_transaction():
    assert src.Programm.add_transaction("testing.txt","30/1/2025", "Checking", "Savings", "400", "Transfer") == "30/1/2025;Checking;Savings;400;Transfer;\n"


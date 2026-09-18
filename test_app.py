from app import calculate_bill

def test_patient_bill():
    assert calculate_bill(500, 200) == 700

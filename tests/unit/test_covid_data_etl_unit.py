from covid.covid_data_etl import validate_data


def test_validate_data():
    # Test when both 'Incident_Rate'
    # and 'Case_Fatality_Ratio' are empty strings
    record = {"Incident_Rate": "", "Case_Fatality_Ratio": ""}
    validate_data(record)
    assert record == {"Incident_Rate": 0.0, "Case_Fatality_Ratio": 0.0}

    # Test when only 'Incident_Rate' is an empty string
    record = {"Incident_Rate": "", "Case_Fatality_Ratio": 1.0}
    validate_data(record)
    assert record == {"Incident_Rate": 0.0, "Case_Fatality_Ratio": 1.0}

    # Test when only 'Case_Fatality_Ratio' is an empty string
    record = {"Incident_Rate": 1000, "Case_Fatality_Ratio": ""}
    validate_data(record)
    assert record == {"Incident_Rate": 1000, "Case_Fatality_Ratio": 0.0}

    # Test when neither 'Incident_Rate'
    # nor 'Case_Fatality_Ratio' is an empty string
    record = {"Incident_Rate": 1000, "Case_Fatality_Ratio": 1.0}
    validate_data(record)
    assert record == {"Incident_Rate": 1000, "Case_Fatality_Ratio": 1.0}

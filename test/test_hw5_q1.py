import hw5

def test_patient_init():
    # Creating patient an object of the class Patient
    patient = hw5.Patient("Roy", ["cough"])

    # Testing whether this patient has their name, symptoms list
    # and test_storage dictionary initiallized:
    assert patient.name == "Roy"
    assert patient.symptoms == ["cough"]
    assert patient.test_storage == {}

def test_add_test():
    # Creating patient an object of the class Patient
    patient = hw5.Patient("Pau", ["fever", "anosmia"])

    patient.add_test("covid", False)
    patient.add_test("flu", True)
    
    assert patient.test_storage["covid"] is False
    assert patient.test_storage["flu"] is True

# Splitting has_covid method into several subtests (for completeness)

def test_has_covid_baseline():
    # Create patient with no symptoms
    patient = hw5.Patient("John Doe", [])

    assert patient.has_covid() == 0.05

def test_has_covid_irrelevant_symptoms():
    # Create patient with no symptoms
    patient = hw5.Patient("Sick Jeff", ["headache", "stomachache", "runny nose", "fatigue"])

    # Asserting that these irrelevant symptoms do not have an effect on our return value
    # Which should be the same as the baseline value of 0.05 since none of the sympoms match
    assert patient.has_covid() == 0.05

def test_has_covid_symptoms_no_covid_test():
    # Create patient with symptoms but no covid test (in their test_storage dictionary)
    patient = hw5.Patient("Hannes", ["cough", "anosmia"])

    # We can even give this patient other added tests but no adding covid test:
    patient.add_test("flu", True)

    # Asserting that has_covid returns 0.05 + 0.1n for n the number of matches in
    # the patient's symptoms list
    assert patient.has_covid() == 0.25

def test_has_covid_duplicated_symptoms():
    # Creating patient with duplicated symptoms in their symptoms list
    patient = hw5.Patient("Dupe", ["cough", "cough", "cough", "cough", "anosmia"])

    # Asserting that this has no duplicated effect in our summation assignment
    assert patient.has_covid() == 0.25


def test_has_covid_true():
    # Testing when the patient does in fact have "covid" in their test_storage dictionary stored as True
    # Creating patient which has been tested positive for Covid:
    covid_patient = hw5.Patient("Bob", ["fever", "cough"])

    # Covid test true
    covid_patient.add_test("covid", True)

    # Asserting that this automatically returns 0.99
    assert covid_patient.has_covid() == 0.99

def test_has_covid_false():
    # Lastly testing when the patient does in fact have "covid" in their test_storage dictionary stored as False
    # Creating patient which has been tested negative for Covid:
    covid_patient = hw5.Patient("Bob", ["fever", "cough"])

    # Covid test false
    covid_patient.add_test("covid", False)

    # Asserting that this automatically returns 0.01
    assert covid_patient.has_covid() == 0.01

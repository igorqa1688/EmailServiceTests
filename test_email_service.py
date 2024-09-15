import pytest
from requests import send_email
from functions import generate_random_string


@pytest.mark.smoke
def test_send_email_nous() -> None:
    recipient = "igorqa@nous.dev"
    subject = generate_random_string(15)
    body = generate_random_string(150)

    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_google() -> None:
    recipient = "userpoker67@gmail.com"
    subject = generate_random_string(15)
    body = generate_random_string(150)

    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_subject_one_symbol() -> None:
    recipient = "userpoker67@gmail.com"
    subject = "s"
    body = generate_random_string(150)

    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_subject_two_dots() -> None:
    recipient = "komrad.legioferrata@yandex.ru"
    subject = "two dots"
    body = generate_random_string(150)

    response = send_email(recipient, subject, body)
    print(response)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_body_one_symbol() -> None:
    recipient = "userpoker67@gmail.com"
    subject = generate_random_string(15)
    body = "B"

    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_subject_with_cyrillic() -> None:
    recipient = "userpoker67@gmail.com"
    subject = generate_random_string(15)+"кириллица"
    body = generate_random_string(150)
    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_subject_with_emoji() -> None:
    recipient = "userpoker67@gmail.com"
    subject = generate_random_string(15)+"🤗"
    body = generate_random_string(150)
    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_body_with_cyrillic() -> None:
    recipient = "userpoker67@gmail.com"
    subject = generate_random_string(15)
    body = generate_random_string(15)+"кириллица"
    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_body_with_emoji() -> None:
    recipient = "userpoker67@gmail.com"
    subject = generate_random_string(15)
    body = "🚴" + generate_random_string(150)+ "😛" + generate_random_string(3) + "\n" + "⚡⚡"
    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_nous_in_upper_case() -> None:
    recipient = "igorqa@nous.dev"
    subject = generate_random_string(15)
    body = generate_random_string(150)

    response = send_email(recipient.upper(), subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_no_exist_email() -> None:
    recipient = "igorqa@no.devasd"
    subject = generate_random_string(15)
    body = generate_random_string(150)

    response = send_email(recipient.upper(), subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_body_only_space() -> None:
    recipient = "userpoker67@gmail.com"
    subject = generate_random_string(15)
    body = " "

    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_subject_only_space() -> None:
    recipient = "userpoker67@gmail.com"
    subject = " "
    body = "Body Test"

    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_space_before_and_after_recipient() -> None:
    recipient = " userpoker67@gmail.com "
    subject = "Subject test"
    body = "Body Test"

    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.smoke
def test_send_email_space_in_recipient() -> None:
    recipient = "user poker67@gmail.com"
    subject = "Subject test"
    body = "test_send_email_space_in_recipient"

    response = send_email(recipient, subject, body)
    assert response.success == True


@pytest.mark.negative
def test_send_without_recipient() -> None:
    recipient = ""
    subject = generate_random_string(15)
    body = generate_random_string(150)
    result = send_email(recipient.upper(), subject, body)
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Empty data"


@pytest.mark.negative
def test_send_without_subject() -> None:
    recipient = "igorqa@nous.dev"
    subject = ""
    body = generate_random_string(150)
    result = send_email(recipient, subject, body)
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Empty data"


@pytest.mark.negative
def test_send_without_body() -> None:
    recipient = "igorqa@nous.dev"
    subject = "test_subject"
    body = ""
    result = send_email(recipient, subject, body)
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Empty data"


@pytest.mark.negative
def test_send_email_only_recipient() -> None:
    recipient = "igorqa@nous.dev"
    subject = ""
    body = ""
    result = send_email(recipient, subject, body)
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Empty data"


@pytest.mark.negative
def test_send_email_only_subject() -> None:
    recipient = ""
    subject = "test subject"
    body = ""
    result = send_email(recipient, subject, body)
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Empty data"


@pytest.mark.negative
def test_send_email_only_body() -> None:
    recipient = ""
    subject = ""
    body = "test body"
    result = send_email(recipient, subject, body)
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Empty data"


@pytest.mark.negative
def test_send_without_all_data() -> None:
    recipient = ""
    subject = ""
    body = ""
    result = send_email(recipient, subject, body)
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Empty data"


@pytest.mark.negative
def test_send_email_without_symbol() -> None:
    recipient = "igorqanous.dev"
    subject = generate_random_string(15)
    body = generate_random_string(150)
    result = send_email(recipient, subject, body)
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Invalid email format"


@pytest.mark.negative
def test_send_email_recipient_contain_two_symbol() -> None:
    recipient = "ig@orqa@nous.dev"
    subject = generate_random_string(15)
    body = generate_random_string(150)
    result = send_email(recipient, subject, body)
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Invalid email format"


@pytest.mark.negative
def test_send_email_without_domen() -> None:
    recipient = "igorqa@nous"
    subject = generate_random_string(15)
    body = generate_random_string(150)
    result = send_email(recipient, subject, body)
    print("result "+str(result))
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Invalid email format"


@pytest.mark.negative
def test_send_email_without_name() -> None:
    recipient = "@nous.dev"
    subject = generate_random_string(15)
    body = generate_random_string(150)
    result = send_email(recipient, subject, body)
    print("result "+str(result))
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Invalid email format"
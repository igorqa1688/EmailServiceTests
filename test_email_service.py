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
def test_send_email_nous_in_upper_case() -> None:
    recipient = "igorqa@nous.dev"
    subject = generate_random_string(15)
    body = generate_random_string(150)

    response = send_email(recipient.upper(), subject, body)
    assert response.success == True


@pytest.mark.negative
def test_send_without_email() -> None:
    recipient = ""
    subject = generate_random_string(15)
    body = generate_random_string(150)
    result = send_email(recipient.upper(), subject, body)
    print(result)
    # Распаковка ответа
    status_code = result.code()
    grpc_details = result.details()
    assert status_code.value[0] == 3
    assert grpc_details == "Empty data"
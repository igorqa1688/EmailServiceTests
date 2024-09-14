import grpc
import EmailServiceGrpc_pb2
import EmailServiceGrpc_pb2_grpc
from global_vars import server


def send_email(recipient: str, subject: str, body: str) -> str:
    channel = grpc.insecure_channel(server)
    stub = EmailServiceGrpc_pb2_grpc.EmailServiceGrpcStub(channel)
    send_email_data = {
        "recipient": recipient,
        "subject": subject,
        "body": body
    }
    send_email_request = EmailServiceGrpc_pb2.SendEmailRequest(
        recipient=recipient,
        subject=subject,
        body=body
    )
    try:
        send_email_response = stub.SendEmail(request=send_email_request)
        return send_email_response
    except Exception as e:
        return e


if __name__ == "__main__":
    recipient = "igorqa@nous.dev"
    subject = "test subject"
    body = "test body"
    send_email(recipient, subject, body)
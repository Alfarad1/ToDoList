from celery import Celery

celery_app = Celery(
    "worker",
    broker="amqp://guest:guest@localhost:5672//",  # RabbitMQ
    backend="rpc://",  # You can use Redis or another backend
)


@celery_app.task
def send_confirmation_email(email: str, username:str, token: str):
    # Normally you'd use a real email backend like SMTP
    confirmation_url = f"http://localhost:8000/confirm/{token}"
    subject = "Registration confirmation."
    body = f"""Hello, {username}!\nWelcome to ToDo app, please, 
    verify your e-mail by pressing this link:\n
    <a href="{confirmation_url}">"""
    print(f"Send email to {email} with link: {confirmation_url}")
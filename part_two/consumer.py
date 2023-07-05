import pika
import json
from models import Contacts

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def send(_id: str):
    contacts = Contacts.objects(pk=_id)
    [contact.update(send=True) for contact in contacts]


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    send(message['id'])
    print(f" [x] Done: {message['id']}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='email_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
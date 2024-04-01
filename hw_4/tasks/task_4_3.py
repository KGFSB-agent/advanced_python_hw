import multiprocessing
import time
import codecs
import logging
from os import path

logging.basicConfig(
    level=logging.DEBUG,
    filename=path.join("artifacts", "artifacts_4_3", "artifact_4_3.txt"), 
    format='%(asctime)s | %(message)s'
)

def process_a(input_pipe, output_queue):
    while True:
        msg = input_pipe.recv()
        logging.info(f"[Процесс A]: Получаем {msg} из [Главный процесс]")
        logging.info(f"[Процесс A]: Конвертируем {msg} и кладём в очередь")
        output_queue.put(msg.lower())

# Process B that receives messages from process A, encodes them using rot13 and sends them back to the main process
def process_b(input_queue, output_pipe):
    while True:
        # Get message from queue, wait for 5 seconds before getting the next message
        msg = input_queue.get()
        logging.info(f"[Процесс B]: Получаем {msg} из очереди и ждём 5 секунд")
        time.sleep(5)
        # Encode message using rot13
        encoded_msg = codecs.encode(msg, 'rot_13')
        # Send it back to the main process
        logging.info(f"[Процесс B]: Отправляем {encoded_msg} в [Главный процесс]")
        output_pipe.send(encoded_msg)

# Main process
def main():
    # Create a pipe for communication between main process and process A
    parent_conn, child_conn = multiprocessing.Pipe()
    # Create a queue for communication between process A and B
    queue = multiprocessing.Queue()

    # Start process A
    process_a_proc = multiprocessing.Process(target=process_a, args=(child_conn, queue))
    process_a_proc.start()

    # Start process B
    parent_conn_b, child_conn_b = multiprocessing.Pipe()
    process_b_proc = multiprocessing.Process(target=process_b, args=(queue, child_conn_b))
    process_b_proc.start()

    # Send messages to process A
    messages = ["Samolet", "Biotin", "MYSH", "Kanfeta"]
    for msg in messages:
        logging.info(f"[Главный процесс]: Отправляем {msg}")
        parent_conn.send(msg)
        # Receive the processed message from process B
        logging.info(f"[Главный процесс]: Получили {parent_conn_b.recv()}")

if __name__ == '__main__':
    main()

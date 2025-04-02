import codecs
import multiprocessing
import threading
import time
from datetime import datetime
from multiprocessing import Process, Queue


def process_a(queue_main_to_a, queue_a_to_b, end):
    buffer = []
    lock = threading.Lock()

    def read_from_main():
        while not end.is_set():
            message = queue_main_to_a.get()
            with lock:
                buffer.append(message)
                print(f"[{datetime.now()}][A] Received: {message}")

    reader_thread = threading.Thread(target=read_from_main, daemon=True)
    reader_thread.start()

    while not end.is_set():
        time.sleep(5)
        with lock:
            if buffer:
                msg = buffer.pop(0)
                processed_msg = msg.lower()
                print(f"[{datetime.now()}][A] Sent to B: {processed_msg}")
                queue_a_to_b.put(processed_msg)


def process_b(queue_a_to_b, queue_b_to_main, end):
    while not end.is_set():
        msg = queue_a_to_b.get()
        encoded_msg = codecs.encode(msg, 'rot_13')
        timestamp = datetime.now()
        print(f"[{timestamp}][B] Encoded: {msg} -> {encoded_msg}")
        queue_b_to_main.put(encoded_msg)


def main():
    queue_main_to_a = Queue()
    queue_a_to_b = Queue()
    queue_b_to_main = Queue()
    end = multiprocessing.Event()
    a = Process(target=process_a, args=(queue_main_to_a, queue_a_to_b, end))
    b = Process(target=process_b, args=(queue_a_to_b, queue_b_to_main, end))
    a.start()
    b.start()

    def input_reader():
        while not end.is_set():
            line = input()
            if line:
                queue_main_to_a.put(line)
                print(f"[{datetime.now()}][Main] Sent to A: {line}")
            else:
                end.set()
                break

    input_thread = threading.Thread(target=input_reader)
    input_thread.start()
    while not end.is_set():
        encoded_msg = queue_b_to_main.get()
        print(f"[{datetime.now()}][Main] Received from B: {encoded_msg}")
    a.join()
    b.join()


if __name__ == "__main__":
    main()

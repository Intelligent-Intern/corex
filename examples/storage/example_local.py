import time
import multiprocessing
from corex.config_loader import load_storage_backend, load_messaging_backend


def message_listener():
    """
    This subprocess connects to the messaging system and listens to storage events.
    """
    messenger = load_messaging_backend("corex_config_messenger.yaml")

    def on_message(topic: str, message: str):
        print(f"[MESSENGER] Topic: {topic} | Message: {message}")

    messenger.subscribe("storage.notifications", on_message)

    print("[Listener] Waiting for messages...")
    while True:
        time.sleep(1)  # Keep process alive


def main():
    """
    Main process:
    - Creates bucket
    - Adds storage PUT event -> messenger forwarder
    - Uploads a file
    """
    storage = load_storage_backend("corex_config_minio.yaml")
    messenger = load_messaging_backend("corex_config_messenger.yaml")

    if not storage.bucket_exists("test-bucket"):
        storage.create_bucket("test-bucket")

    def event_handler(event):
        """
        Storage event handler, triggered on file upload (PUT).
        """
        path = event.get("path", "<unknown>")
        messenger.send("storage.notifications", f"File uploaded: {path}")

    # Register event for 'put'
    storage.add_event_handler("put", event_handler)

    # Start listener subprocess
    listener = multiprocessing.Process(target=message_listener)
    listener.start()

    # Upload a file to trigger event
    test_file = "example.txt"
    remote_path = "incoming/example.txt"

    print("[Main] Uploading test file...")
    storage.save(test_file, remote_path)

    # Allow some time for the message to be processed
    time.sleep(5)

    print("[Main] Done. Terminating listener.")
    listener.terminate()
    listener.join()


if __name__ == "__main__":
    main()

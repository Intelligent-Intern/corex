from corex.config_loader import load_storage_backend, load_messaging_backend

def on_file_uploaded(event):
    # You get event metadata like path, user, timestamp etc.
    print("EVENT:", event)
    messenger.send("storage.notifications", f"New file uploaded: {event['path']}")

def main():
    # Load storage and messaging handlers
    storage = load_storage_backend("corex_config_minio.yaml")
    global messenger
    messenger = load_messaging_backend("corex_config_messenger.yaml")

    # Create bucket if not exists
    if not storage.bucket_exists("my-bucket"):
        storage.create_bucket("my-bucket")
        print("Bucket created.")

    # Register event handler for PUT (upload)
    storage.add_event_handler(event_type="put", handler=on_file_uploaded)

    # Upload a file to trigger the event
    local_file = "example.txt"
    remote_path = "incoming/example.txt"
    storage.save(local_file, remote_path)

if __name__ == "__main__":
    main()

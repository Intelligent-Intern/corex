from abc import ABC, abstractmethod
from typing import List, Callable, Any

class StorageInterface(ABC):
    """
    A unified storage interface that covers both local file operations and bucket-based
    operations typical of S3-compatible systems. In a local file system, buckets can be 
    simulated as subdirectories and file events can be emulated via a filewatcher mechanism.
    """

    # Basic file operations
    @abstractmethod
    def save(self, source: str, destination: str) -> None:
        """
        Save a file from the source location to the destination in the storage system.

        :param source: Local file path of the file to save.
        :param destination: Target path in the storage system (can be within a bucket/subfolder).
        """
        raise NotImplementedError("The save method must be implemented by subclasses.")

    @abstractmethod
    def read(self, file_path: str) -> bytes:
        """
        Read and return the contents of a file from the storage system.

        :param file_path: The path to the file to read.
        :return: The file content as bytes.
        """
        raise NotImplementedError("The read method must be implemented by subclasses.")

    @abstractmethod
    def delete(self, file_path: str) -> None:
        """
        Delete a file at the specified path.

        :param file_path: The path to the file to delete.
        """
        raise NotImplementedError("The delete method must be implemented by subclasses.")

    @abstractmethod
    def list_files(self, directory: str) -> List[str]:
        """
        List all files in the given directory.

        :param directory: Directory path in the storage system.
        :return: A list of file paths.
        """
        raise NotImplementedError("The list_files method must be implemented by subclasses.")

    @abstractmethod
    def search(self, directory: str, pattern: str, recursive: bool = True) -> List[str]:
        """
        Search for files matching the given pattern in a directory.

        :param directory: Directory path in the storage system.
        :param pattern: Search pattern (could be a substring or regex).
        :param recursive: Whether to search recursively.
        :return: A list of matching file paths.
        """
        raise NotImplementedError("The search method must be implemented by subclasses.")

    # Bucket operations

    @abstractmethod
    def create_bucket(self, bucket_name: str) -> None:
        """
        Create a new bucket. For local storage, this can be implemented as creating a subfolder.

        :param bucket_name: Name of the bucket to create.
        """
        raise NotImplementedError("The create_bucket method must be implemented by subclasses.")

    @abstractmethod
    def delete_bucket(self, bucket_name: str) -> None:
        """
        Delete an existing bucket. For local storage, this can be implemented as deleting a subfolder.

        :param bucket_name: Name of the bucket to delete.
        """
        raise NotImplementedError("The delete_bucket method must be implemented by subclasses.")

    @abstractmethod
    def list_buckets(self) -> List[str]:
        """
        List all buckets available in the storage system.

        :return: A list of bucket names.
        """
        raise NotImplementedError("The list_buckets method must be implemented by subclasses.")

    # Event and filewatcher operations

    @abstractmethod
    def add_event_listener(self, path: str, event: str, callback: Callable[[str, str], Any]) -> None:
        """
        Add an event listener to a bucket or directory. In a local implementation, this can be
        achieved using a filewatcher to simulate S3-like events (e.g., file creation, deletion, or modification).

        :param path: The bucket or directory path to monitor.
        :param event: The event type (e.g., 'create', 'delete', 'modify').
        :param callback: A callable to be invoked with the event type and file path.
        """
        raise NotImplementedError("The add_event_listener method must be implemented by subclasses.")

    @abstractmethod
    def remove_event_listener(self, path: str, event: str, callback: Callable[[str, str], Any]) -> None:
        """
        Remove a previously added event listener from a bucket or directory.

        :param path: The bucket or directory path.
        :param event: The event type.
        :param callback: The callback that was registered.
        """
        raise NotImplementedError("The remove_event_listener method must be implemented by subclasses.")

    @abstractmethod
    def watch(self, path: str) -> None:
        """
        Start watching a bucket or directory for file system events. This method should
        integrate with a filewatcher mechanism to simulate event notifications for operations 
        like save, delete, or modifications.

        :param path: The bucket or directory path to watch.
        """
        raise NotImplementedError("The watch method must be implemented by subclasses.")

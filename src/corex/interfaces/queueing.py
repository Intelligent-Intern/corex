from abc import ABC, abstractmethod
from typing import Any, List, Optional

class QueueingInterface(ABC):
    """
    CoreX Interface for Queueing.
    
    This interface provides a standardized API for message queueing operations, 
    including enqueueing, dequeueing, and management of queues. Implementations 
    can support various queueing systems (e.g., RabbitMQ, AWS SQS, Kafka, etc.).
    """

    @abstractmethod
    def enqueue(self, queue_name: str, message: Any) -> None:
        """
        Add a message to the specified queue.
        
        :param queue_name: The name of the queue.
        :param message: The message to enqueue.
        """
        raise NotImplementedError("enqueue must be implemented by subclasses.")

    @abstractmethod
    def dequeue(self, queue_name: str, timeout: Optional[int] = None) -> Optional[Any]:
        """
        Retrieve and remove a message from the specified queue.
        
        :param queue_name: The name of the queue.
        :param timeout: Maximum time in seconds to wait for a message (if applicable).
        :return: The dequeued message, or None if no message is available.
        """
        raise NotImplementedError("dequeue must be implemented by subclasses.")

    @abstractmethod
    def create_queue(self, queue_name: str) -> None:
        """
        Create a new queue with the specified name.
        
        :param queue_name: The name of the queue to create.
        """
        raise NotImplementedError("create_queue must be implemented by subclasses.")

    @abstractmethod
    def delete_queue(self, queue_name: str) -> None:
        """
        Delete the specified queue.
        
        :param queue_name: The name of the queue to delete.
        """
        raise NotImplementedError("delete_queue must be implemented by subclasses.")

    @abstractmethod
    def list_queues(self) -> List[str]:
        """
        List all queues available in the system.
        
        :return: A list of queue names.
        """
        raise NotImplementedError("list_queues must be implemented by subclasses.")

    @abstractmethod
    def acknowledge(self, queue_name: str, message_id: str) -> None:
        """
        Acknowledge that a message has been processed.
        
        :param queue_name: The name of the queue.
        :param message_id: The identifier of the message to acknowledge.
        """
        raise NotImplementedError("acknowledge must be implemented by subclasses.")

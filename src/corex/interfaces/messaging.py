from abc import ABC, abstractmethod
from typing import Any, Callable, Optional, Dict, List

class MessagingInterface(ABC):
    """
    CoreX Interface for Messaging.

    This interface standardizes messaging operations such as connecting to a messaging system,
    sending and receiving messages, subscribing to channels, and acknowledging messages.
    Implementations may support various messaging systems (e.g., RabbitMQ, Kafka, ZeroMQ) and protocols.
    """

    @abstractmethod
    def connect(self, connection_params: Dict[str, Any]) -> None:
        """
        Establish a connection to the messaging system.

        :param connection_params: Dictionary of connection parameters (e.g., host, port, credentials).
        """
        raise NotImplementedError("connect must be implemented by subclasses.")

    @abstractmethod
    def disconnect(self) -> None:
        """
        Close the connection to the messaging system.
        """
        raise NotImplementedError("disconnect must be implemented by subclasses.")

    @abstractmethod
    def is_connected(self) -> bool:
        """
        Check if the connection to the messaging system is active.

        :return: True if connected, False otherwise.
        """
        raise NotImplementedError("is_connected must be implemented by subclasses.")

    @abstractmethod
    def reconnect(self) -> None:
        """
        Attempt to re-establish a lost connection to the messaging system.
        """
        raise NotImplementedError("reconnect must be implemented by subclasses.")

    @abstractmethod
    def send_message(self, destination: str, message: Any) -> None:
        """
        Send a message to the specified destination.

        :param destination: The destination channel, queue, or topic.
        :param message: The message to be sent.
        """
        raise NotImplementedError("send_message must be implemented by subclasses.")

    @abstractmethod
    def send_bulk_messages(self, destination: str, messages: List[Any]) -> None:
        """
        Send a list of messages to the specified destination in bulk.

        :param destination: The destination channel, queue, or topic.
        :param messages: A list of messages to be sent.
        """
        raise NotImplementedError("send_bulk_messages must be implemented by subclasses.")

    @abstractmethod
    def receive_message(self, source: str, timeout: Optional[int] = None) -> Optional[Any]:
        """
        Receive a message from the specified source.

        :param source: The source channel, queue, or topic.
        :param timeout: Optional timeout in seconds to wait for a message.
        :return: The received message, or None if no message is available within the timeout.
        """
        raise NotImplementedError("receive_message must be implemented by subclasses.")

    @abstractmethod
    def subscribe(self, channel: str, callback: Callable[[Any], None]) -> None:
        """
        Subscribe to a channel to receive messages asynchronously.

        :param channel: The channel (queue/topic) to subscribe to.
        :param callback: A callable that will be invoked with each received message.
        """
        raise NotImplementedError("subscribe must be implemented by subclasses.")

    @abstractmethod
    def unsubscribe(self, channel: str, callback: Callable[[Any], None]) -> None:
        """
        Unsubscribe the specified callback from a channel.

        :param channel: The channel (queue/topic) to unsubscribe from.
        :param callback: The callback that was previously registered.
        """
        raise NotImplementedError("unsubscribe must be implemented by subclasses.")

    @abstractmethod
    def ack_message(self, message_id: str) -> None:
        """
        Acknowledge that a message has been processed successfully.

        :param message_id: The identifier of the message to acknowledge.
        """
        raise NotImplementedError("ack_message must be implemented by subclasses.")

    @abstractmethod
    def nack_message(self, message_id: str, requeue: bool = True) -> None:
        """
        Negatively acknowledge a message, optionally requeueing it for later processing.

        :param message_id: The identifier of the message.
        :param requeue: If True, the message will be requeued; otherwise, it will be discarded.
        """
        raise NotImplementedError("nack_message must be implemented by subclasses.")

    @abstractmethod
    def start_transaction(self) -> None:
        """
        Start a transaction in the messaging system, if supported.
        """
        raise NotImplementedError("start_transaction must be implemented by subclasses.")

    @abstractmethod
    def commit_transaction(self) -> None:
        """
        Commit the current messaging transaction.
        """
        raise NotImplementedError("commit_transaction must be implemented by subclasses.")

    @abstractmethod
    def rollback_transaction(self) -> None:
        """
        Rollback the current messaging transaction.
        """
        raise NotImplementedError("rollback_transaction must be implemented by subclasses.")

    @abstractmethod
    def purge_queue(self, queue_name: str) -> None:
        """
        Remove all messages from the specified queue.

        :param queue_name: The name of the queue to purge.
        """
        raise NotImplementedError("purge_queue must be implemented by subclasses.")

    @abstractmethod
    def get_queue_length(self, queue_name: str) -> int:
        """
        Retrieve the number of messages currently in the specified queue.

        :param queue_name: The name of the queue.
        :return: The count of messages in the queue.
        """
        raise NotImplementedError("get_queue_length must be implemented by subclasses.")

    @abstractmethod
    def start_consumer(self, channel: str, callback: Callable[[Any], None], polling_interval: int = 1) -> None:
        """
        Start a consumer that continuously polls for messages on a channel.

        :param channel: The channel (queue/topic) to consume from.
        :param callback: A callable that will be invoked with each received message.
        :param polling_interval: Time in seconds between polling attempts.
        """
        raise NotImplementedError("start_consumer must be implemented by subclasses.")

    @abstractmethod
    def stop_consumer(self, channel: str) -> None:
        """
        Stop the consumer that is polling messages on the specified channel.

        :param channel: The channel (queue/topic) to stop consuming from.
        """
        raise NotImplementedError("stop_consumer must be implemented by subclasses.")

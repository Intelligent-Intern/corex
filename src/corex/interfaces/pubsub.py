from abc import ABC, abstractmethod
from typing import Any, Callable, List

class PubsubInterface(ABC):
    """
    CoreX Interface for Pub/Sub.

    This interface provides a standardized API for publish/subscribe operations,
    including topic management, message publishing, and subscription handling.
    Implementations can support various pub/sub systems (e.g., Google Pub/Sub, AWS SNS,
    Apache Kafka, etc.).
    """

    @abstractmethod
    def create_topic(self, topic_name: str) -> None:
        """
        Create a new topic.

        :param topic_name: The name of the topic to create.
        """
        raise NotImplementedError("create_topic must be implemented by subclasses.")

    @abstractmethod
    def delete_topic(self, topic_name: str) -> None:
        """
        Delete an existing topic.

        :param topic_name: The name of the topic to delete.
        """
        raise NotImplementedError("delete_topic must be implemented by subclasses.")

    @abstractmethod
    def list_topics(self) -> List[str]:
        """
        List all topics available in the pub/sub system.

        :return: A list of topic names.
        """
        raise NotImplementedError("list_topics must be implemented by subclasses.")

    @abstractmethod
    def publish(self, topic_name: str, message: Any) -> None:
        """
        Publish a message to the specified topic.

        :param topic_name: The name of the topic to publish to.
        :param message: The message to be published.
        """
        raise NotImplementedError("publish must be implemented by subclasses.")

    @abstractmethod
    def subscribe(self, topic_name: str, callback: Callable[[Any], None]) -> None:
        """
        Subscribe to a topic with a callback to handle incoming messages.

        :param topic_name: The name of the topic to subscribe to.
        :param callback: A callable that takes a message as its only argument.
        """
        raise NotImplementedError("subscribe must be implemented by subclasses.")

    @abstractmethod
    def unsubscribe(self, topic_name: str, callback: Callable[[Any], None]) -> None:
        """
        Unsubscribe the specified callback from a topic.

        :param topic_name: The name of the topic.
        :param callback: The callback that was previously registered.
        """
        raise NotImplementedError("unsubscribe must be implemented by subclasses.")

from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Optional

class EventsInterface(ABC):
    """
    CoreX Interface for Events.

    This interface standardizes event operations including initialization, publishing events,
    subscribing and unsubscribing to events, triggering events, and shutdown procedures.
    Implementations may support various event systems (e.g., in-process event emitters, Kafka, EventBridge)
    to enable event-driven architectures.
    """

    @abstractmethod
    def initialize_events(self, config: Dict[str, Any]) -> None:
        """
        Initialize the event system with the provided configuration.

        :param config: A dictionary containing configuration parameters.
        """
        raise NotImplementedError("initialize_events must be implemented by subclasses.")

    @abstractmethod
    def publish_event(self, event_name: str, payload: Any, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Publish an event with the given name, payload, and optional metadata.

        :param event_name: The name or type of the event.
        :param payload: The event data.
        :param metadata: Optional metadata associated with the event.
        """
        raise NotImplementedError("publish_event must be implemented by subclasses.")

    @abstractmethod
    def subscribe_event(self, event_name: str, callback: Callable[[str, Any], None]) -> None:
        """
        Subscribe to a specific event type with a callback function.

        :param event_name: The event name to subscribe to.
        :param callback: A callable that will be invoked when the event is published.
                         The callback should accept the event name and payload as parameters.
        """
        raise NotImplementedError("subscribe_event must be implemented by subclasses.")

    @abstractmethod
    def unsubscribe_event(self, event_name: str, callback: Callable[[str, Any], None]) -> None:
        """
        Unsubscribe a callback from a specific event type.

        :param event_name: The event name to unsubscribe from.
        :param callback: The callback to remove from the event subscription.
        """
        raise NotImplementedError("unsubscribe_event must be implemented by subclasses.")

    @abstractmethod
    def get_subscriptions(self) -> Dict[str, List[Callable[[str, Any], None]]]:
        """
        Retrieve the current subscriptions mapping.

        :return: A dictionary where keys are event names and values are lists of subscribed callbacks.
        """
        raise NotImplementedError("get_subscriptions must be implemented by subclasses.")

    @abstractmethod
    def trigger_event(self, event_name: str, payload: Any) -> None:
        """
        Trigger an event synchronously, invoking all subscribed callbacks immediately.

        :param event_name: The name of the event to trigger.
        :param payload: The event data to pass to the subscribers.
        """
        raise NotImplementedError("trigger_event must be implemented by subclasses.")

    @abstractmethod
    def shutdown_events(self) -> None:
        """
        Shutdown the event system and perform any necessary cleanup.
        """
        raise NotImplementedError("shutdown_events must be implemented by subclasses.")

    @abstractmethod
    def register_global_handler(self, handler: Callable[[str, Any], None]) -> None:
        """
        Register a global event handler that will receive all events regardless of event name.

        :param handler: A callable that accepts an event name and payload.
        """
        raise NotImplementedError("register_global_handler must be implemented by subclasses.")

    @abstractmethod
    def deregister_global_handler(self, handler: Callable[[str, Any], None]) -> None:
        """
        Deregister a previously registered global event handler.

        :param handler: The global handler to remove.
        """
        raise NotImplementedError("deregister_global_handler must be implemented by subclasses.")

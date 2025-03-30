from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Callable

class MonitoringInterface(ABC):
    """
    CoreX Interface for Monitoring.

    This interface standardizes monitoring operations including recording metrics, tracking events,
    querying monitoring data, and issuing alerts. Implementations can support various monitoring systems
    (e.g., Prometheus, Datadog, New Relic) to provide insights into application performance and system health.
    """

    @abstractmethod
    def record_metric(self, metric_name: str, value: float, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Record a metric with a specified value and optional labels.

        :param metric_name: Name of the metric.
        :param value: The value to record.
        :param labels: Optional dictionary of labels or tags associated with the metric.
        """
        raise NotImplementedError("record_metric must be implemented by subclasses.")

    @abstractmethod
    def increment_metric(self, metric_name: str, increment: float = 1.0, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Increment a counter metric by a specified amount.

        :param metric_name: Name of the metric.
        :param increment: The amount to increment (default is 1.0).
        :param labels: Optional dictionary of labels or tags.
        """
        raise NotImplementedError("increment_metric must be implemented by subclasses.")

    @abstractmethod
    def set_metric(self, metric_name: str, value: float, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Set the value of a metric.

        :param metric_name: Name of the metric.
        :param value: The value to set.
        :param labels: Optional dictionary of labels or tags.
        """
        raise NotImplementedError("set_metric must be implemented by subclasses.")

    @abstractmethod
    def record_event(self, event_name: str, properties: Optional[Dict[str, Any]] = None) -> None:
        """
        Record an event with optional properties.

        :param event_name: The name of the event.
        :param properties: Optional dictionary of properties or metadata for the event.
        """
        raise NotImplementedError("record_event must be implemented by subclasses.")

    @abstractmethod
    def query_metrics(self, query: str) -> Any:
        """
        Query the monitoring system for metrics data using a specific query language.

        :param query: The query string.
        :return: The result of the query execution.
        """
        raise NotImplementedError("query_metrics must be implemented by subclasses.")

    @abstractmethod
    def alert(self, alert_name: str, message: str, severity: str = "info") -> None:
        """
        Send an alert based on monitoring data or events.

        :param alert_name: The identifier for the alert.
        :param message: A descriptive message for the alert.
        :param severity: The severity level of the alert (e.g., 'info', 'warning', 'critical').
        """
        raise NotImplementedError("alert must be implemented by subclasses.")

    # Additional methods for enhanced monitoring functionality

    @abstractmethod
    def get_metric(self, metric_name: str, labels: Optional[Dict[str, str]] = None) -> Any:
        """
        Retrieve the current value of a specified metric.

        :param metric_name: Name of the metric.
        :param labels: Optional dictionary of labels to filter the metric.
        :return: The current value or state of the metric.
        """
        raise NotImplementedError("get_metric must be implemented by subclasses.")

    @abstractmethod
    def flush_metrics(self) -> None:
        """
        Flush any buffered metrics to the monitoring backend immediately.
        """
        raise NotImplementedError("flush_metrics must be implemented by subclasses.")

    @abstractmethod
    def health_check(self) -> bool:
        """
        Perform a health check of the monitoring system.

        :return: True if the monitoring system is healthy; otherwise, False.
        """
        raise NotImplementedError("health_check must be implemented by subclasses.")

    @abstractmethod
    def configure(self, configuration: Dict[str, Any]) -> None:
        """
        Configure the monitoring system with custom settings.

        :param configuration: A dictionary of configuration parameters.
        """
        raise NotImplementedError("configure must be implemented by subclasses.")

    @abstractmethod
    def set_alert_threshold(self, metric_name: str, threshold: float, severity: str = "warning") -> None:
        """
        Set an alert threshold for a specific metric.

        :param metric_name: Name of the metric.
        :param threshold: The threshold value for triggering an alert.
        :param severity: The severity level if the threshold is breached.
        """
        raise NotImplementedError("set_alert_threshold must be implemented by subclasses.")

    @abstractmethod
    def remove_alert_threshold(self, metric_name: str) -> None:
        """
        Remove an existing alert threshold for a specific metric.

        :param metric_name: Name of the metric.
        """
        raise NotImplementedError("remove_alert_threshold must be implemented by subclasses.")

    @abstractmethod
    def subscribe_to_event(self, event_name: str, callback: Callable[[Dict[str, Any]], None]) -> None:
        """
        Subscribe to a specific event and register a callback to be invoked when the event occurs.

        :param event_name: The name of the event.
        :param callback: A callable that receives event details as a dictionary.
        """
        raise NotImplementedError("subscribe_to_event must be implemented by subclasses.")

    @abstractmethod
    def unsubscribe_from_event(self, event_name: str, callback: Callable[[Dict[str, Any]], None]) -> None:
        """
        Unsubscribe the given callback from a specific event.

        :param event_name: The name of the event.
        :param callback: The callback to remove.
        """
        raise NotImplementedError("unsubscribe_from_event must be implemented by subclasses.")

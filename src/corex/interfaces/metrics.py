from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class MetricsInterface(ABC):
    """
    CoreX Interface for Metrics.

    This interface standardizes metrics operations including recording, incrementing,
    setting gauge values, observing histograms, flushing metrics, and querying metrics data.
    Implementations can support various metrics backends (e.g., Prometheus, Datadog, New Relic)
    to provide real-time insights into application performance.
    """

    @abstractmethod
    def record_metric(self, metric_name: str, value: float, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Record a metric with the specified value.

        :param metric_name: The name of the metric.
        :param value: The metric value to record.
        :param labels: Optional dictionary of labels or tags associated with the metric.
        """
        raise NotImplementedError("record_metric must be implemented by subclasses.")

    @abstractmethod
    def increment_metric(self, metric_name: str, increment: float = 1.0, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Increment a counter metric by a specified amount.

        :param metric_name: The name of the metric.
        :param increment: The amount to increment the metric (default is 1.0).
        :param labels: Optional dictionary of labels or tags.
        """
        raise NotImplementedError("increment_metric must be implemented by subclasses.")

    @abstractmethod
    def set_gauge(self, metric_name: str, value: float, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Set the value of a gauge metric.

        :param metric_name: The name of the metric.
        :param value: The gauge value to set.
        :param labels: Optional dictionary of labels or tags.
        """
        raise NotImplementedError("set_gauge must be implemented by subclasses.")

    @abstractmethod
    def observe_histogram(self, metric_name: str, value: float, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Record an observation for a histogram metric.

        :param metric_name: The name of the histogram metric.
        :param value: The observed value to record.
        :param labels: Optional dictionary of labels or tags.
        """
        raise NotImplementedError("observe_histogram must be implemented by subclasses.")

    @abstractmethod
    def get_metric(self, metric_name: str, labels: Optional[Dict[str, str]] = None) -> Any:
        """
        Retrieve the current value or state of a metric.

        :param metric_name: The name of the metric.
        :param labels: Optional dictionary of labels to filter the metric.
        :return: The current metric data.
        """
        raise NotImplementedError("get_metric must be implemented by subclasses.")

    @abstractmethod
    def flush_metrics(self) -> None:
        """
        Flush any buffered metrics data to the backend immediately.
        """
        raise NotImplementedError("flush_metrics must be implemented by subclasses.")

    @abstractmethod
    def configure(self, configuration: Dict[str, Any]) -> None:
        """
        Configure the metrics system with provided settings.

        :param configuration: A dictionary of configuration parameters.
        """
        raise NotImplementedError("configure must be implemented by subclasses.")

    @abstractmethod
    def query_metrics(self, query: str) -> Any:
        """
        Query metrics data using a query language or API.

        :param query: The query string.
        :return: The result of the metrics query.
        """
        raise NotImplementedError("query_metrics must be implemented by subclasses.")

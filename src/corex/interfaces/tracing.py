from abc import ABC, abstractmethod
from typing import Any, Optional, Dict, ContextManager, Callable

class TracingInterface(ABC):
    """
    CoreX Interface for Tracing.
    
    This interface provides a standardized API for distributed tracing,
    allowing implementation of trace and span management, annotation, and error recording.
    """

    @abstractmethod
    def start_trace(self, name: str, **kwargs) -> Any:
        """
        Start a new trace with the given name.
        
        :param name: The name of the trace.
        :param kwargs: Additional keyword arguments for trace initialization.
        :return: A trace context or object representing the started trace.
        """
        raise NotImplementedError("start_trace must be implemented by subclasses.")

    @abstractmethod
    def end_trace(self, trace: Any, **kwargs) -> None:
        """
        End an existing trace.
        
        :param trace: The trace object returned by start_trace.
        :param kwargs: Additional keyword arguments for trace finalization.
        """
        raise NotImplementedError("end_trace must be implemented by subclasses.")

    @abstractmethod
    def create_span(self, name: str, parent: Optional[Any] = None, **kwargs) -> Any:
        """
        Create a new span within an existing trace.
        
        :param name: The name of the span.
        :param parent: The parent trace or span context, if any.
        :param kwargs: Additional keyword arguments for span creation.
        :return: A span object representing the started span.
        """
        raise NotImplementedError("create_span must be implemented by subclasses.")

    @abstractmethod
    def end_span(self, span: Any, **kwargs) -> None:
        """
        End a previously started span.
        
        :param span: The span object returned by create_span.
        :param kwargs: Additional keyword arguments for span finalization.
        """
        raise NotImplementedError("end_span must be implemented by subclasses.")

    @abstractmethod
    def annotate(self, trace_or_span: Any, key: str, value: Any) -> None:
        """
        Add an annotation to a trace or span.
        
        :param trace_or_span: The trace or span object to annotate.
        :param key: The annotation key.
        :param value: The annotation value.
        """
        raise NotImplementedError("annotate must be implemented by subclasses.")

    @abstractmethod
    def record_error(self, trace_or_span: Any, error: Exception) -> None:
        """
        Record an error in a trace or span.
        
        :param trace_or_span: The trace or span object.
        :param error: The exception instance representing the error.
        """
        raise NotImplementedError("record_error must be implemented by subclasses.")

    @abstractmethod
    def trace_context(self, name: str, **kwargs) -> ContextManager:
        """
        Provide a context manager for automatic trace handling.
        
        Usage:
            with tracer.trace_context("my_trace") as trace:
                # perform operations under the trace context
                ...
        
        :param name: The name of the trace.
        :param kwargs: Additional keyword arguments for trace initialization.
        :return: A context manager that starts and ends a trace.
        """
        raise NotImplementedError("trace_context must be implemented by subclasses.")

    @abstractmethod
    def span_context(self, name: str, parent: Optional[Any] = None, **kwargs) -> ContextManager:
        """
        Provide a context manager for automatic span handling.
        
        Usage:
            with tracer.span_context("my_span", parent=trace) as span:
                # perform operations under the span context
                ...
        
        :param name: The name of the span.
        :param parent: The parent trace or span, if any.
        :param kwargs: Additional keyword arguments for span initialization.
        :return: A context manager that starts and ends a span.
        """
        raise NotImplementedError("span_context must be implemented by subclasses.")

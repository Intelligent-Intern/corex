from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Union, Callable, List, Iterator

class HttpInterface(ABC):
    """
    CoreX Interface for HTTP.

    This interface standardizes HTTP operations for sending requests and handling responses.
    Implementations can integrate with various HTTP client libraries (e.g., requests, httpx)
    to provide a consistent API for HTTP communications.
    """

    @abstractmethod
    def request(self, method: str, url: str, *,
                headers: Optional[Dict[str, str]] = None,
                params: Optional[Dict[str, Union[str, int]]] = None,
                data: Optional[Any] = None,
                json: Optional[Any] = None,
                timeout: Optional[int] = None) -> Any:
        """
        Send an HTTP request using the specified method.

        :param method: The HTTP method (e.g., 'GET', 'POST', etc.).
        :param url: The target URL.
        :param headers: Optional HTTP headers.
        :param params: Optional URL query parameters.
        :param data: Optional data for the request body.
        :param json: Optional JSON data for the request body.
        :param timeout: Optional timeout in seconds.
        :return: An HTTP response object.
        """
        raise NotImplementedError("request must be implemented by subclasses.")

    @abstractmethod
    def get(self, url: str, *,
            headers: Optional[Dict[str, str]] = None,
            params: Optional[Dict[str, Union[str, int]]] = None,
            timeout: Optional[int] = None) -> Any:
        """
        Send an HTTP GET request.
        """
        raise NotImplementedError("get must be implemented by subclasses.")

    @abstractmethod
    def post(self, url: str, *,
             headers: Optional[Dict[str, str]] = None,
             data: Optional[Any] = None,
             json: Optional[Any] = None,
             timeout: Optional[int] = None) -> Any:
        """
        Send an HTTP POST request.
        """
        raise NotImplementedError("post must be implemented by subclasses.")

    @abstractmethod
    def put(self, url: str, *,
            headers: Optional[Dict[str, str]] = None,
            data: Optional[Any] = None,
            json: Optional[Any] = None,
            timeout: Optional[int] = None) -> Any:
        """
        Send an HTTP PUT request.
        """
        raise NotImplementedError("put must be implemented by subclasses.")

    @abstractmethod
    def delete(self, url: str, *,
               headers: Optional[Dict[str, str]] = None,
               timeout: Optional[int] = None) -> Any:
        """
        Send an HTTP DELETE request.
        """
        raise NotImplementedError("delete must be implemented by subclasses.")

    @abstractmethod
    def patch(self, url: str, *,
              headers: Optional[Dict[str, str]] = None,
              data: Optional[Any] = None,
              json: Optional[Any] = None,
              timeout: Optional[int] = None) -> Any:
        """
        Send an HTTP PATCH request.
        """
        raise NotImplementedError("patch must be implemented by subclasses.")

    @abstractmethod
    def head(self, url: str, *,
             headers: Optional[Dict[str, str]] = None,
             timeout: Optional[int] = None) -> Any:
        """
        Send an HTTP HEAD request.
        """
        raise NotImplementedError("head must be implemented by subclasses.")

    @abstractmethod
    def options(self, url: str, *,
                headers: Optional[Dict[str, str]] = None,
                timeout: Optional[int] = None) -> Any:
        """
        Send an HTTP OPTIONS request.
        """
        raise NotImplementedError("options must be implemented by subclasses.")

    @abstractmethod
    def trace(self, url: str, *,
              headers: Optional[Dict[str, str]] = None,
              timeout: Optional[int] = None) -> Any:
        """
        Send an HTTP TRACE request.
        """
        raise NotImplementedError("trace must be implemented by subclasses.")

    @abstractmethod
    def download_file(self, url: str, destination_path: str, *,
                      headers: Optional[Dict[str, str]] = None,
                      timeout: Optional[int] = None) -> None:
        """
        Download a file from the specified URL to a local destination path.
        """
        raise NotImplementedError("download_file must be implemented by subclasses.")

    @abstractmethod
    def upload_file(self, url: str, file_path: str, *,
                    headers: Optional[Dict[str, str]] = None,
                    timeout: Optional[int] = None) -> Any:
        """
        Upload a file from a local path to the specified URL.
        """
        raise NotImplementedError("upload_file must be implemented by subclasses.")

    @abstractmethod
    def create_session(self) -> Any:
        """
        Create and return a persistent HTTP session.
        """
        raise NotImplementedError("create_session must be implemented by subclasses.")

    @abstractmethod
    def close_session(self, session: Any) -> None:
        """
        Close a persistent HTTP session.
        """
        raise NotImplementedError("close_session must be implemented by subclasses.")

    @abstractmethod
    def set_cookies(self, session: Any, cookies: Dict[str, str]) -> None:
        """
        Set cookies for the given session.
        """
        raise NotImplementedError("set_cookies must be implemented by subclasses.")

    @abstractmethod
    def get_cookies(self, session: Any) -> Dict[str, str]:
        """
        Retrieve cookies from the given session.
        """
        raise NotImplementedError("get_cookies must be implemented by subclasses.")

    @abstractmethod
    def stream_request(self, method: str, url: str, *,
                       headers: Optional[Dict[str, str]] = None,
                       params: Optional[Dict[str, Union[str, int]]] = None,
                       data: Optional[Any] = None,
                       json: Optional[Any] = None,
                       timeout: Optional[int] = None) -> Iterator[bytes]:
        """
        Send an HTTP request and return an iterator over the response content.
        """
        raise NotImplementedError("stream_request must be implemented by subclasses.")

    @abstractmethod
    def add_request_interceptor(self, interceptor: Callable[[Dict[str, Any]], Dict[str, Any]]) -> None:
        """
        Add an interceptor to modify or log the outgoing HTTP request.
        
        :param interceptor: A callable that takes a request dictionary and returns a modified version.
        """
        raise NotImplementedError("add_request_interceptor must be implemented by subclasses.")

    @abstractmethod
    def add_response_interceptor(self, interceptor: Callable[[Any], Any]) -> None:
        """
        Add an interceptor to process or log the incoming HTTP response.
        
        :param interceptor: A callable that takes the response object and returns a modified version.
        """
        raise NotImplementedError("add_response_interceptor must be implemented by subclasses.")

    @abstractmethod
    def remove_request_interceptor(self, interceptor: Callable[[Dict[str, Any]], Dict[str, Any]]) -> None:
        """
        Remove a previously added request interceptor.
        """
        raise NotImplementedError("remove_request_interceptor must be implemented by subclasses.")

    @abstractmethod
    def remove_response_interceptor(self, interceptor: Callable[[Any], Any]) -> None:
        """
        Remove a previously added response interceptor.
        """
        raise NotImplementedError("remove_response_interceptor must be implemented by subclasses.")

    @abstractmethod
    def set_authentication(self, auth: Any) -> None:
        """
        Set authentication credentials for subsequent HTTP requests.
        """
        raise NotImplementedError("set_authentication must be implemented by subclasses.")

    @abstractmethod
    def clear_authentication(self) -> None:
        """
        Clear any previously set authentication credentials.
        """
        raise NotImplementedError("clear_authentication must be implemented by subclasses.")

    @abstractmethod
    def handle_redirects(self, allow: bool) -> None:
        """
        Configure whether the HTTP client should automatically follow redirects.
        """
        raise NotImplementedError("handle_redirects must be implemented by subclasses.")

    @abstractmethod
    def get_last_response(self) -> Optional[Any]:
        """
        Retrieve the last HTTP response received, if available.
        """
        raise NotImplementedError("get_last_response must be implemented by subclasses.")

    @abstractmethod
    def set_timeout(self, timeout: int) -> None:
        """
        Set a default timeout (in seconds) for all HTTP requests.
        """
        raise NotImplementedError("set_timeout must be implemented by subclasses.")

    @abstractmethod
    def get_timeout(self) -> int:
        """
        Get the current default timeout for HTTP requests.
        """
        raise NotImplementedError("get_timeout must be implemented by subclasses.")

    @abstractmethod
    def enable_logging(self, enable: bool = True) -> None:
        """
        Enable or disable logging of HTTP request and response details.
        """
        raise NotImplementedError("enable_logging must be implemented by subclasses.")

    @abstractmethod
    def disable_logging(self) -> None:
        """
        Disable logging of HTTP request and response details.
        """
        raise NotImplementedError("disable_logging must be implemented by subclasses.")

    @abstractmethod
    def set_retry_policy(self, retries: int, backoff_factor: float) -> None:
        """
        Configure a retry policy for failed HTTP requests.

        :param retries: Number of retry attempts.
        :param backoff_factor: Backoff factor for wait time between retries.
        """
        raise NotImplementedError("set_retry_policy must be implemented by subclasses.")

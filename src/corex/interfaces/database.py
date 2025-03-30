from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class DatabaseInterface(ABC):
    """
    CoreX Interface for Database (Raw Access).

    This interface standardizes low-level database operations for connecting, executing queries,
    managing transactions, and handling cursors. It is intended for use cases where a full ORM is not
    desired, providing direct access to the underlying database.
    """

    @abstractmethod
    def connect(self, connection_string: str) -> None:
        """
        Establish a connection to the database using the provided connection string.

        :param connection_string: The connection string with database credentials and parameters.
        """
        raise NotImplementedError("connect must be implemented by subclasses.")

    @abstractmethod
    def disconnect(self) -> None:
        """
        Close the database connection.
        """
        raise NotImplementedError("disconnect must be implemented by subclasses.")

    @abstractmethod
    def execute(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> Any:
        """
        Execute a SQL query or command against the database.

        :param query: The SQL query or command to execute.
        :param parameters: Optional parameters for parameterized queries.
        :return: The result of the query execution.
        """
        raise NotImplementedError("execute must be implemented by subclasses.")

    @abstractmethod
    def fetch_one(self) -> Optional[Any]:
        """
        Fetch a single record from the result of the last executed query.

        :return: A single record, or None if no more records are available.
        """
        raise NotImplementedError("fetch_one must be implemented by subclasses.")

    @abstractmethod
    def fetch_all(self) -> List[Any]:
        """
        Fetch all records from the result of the last executed query.

        :return: A list of records.
        """
        raise NotImplementedError("fetch_all must be implemented by subclasses.")

    @abstractmethod
    def begin_transaction(self) -> None:
        """
        Begin a new database transaction.
        """
        raise NotImplementedError("begin_transaction must be implemented by subclasses.")

    @abstractmethod
    def commit(self) -> None:
        """
        Commit the current transaction.
        """
        raise NotImplementedError("commit must be implemented by subclasses.")

    @abstractmethod
    def rollback(self) -> None:
        """
        Roll back the current transaction.
        """
        raise NotImplementedError("rollback must be implemented by subclasses.")

    @abstractmethod
    def close_cursor(self) -> None:
        """
        Close the current database cursor, if applicable.
        """
        raise NotImplementedError("close_cursor must be implemented by subclasses.")

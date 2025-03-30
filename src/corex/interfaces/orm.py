from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Type

class OrmInterface(ABC):
    """
    CoreX Interface for ORM.

    This interface standardizes common ORM operations including connection management,
    CRUD operations, transactions, bulk operations, and additional helper methods.
    Implementations can vary based on the underlying ORM framework (e.g., SQLAlchemy, Django ORM).
    """

    @abstractmethod
    def connect(self, connection_string: str) -> None:
        """
        Establish a connection to the database.

        :param connection_string: The database connection string.
        """
        raise NotImplementedError("connect must be implemented by subclasses.")

    @abstractmethod
    def disconnect(self) -> None:
        """
        Close the connection to the database.
        """
        raise NotImplementedError("disconnect must be implemented by subclasses.")

    @abstractmethod
    def create(self, model: Type, data: Dict[str, Any]) -> Any:
        """
        Create a new record for the given model.

        :param model: The model class.
        :param data: A dictionary of field names and values.
        :return: The created model instance.
        """
        raise NotImplementedError("create must be implemented by subclasses.")

    @abstractmethod
    def bulk_create(self, model: Type, data_list: List[Dict[str, Any]]) -> List[Any]:
        """
        Create multiple records for the given model in a single operation.

        :param model: The model class.
        :param data_list: A list of dictionaries, each containing field names and values.
        :return: A list of created model instances.
        """
        raise NotImplementedError("bulk_create must be implemented by subclasses.")

    @abstractmethod
    def read(self, model: Type, **filters) -> List[Any]:
        """
        Read records from the database for the given model using provided filters.

        :param model: The model class.
        :param filters: Keyword arguments representing field filters.
        :return: A list of model instances matching the filters.
        """
        raise NotImplementedError("read must be implemented by subclasses.")

    @abstractmethod
    def get_by_id(self, model: Type, record_id: Any) -> Optional[Any]:
        """
        Retrieve a single record by its primary key.

        :param model: The model class.
        :param record_id: The primary key of the record.
        :return: The model instance if found, otherwise None.
        """
        raise NotImplementedError("get_by_id must be implemented by subclasses.")

    @abstractmethod
    def update(self, model: Type, filters: Dict[str, Any], updates: Dict[str, Any]) -> int:
        """
        Update records matching the filters with the provided updates.

        :param model: The model class.
        :param filters: A dictionary of field filters to select records.
        :param updates: A dictionary of field updates to apply.
        :return: The number of records updated.
        """
        raise NotImplementedError("update must be implemented by subclasses.")

    @abstractmethod
    def update_or_create(self, model: Type, defaults: Dict[str, Any], **filters) -> Any:
        """
        Update a record if it exists, or create it if it doesn't.

        :param model: The model class.
        :param defaults: A dictionary of fields to update or create.
        :param filters: Keyword arguments representing field filters.
        :return: The updated or created model instance.
        """
        raise NotImplementedError("update_or_create must be implemented by subclasses.")

    @abstractmethod
    def delete(self, model: Type, **filters) -> int:
        """
        Delete records from the database for the given model using provided filters.

        :param model: The model class.
        :param filters: Keyword arguments representing field filters.
        :return: The number of records deleted.
        """
        raise NotImplementedError("delete must be implemented by subclasses.")

    @abstractmethod
    def delete_all(self, model: Type) -> int:
        """
        Delete all records for the given model.

        :param model: The model class.
        :return: The number of records deleted.
        """
        raise NotImplementedError("delete_all must be implemented by subclasses.")

    @abstractmethod
    def count(self, model: Type, **filters) -> int:
        """
        Count the number of records for the given model matching the filters.

        :param model: The model class.
        :param filters: Keyword arguments representing field filters.
        :return: The count of matching records.
        """
        raise NotImplementedError("count must be implemented by subclasses.")

    @abstractmethod
    def query(self, query_string: str, parameters: Optional[Dict[str, Any]] = None) -> Any:
        """
        Execute a raw SQL query on the database.

        :param query_string: The SQL query string.
        :param parameters: Optional dictionary of parameters for the query.
        :return: The result of the query execution.
        """
        raise NotImplementedError("query must be implemented by subclasses.")

    @abstractmethod
    def aggregate(self, model: Type, aggregation: Dict[str, Any], **filters) -> Any:
        """
        Perform an aggregation operation on the model's records.

        :param model: The model class.
        :param aggregation: A dictionary specifying the aggregation operations (e.g., sum, avg).
        :param filters: Keyword arguments representing field filters.
        :return: The aggregation result.
        """
        raise NotImplementedError("aggregate must be implemented by subclasses.")

    @abstractmethod
    def refresh(self, instance: Any) -> None:
        """
        Refresh a model instance from the database.

        :param instance: The model instance to refresh.
        """
        raise NotImplementedError("refresh must be implemented by subclasses.")

    @abstractmethod
    def begin_transaction(self) -> None:
        """
        Begin a new transaction.
        """
        raise NotImplementedError("begin_transaction must be implemented by subclasses.")

    @abstractmethod
    def commit_transaction(self) -> None:
        """
        Commit the current transaction.
        """
        raise NotImplementedError("commit_transaction must be implemented by subclasses.")

    @abstractmethod
    def rollback_transaction(self) -> None:
        """
        Roll back the current transaction.
        """
        raise NotImplementedError("rollback_transaction must be implemented by subclasses.")

    @abstractmethod
    def get_session(self) -> Any:
        """
        Retrieve the current session or connection object for advanced operations.

        :return: The current session or connection.
        """
        raise NotImplementedError("get_session must be implemented by subclasses.")

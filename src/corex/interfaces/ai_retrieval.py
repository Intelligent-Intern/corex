from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class Ai_retrievalInterface(ABC):
    """
    CoreX Interface for AI Retrieval.

    This interface standardizes operations for semantic and document retrieval in AI applications.
    Implementations can support various retrieval backends (e.g., FAISS, Pinecone, Milvus, Qdrant) and
    provide a consistent API for indexing, updating, deleting, and querying document collections or vector databases.
    """

    # Document management and indexing

    @abstractmethod
    def add_document(self, doc_id: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Add a single document to the retrieval index.

        :param doc_id: Unique identifier for the document.
        :param content: The content of the document.
        :param metadata: Optional metadata associated with the document.
        """
        raise NotImplementedError("add_document must be implemented by subclasses.")

    @abstractmethod
    def delete_document(self, doc_id: str) -> None:
        """
        Delete a document from the retrieval index.

        :param doc_id: Unique identifier for the document to be deleted.
        """
        raise NotImplementedError("delete_document must be implemented by subclasses.")

    @abstractmethod
    def update_document(self, doc_id: str, content: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Update an existing document in the retrieval index.

        :param doc_id: Unique identifier for the document.
        :param content: Updated content for the document.
        :param metadata: Updated metadata for the document.
        """
        raise NotImplementedError("update_document must be implemented by subclasses.")

    @abstractmethod
    def build_index(self, documents: List[Dict[str, Any]]) -> None:
        """
        Build or rebuild the retrieval index using a list of documents.
        Each document should be a dictionary with at least the keys 'id' and 'content',
        and optionally 'metadata'.

        :param documents: List of document dictionaries.
        """
        raise NotImplementedError("build_index must be implemented by subclasses.")

    @abstractmethod
    def get_document(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a document from the index by its unique identifier.

        :param doc_id: The document's unique identifier.
        :return: The document dictionary if found, otherwise None.
        """
        raise NotImplementedError("get_document must be implemented by subclasses.")

    # Querying and search

    @abstractmethod
    def query(self, query_text: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Query the retrieval index to find the most relevant documents for a given text query.

        :param query_text: The text query to search for.
        :param top_k: The number of top documents to return.
        :return: A list of document dictionaries, each including a relevance score.
        """
        raise NotImplementedError("query must be implemented by subclasses.")

    @abstractmethod
    def similarity_search(self, embedding: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Perform a similarity search using an embedding vector as the query.
        This method is typically used when the retrieval system supports vector-based search.

        :param embedding: A list of floats representing the query's embedding vector.
        :param top_k: The number of top results to return.
        :return: A list of document dictionaries with similarity scores.
        """
        raise NotImplementedError("similarity_search must be implemented by subclasses.")

    # Persistence and index management

    @abstractmethod
    def save_index(self, filepath: str) -> None:
        """
        Save the current retrieval index to a file.

        :param filepath: Path to the file where the index will be saved.
        """
        raise NotImplementedError("save_index must be implemented by subclasses.")

    @abstractmethod
    def load_index(self, filepath: str) -> None:
        """
        Load a retrieval index from a file.

        :param filepath: Path to the file from which the index will be loaded.
        """
        raise NotImplementedError("load_index must be implemented by subclasses.")

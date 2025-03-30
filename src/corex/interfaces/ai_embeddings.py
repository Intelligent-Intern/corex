from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Tuple

class Ai_embeddingsInterface(ABC):
    """
    CoreX Interface for AI Embeddings.

    This interface standardizes operations for generating and handling text embeddings.
    Implementations can support various embedding models (e.g., Sentence Transformers, fasttext, Gensim)
    and provide methods for generating embeddings, processing batches, and performing similarity searches.
    """

    @abstractmethod
    def load_model(self, model_name: str, **kwargs) -> None:
        """
        Load the embedding model using the given model name and optional configuration parameters.

        :param model_name: The identifier or name of the embedding model.
        :param kwargs: Additional configuration parameters (e.g., model path, device, batch size).
        """
        raise NotImplementedError("load_model must be implemented by subclasses.")

    @abstractmethod
    def embed_text(self, text: str, **kwargs) -> List[float]:
        """
        Generate an embedding vector for a single piece of text.

        :param text: The input text to be converted into an embedding.
        :param kwargs: Optional parameters, such as normalization or tokenization options.
        :return: A list of floats representing the embedding vector.
        """
        raise NotImplementedError("embed_text must be implemented by subclasses.")

    @abstractmethod
    def embed_batch(self, texts: List[str], **kwargs) -> List[List[float]]:
        """
        Generate embedding vectors for a batch of texts.

        :param texts: A list of texts to be converted into embeddings.
        :param kwargs: Optional parameters for batch processing.
        :return: A list where each element is an embedding vector corresponding to an input text.
        """
        raise NotImplementedError("embed_batch must be implemented by subclasses.")

    @abstractmethod
    def similarity(self, emb1: List[float], emb2: List[float]) -> float:
        """
        Compute the similarity between two embedding vectors (e.g., using cosine similarity).

        :param emb1: The first embedding vector.
        :param emb2: The second embedding vector.
        :return: A float representing the similarity score.
        """
        raise NotImplementedError("similarity must be implemented by subclasses.")

    @abstractmethod
    def similarity_search(self, query: str, corpus: List[str], top_k: int = 5, **kwargs) -> List[Tuple[str, float]]:
        """
        Perform a similarity search by comparing the embedding of a query text against a corpus of texts.

        :param query: The query text for which to find similar texts.
        :param corpus: A list of texts that constitute the search corpus.
        :param top_k: The number of top results to return.
        :param kwargs: Optional parameters for similarity computation or filtering.
        :return: A list of tuples where each tuple contains a corpus text and its similarity score.
        """
        raise NotImplementedError("similarity_search must be implemented by subclasses.")

    @abstractmethod
    def get_model_info(self) -> Dict[str, Any]:
        """
        Retrieve information about the loaded embedding model, such as its name, version, and embedding dimension.

        :return: A dictionary containing model details.
        """
        raise NotImplementedError("get_model_info must be implemented by subclasses.")

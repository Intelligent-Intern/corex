from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Iterator

class Ai_runtimesInterface(ABC):
    """
    CoreX Interface for AI Runtimes.

    This interface standardizes the execution of AI model runtimes and is designed to
    abstract over various implementations such as vLLM, text_generation_webui, Ollama,
    Ray, and TensorRT. Implementations should support initialization, model loading,
    inference (both synchronous and streaming), dynamic configuration updates, and
    graceful shutdown of runtime resources.
    """

    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> None:
        """
        Initialize the AI runtime environment using the provided configuration.

        :param config: A dictionary of configuration parameters (e.g., device settings, batch size).
        """
        raise NotImplementedError("initialize must be implemented by subclasses.")

    @abstractmethod
    def load_model(self, model_path: str, **kwargs) -> None:
        """
        Load an AI model into the runtime.

        :param model_path: Path or identifier of the model to load.
        :param kwargs: Additional parameters (e.g., model configuration, version).
        """
        raise NotImplementedError("load_model must be implemented by subclasses.")

    @abstractmethod
    def run_inference(self, input_data: Any, **kwargs) -> Any:
        """
        Run inference with the loaded model on the given input data.

        :param input_data: Data to be processed by the model.
        :param kwargs: Additional parameters for inference (e.g., temperature, top_k sampling).
        :return: The inference result (e.g., generated text, predictions).
        """
        raise NotImplementedError("run_inference must be implemented by subclasses.")

    @abstractmethod
    def stream_inference(self, input_data: Any, **kwargs) -> Iterator[Any]:
        """
        Execute inference in a streaming manner, yielding outputs incrementally.

        :param input_data: Data to be processed.
        :param kwargs: Additional parameters for streaming inference.
        :return: An iterator yielding parts of the inference output.
        """
        raise NotImplementedError("stream_inference must be implemented by subclasses.")

    @abstractmethod
    def update_config(self, config: Dict[str, Any]) -> None:
        """
        Update the runtime configuration dynamically.

        :param config: A dictionary of configuration updates.
        """
        raise NotImplementedError("update_config must be implemented by subclasses.")

    @abstractmethod
    def shutdown(self) -> None:
        """
        Gracefully shut down the AI runtime, releasing resources and closing connections.
        """
        raise NotImplementedError("shutdown must be implemented by subclasses.")

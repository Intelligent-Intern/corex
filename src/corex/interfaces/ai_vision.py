from abc import ABC, abstractmethod
from typing import Any, List, Dict, Tuple, Optional, Iterator

class Ai_visionInterface(ABC):
    """
    CoreX Interface for AI Vision – Extended

    This interface standardizes operations for computer vision tasks. In addition to basic
    tasks such as preprocessing, classification, object detection, segmentation, captioning,
    and feature extraction, this extended interface includes methods for advanced functionalities
    such as face detection, object tracking, optical character recognition (OCR), pose estimation,
    image enhancement, and video processing.
    """

    # Preprocessing and Basic Transformations
    @abstractmethod
    def preprocess(self, image: Any) -> Any:
        """
        Preprocess the input image (e.g., resizing, normalization, format conversion)
        for downstream vision tasks.
        """
        raise NotImplementedError("preprocess must be implemented by subclasses.")

    @abstractmethod
    def resize(self, image: Any, size: Tuple[int, int]) -> Any:
        """
        Resize the input image to the specified dimensions.
        """
        raise NotImplementedError("resize must be implemented by subclasses.")

    # Core Vision Tasks
    @abstractmethod
    def classify(self, image: Any) -> Dict[str, float]:
        """
        Classify the image and return a dictionary of labels with confidence scores.
        """
        raise NotImplementedError("classify must be implemented by subclasses.")

    @abstractmethod
    def detect_objects(self, image: Any) -> List[Dict[str, Any]]:
        """
        Detect objects in the image, returning a list of detections with bounding boxes, labels,
        and confidence scores.
        """
        raise NotImplementedError("detect_objects must be implemented by subclasses.")

    @abstractmethod
    def segment(self, image: Any) -> Any:
        """
        Perform image segmentation to produce a segmentation mask or similar structure.
        """
        raise NotImplementedError("segment must be implemented by subclasses.")

    @abstractmethod
    def caption(self, image: Any) -> str:
        """
        Generate a descriptive caption for the given image.
        """
        raise NotImplementedError("caption must be implemented by subclasses.")

    @abstractmethod
    def generate_image(self, prompt: str, **kwargs) -> Any:
        """
        Generate an image based on a text prompt using generative models.
        """
        raise NotImplementedError("generate_image must be implemented by subclasses.")

    @abstractmethod
    def extract_features(self, image: Any) -> List[float]:
        """
        Extract a feature vector or embedding from the image.
        """
        raise NotImplementedError("extract_features must be implemented by subclasses.")

    @abstractmethod
    def compute_similarity(self, image1: Any, image2: Any) -> float:
        """
        Compute a similarity score between two images based on their feature representations.
        """
        raise NotImplementedError("compute_similarity must be implemented by subclasses.")

    # Advanced and Extended Vision Capabilities
    @abstractmethod
    def detect_faces(self, image: Any) -> List[Dict[str, Any]]:
        """
        Detect human faces in the image.

        :return: A list of face detections with bounding boxes and confidence scores.
        """
        raise NotImplementedError("detect_faces must be implemented by subclasses.")

    @abstractmethod
    def track_objects(self, video: Any) -> Iterator[List[Dict[str, Any]]]:
        """
        Track objects across frames in a video.

        :return: An iterator that yields detection results (lists of objects) for each frame.
        """
        raise NotImplementedError("track_objects must be implemented by subclasses.")

    @abstractmethod
    def perform_ocr(self, image: Any) -> str:
        """
        Perform optical character recognition (OCR) on the image to extract text.
        """
        raise NotImplementedError("perform_ocr must be implemented by subclasses.")

    @abstractmethod
    def estimate_pose(self, image: Any) -> Dict[str, Any]:
        """
        Estimate human pose from the image, returning keypoints or skeleton data.
        """
        raise NotImplementedError("estimate_pose must be implemented by subclasses.")

    @abstractmethod
    def enhance_image(self, image: Any, enhancement_type: Optional[str] = None) -> Any:
        """
        Enhance the image using techniques such as denoising, super-resolution, or color correction.
        
        :param enhancement_type: Optional type of enhancement (e.g., "denoise", "super_resolution").
        """
        raise NotImplementedError("enhance_image must be implemented by subclasses.")

    @abstractmethod
    def process_video(self, video: Any, task: str, **kwargs) -> Any:
        """
        Process a video for a specified vision task (e.g., video classification, action recognition).
        
        :param task: The vision task to perform on the video.
        :return: The result of the video processing task.
        """
        raise NotImplementedError("process_video must be implemented by subclasses.")

    # Visualization and Post-Processing
    @abstractmethod
    def visualize_detections(self, image: Any, detections: List[Dict[str, Any]]) -> Any:
        """
        Overlay detection results on the image for visualization.
        """
        raise NotImplementedError("visualize_detections must be implemented by subclasses.")

    @abstractmethod
    def display(self, image: Any) -> None:
        """
        Display the image using an appropriate visualization backend.
        """
        raise NotImplementedError("display must be implemented by subclasses.")

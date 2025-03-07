from typing import List, Tuple, Dict, Any, Optional
import numpy as np
from keras._tf_keras.keras import Sequential

class HAI:
    def __init__(self, NLP_data: Optional[str] = None, model_file: Optional[str] = None) -> None:
        """
        Initialize the HAI class.

        :param NLP_data: Path to the NLP data file (JSON format).
        :param model_file: Path to the pre-trained model file (HDF5 format).
        """
        ...

    def Tokenizer(self, text: str) -> Optional[List[str]]:
        """
        Tokenize the input text.

        :param text: Input text to tokenize.
        :return: List of tokens or None if text is empty.
        """
        ...

    def preprocess_data(self) -> None:
        """
        Preprocess the NLP data from the JSON file.
        """
        ...

    def make_bow(self, sentence: str, all_words: List[str], tkn_low: bool = True) -> np.ndarray:
        """
        Create a Bag of Words (BoW) representation of the sentence.

        :param sentence: Input sentence.
        :param all_words: List of all words in the vocabulary.
        :param tkn_low: Whether to lowercase the sentence before tokenization.
        :return: Bag of Words representation as a numpy array.
        """
        ...

    def create_train_data(self) -> None:
        """
        Create training data from the preprocessed documents.
        """
        ...

    def predict(self, sentence: str, model: Sequential) -> Optional[Dict[str, str]]:
        """
        Predict the intent of the input sentence.

        :param sentence: Input sentence to predict.
        :param model: Trained Keras model.
        :return: Dictionary containing the predicted intent and probability, or None if prediction is below threshold.
        """
        ...

    def get_response(self, intents_prd: Optional[Dict[str, str]], all_intents: Dict[str, Any]) -> str:
        """
        Get a response based on the predicted intent.

        :param intents_prd: Predicted intent and probability.
        :param all_intents: All intents from the NLP data.
        :return: A response string.
        """
        ...

    def Chat(self, message: str) -> str:
        """
        Chat with the model using the input message.

        :param message: Input message to the chatbot.
        :return: Response from the chatbot.
        """
        ...

    def Train(self) -> None:
        """
        Train the chatbot model using the preprocessed data.
        """
        ...
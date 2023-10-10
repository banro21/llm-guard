from typing import List

from llm_guard.input_scanners.ban_topics import BanTopics as InputBanTopics

from .base import Scanner


class BanTopics(Scanner):
    """
    A text scanner that checks whether the generated text output includes banned topics.

    The class uses the zero-shot-classification model from Hugging Face to scan the topics present in the text.
    """

    def __init__(self, topics=List[str], threshold: float = 0.75):
        """
        Initializes BanTopics with a list of topics and a probability threshold.

        Parameters:
            topics (List[str]): The list of topics to be banned from the text.
            threshold (float): The minimum probability required for a topic to be considered present in the text.
                               Default is 0.75.

        Raises:
            ValueError: If no topics are provided.
        """
        self._scanner = InputBanTopics(topics=topics, threshold=threshold)

    def scan(self, prompt: str, output: str) -> (str, bool, float):
        return self._scanner.scan(output)

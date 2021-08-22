# Requests import for API calls
import requests

# Regular Expression Class Imports
import re


class YouTubeTranscriptSummarizer:
    def __init__(self, debug_logs: bool = False):
        # Mutual-Exclusively Required Variables
        self._video_url: str = str()
        self._video_id: str = str()

        # Required Variables
        self._percent: int = int()
        self._choice: str = str()

        # Internal Values
        self._debug_logs: bool = debug_logs
        self._choices_list = ["gensim-sum", "spacy-sum", "nltk-sum", "sumy-lsa-sum", "sumy-luhn-sum",
                              "sumy-text-rank-sum"]

    def get_by_url(self, video_url: str, percent: int = 20, choice: str = "gensim-sum") -> (str, dict):
        """Returns summary for the given YouTube URL. This method requests our API to deliver your desired summary.
        Read our documentation for proper usage.

            :param video_url: str
                - The Video URL for which you want to generate the summary.
            :param percent: int
                - Percentage value is used to generate summary in X% lines of the whole transcript.
                Use values from 20 to 30 to get better results.
            :param choice: str
                - Algorithm Choice which you would like to use for summarization. Default Algorithm is Text Rank
                Summarization using Gensim. Accepted values are:
                ["gensim-sum", "spacy-sum", "nltk-sum", "sumy-lsa-sum", "sumy-luhn-sum", "sumy-text-rank-sum"].
                Read documentation for more details on these choices.
            :returns: str
                - Summary of the YouTube Video.

        """

        # Storing received arguments in instance variables
        self._video_url = video_url
        self._percent = percent

        # Checking Algorithm String
        if choice in self._choices_list:
            self._choice = choice
        else:
            raise AlgorithmArgumentErrorException(choice)

        # Informatory Console Print
        if self._debug_logs:
            print("\nVideo URL is: {}".format(video_url))

        # Returning summary after processing.
        return self.__summarize(has_video_id=False)

    def get_by_id(self, video_id: str, percent: int = 20, choice: str = "gensim-sum") -> (str, dict):
        """Returns summary for the given YouTube ID. This method requests our API to deliver your desired summary.
        Read our documentation for proper usage.

            :param video_id: str
                - The Video ID for which you want to generate the summary. Each video has a unique ID.
            :param percent: int
                - Percentage value is used to generate summary in X% lines of the whole transcript.
                Use values from 20 to 30 to get better results.
            :param choice: str
                - Algorithm Choice which you would like to use for summarization. Default Algorithm is Text Rank
                Summarization using Gensim. Accepted values are:
                ["gensim-sum", "spacy-sum", "nltk-sum", "sumy-lsa-sum", "sumy-luhn-sum", "sumy-text-rank-sum"].
                Read documentation for more details on these choices.
            :returns: str
                - Summary of the YouTube Video.

        """

        # Storing received arguments in instance variables
        self._video_id = video_id
        self._percent = percent

        # Checking Algorithm String
        if choice in self._choices_list:
            self._choice = choice
        else:
            raise AlgorithmArgumentErrorException(choice)

        # Informatory Console Print
        if self._debug_logs:
            print("\nVideo ID is: {}".format(video_id))

        # Returning summary after processing.
        return self.__summarize(has_video_id=True)

    def __summarize(self, has_video_id: bool) -> (str, dict):
        # Informatory Console Print
        if self._debug_logs:
            print("Percentage is: {}%".format(self._percent))
            print("Algorithm Choice is: \"{}\" - {}\n".format(self._choice, _detailed_parse_choice(self._choice)))

            print("•> Making Summarization Request. Please Wait!")

        # Make the summary request to the API Now.

        # Capturing the video id
        if has_video_id:
            # Create temporary variable to check the id's validity by the same regular expression.
            temp = "https://www.youtube.com/watch?v={}".format(self._video_id)
            video_id = _parse_youtube_video_id(temp)
        else:
            video_id = _parse_youtube_video_id(self._video_url)

        # Capturing all variables
        percent = str(self._percent)
        choice = self._choice

        # Characters for bold font : We have to start and end with these characters
        bold_start = ''
        bold_end = ''
        # bold_start = '\033[1m'
        # bold_end = '\033[0m'

        # Making a new request to our server.
        if video_id:
            # https://ytsum.herokuapp.com
            # http://127.0.0.1:5000
            try:
                response = requests.get(
                    "https://ytsum.herokuapp.com/summarize/?id=" + video_id + "&percent=" + percent + "&choice=" + choice)
                if self._debug_logs:
                    print('•> {}Making Summarization Request ✓{}'.format(bold_start, bold_end))
                    print('•> {}Displaying Response Result ✓{}'.format(bold_start, bold_end))
                # Getting response
                summary_response = response.json()
                # Printing received message
                if self._debug_logs:
                    print("•> {}{}{}".format(bold_start, summary_response['message'], bold_end))
                if summary_response['success']:
                    # Success True, so print received summary and other items
                    json_response = summary_response['response']
                    return json_response['processed_summary'], {'length_original': json_response['length_original'],
                                                                'sentence_original': json_response['sentence_original'],
                                                                'length_summary': json_response['length_summary'],
                                                                'sentence_summary': json_response['sentence_summary']}
                else:
                    # Success Failure, Raise exception
                    raise SummarizationFailureErrorException(summary_response['message'])
            except requests.ConnectionError:
                # Connection error, display error message.
                if self._debug_logs:
                    print('•> {}Summarization Request Failed ✕{}'.format(bold_start, bold_end))
                # Raising exception.
                raise ConnectionErrorException
        else:
            # Video Id was invalid (URL parse check)
            if self._debug_logs:
                print('•> {}Improper Summarization Request ✕{}'.format(bold_start, bold_end))
            # Raise relevant exception.
            if has_video_id:
                raise VideoIDInvalidErrorException
            else:
                raise VideoURLInvalidErrorException


def _detailed_parse_choice(choice):
    """Return Selected Choice's Full Name string as per its codename. Choices are based as per our server.

        :param choice: str
            The code name of the choice
        :return: str
            Return Selected Choice's Full Name string as per its codename
        """

    # Return Choice Full Name string
    if choice == "gensim-sum":
        return "Text Rank Algorithm Based (Gensim)"
    elif choice == "spacy-sum":
        return "Frequency Based (Spacy)"
    elif choice == "nltk-sum":
        return "Frequency Based (NLTK)"
    elif choice == "sumy-lsa-sum":
        return "Latent Semantic Analysis Based (Sumy)"
    elif choice == "sumy-luhn-sum":
        return "Luhn Algorithm Based (Sumy)"
    elif choice == "sumy-text-rank-sum":
        return "Text Rank Algorithm Based (Sumy)"


def _parse_youtube_video_id(url: str):
    """Extract the ``video_id`` from a YouTube url.

    :param url: str
        A YouTube url containing a video id.
    :returns:
        YouTube video id or boolean False if it is not valid.
    """
    return _regex_search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url, group=1)


def _regex_search(pattern: str, string: str, group: int):
    """Shortcut method to search a string for a given pattern.

    :param str pattern:
        A regular expression pattern.
    :param str string:
        A target string to search.
    :param int group:
        Index of group to return.
    :returns:
        Substring pattern matches.
    """
    regex = re.compile(pattern)
    results = regex.search(string)
    if not results:
        return False

    return results.group(group)


class YouTubeTranscriptSummarizeError(Exception):
    """Base Class for raising errors in this package."""


class ConnectionErrorException(YouTubeTranscriptSummarizeError):
    def __init__(self, message="A Connection Error Occurred while making request."):
        self.message = message
        super().__init__(self.message)


class VideoIDInvalidErrorException(YouTubeTranscriptSummarizeError):
    def __init__(self, message="Your YouTube video ID is invalid. Please check your arguments."):
        self.message = message
        super().__init__(self.message)


class VideoURLInvalidErrorException(YouTubeTranscriptSummarizeError):
    def __init__(self, message="Your YouTube video URL is invalid. Please check your arguments."):
        self.message = message
        super().__init__(self.message)


class SummarizationFailureErrorException(YouTubeTranscriptSummarizeError):
    def __init__(self, message):
        self.message = message + " We failed due to this reason."
        super().__init__(self.message)


class AlgorithmArgumentErrorException(YouTubeTranscriptSummarizeError):
    def __init__(self, choice):
        self.message = "Your Choice is: '" + choice + "'. But, we accept these values only: " + \
                       '["gensim-sum", "spacy-sum", "nltk-sum", "sumy-lsa-sum", "sumy-luhn-sum", "sumy-text-rank-sum"]' \
                       + "\nRead our documentation for more details if you are choosing algorithm manually."
        super().__init__(self.message)

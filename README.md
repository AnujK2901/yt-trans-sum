# YouTube Transcript Summarizer: Python Package
### Python Package for using our YouTube Video Transcript Summarizer. This repository makes GET requests to our Flask back-end server API at `/summarize/` endpoint.
#### More details about this backend can be read at our [back-end repository](https://github.com/AnujK2901/yt-sum-flask).
**YouTube Video Transcript Summarization using PIP:** Yes. You heard it right! This package is avaialble on PIP. Just go through this README file to know can you integrate it in your project.
When ever you make a call to the function of our package, it sends API call to our Flask server, and then the server responds back with the summarized text response. Then you can further display the received result to the user.\
As we make API calls to our back-end, this package needs an internet connection to received summarized transcript using `requests`.

##### Requirements
* `Python` `>=3.6` (Use as latest as possible version for more performance.)
* `requests` `>=2.25.1` (Makes for API calls to our server)

![](/readme_images/image_cover_p.png)

*Pre-requisite Knowledge:* YouTube is an American free to use online video sharing and social media platform launched in February 2005. It is currently one of the biggest video platforms where its users watch more than 1 billion hours of videos every day.\
Closed captions are the text derived from the video which are intended for adding more details (such as dialogues, speech translation, non-speech elements) for the viewer. They are widely used to understand video without understanding its audio.

*Use case Scenario:* YouTube has very large number of videos which has transcripts. Summarization would be especially helpful in the cases where videos are longer in length and different parts might have varying importance. In this sense, Summarization of the video might be useful in saving the viewer’s time. It will help in improving user productivity since they will focus only on the important text spoken in video. 

## Aim
This repository is part of our project, in which there is a back-end server using Flask Framework. The backend has also a browser based summarizer, but the package available in this repository depict how server-client server makes efficient use of our code!\
When you install the package, and then invoke the function, it makes request only, and the back-end summarizes the transcript, and sends the response back in `JSON Format`.\
This package returns a `tuple` which has a summary and some insights about your requests. Read below for more details

### Installation and Usage
You can go to your terminal and make sure that `pip` is installed. Then, simply type:
```
pip install yt_trans_sum
```
Now, you can import the package like this:
```
from yt_trans_sum import YouTubeTranscriptSummarizer

if __name__ == "__main__":
    # Simplest Call
    my_summary, my_summary_insights = YouTubeTranscriptSummarizer().get_by_url('https://www.youtube.com/watch?v=zhUgaKb0s5A')
    print("My Summary:", my_summary)
    print("My Summary Insights: ", my_summary_insights)
```
Here, 'my_summary_insights` is a dictionary with key-value pairs of your insights. Below snippet can help you understand the values inside this dictionary.
```
# There are 4 values inside this dictionary for now. The snippet is self explanatory.
print("Characters in Transcript:", my_summary_insights['length_original'])
print("Sentences in Transcript:", my_summary_insights['sentence_original'])
print("Characters in Summary:", my_summary_insights['length_summary'])
print("Sentences in Transcript:", my_summary_insights['sentence_summary'])
```

### More Examples of Usage
1. Print logs while we request the summary
```
from yt_trans_sum import YouTubeTranscriptSummarizer

if __name__ == "__main__":
    # Debug Logs True
    my_summary, my_summary_insights = YouTubeTranscriptSummarizer(debug_logs=True).get_by_url('https://www.youtube.com/watch?v=zhUgaKb0s5A')
    print("My Summary:", my_summary)
    print("My Summary Insights: ", my_summary_insights)
```
The backend requires video id, algorithm and a percentage to summarize the transcript.
* * **`id`** : Video ID of the YouTube Video. Each video has its own unique ID in its URL.\
  For example, *9No-FiEInLA* is the Video ID in *https​://www​.youtube​.com/watch?v=9No-FiEInLA.*.
* **`choice`** : Algorithm Choice for the summarizing the Transcript. There are only six accepted values in this variable.\
  These choices are written along with algorithm names as follows:
    * `gensim-sum` : Text Rank Algorithm Based using Gensim
    * `spacy-sum` : Frequency Based Approach using Spacy.
    * `nltk-sum` : Frequency Based Summarization using NLTK.
    * `sumy-lsa-sum` : Latent Semantic Analysis Based using Sumy.
    * `sumy-luhn-sum` : Luhn Algorithm Based using Sumy.
    * `sumy-text-rank-sum` : Text Rank Algorithm Based using Sumy.
* **`percent`** : The percentage is used to present the summary in approx. `X% lines` of the available transcript. Values between 20 to 30 give better results.
**NOTE:** By default, Algorithm selected is gensim-sum and percentage is 20. You can these values from below examples.

2. Change percentage and algorithm for the summary request:
```
from yt_trans_sum import YouTubeTranscriptSummarizer

if __name__ == "__main__":
    # Full control of arguments
    my_summary, my_summary_insights = YouTubeTranscriptSummarizer().get_by_url(video_url='https://www.youtube.com/watch?v=zhUgaKb0s5A', percent=10, choice='sumy-lsa-sum'
    print("My Summary:", my_summary)
    print("My Summary Insights: ", my_summary_insights)
```
3. Summarization request by using video ID instead of video URL
```
from yt_trans_sum import YouTubeTranscriptSummarizer

if __name__ == "__main__":
    # get_by_id() is called instead of get_by_url()
    my_summary, my_summary_insights = YouTubeTranscriptSummarizer().get_by_id(video_id='zhUgaKb0s5A', percent=10, choice='umy-lsa-sum'
    print("My Summary:", my_summary)
    print("My Summary Insights: ", my_summary_insights)
```

### More information about the backend
You can click [here](https://github.com/AnujK2901/yt-sum-flask#more-information-about-the-backend) to know more about how backend receives and sends data.

#### Feel free to improve this package or even our back-end, add comments and ask any queries if you have any.

##### The back-end uses an undocumented part of the YouTube API, which is called by the YouTube web-client. So there is no guarantee that it would stop working tomorrow, if they change how things work. In case that happens, I will do my best to make things work again as soon as possible if that happens. So if it stops working, let me know!
##### This is not an official package from YouTube. I have built this package for my final year project.

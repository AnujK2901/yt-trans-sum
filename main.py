from yt_trans_sum import YouTubeTranscriptSummarizer

if __name__ == "__main__":
    my_summary, my_summary_insights = YouTubeTranscriptSummarizer().get_by_url('https://www.youtube.com/watch?v=zhUgaKb0s5A')
    print("My Summary:", my_summary)
    print("My Summary Insights: ", my_summary_insights)

    print("Characters in Transcript:", my_summary_insights['length_original'])
    print("Sentences in Transcript:", my_summary_insights['sentence_original'])
    print("Characters in Summary:", my_summary_insights['length_summary'])
    print("Sentences in Transcript:", my_summary_insights['sentence_summary'])

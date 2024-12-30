from nltk.sentiment import SentimentIntensityAnalyzer

from backend.get_comments import get_comments
from backend.preprocess import pipeline


def get_sentiment(id):
    sentiment_object = SentimentIntensityAnalyzer()
    try:
        video_comments = get_comments(id)
    except:
        return False

    polarity = []
    comments = []
    negative_count = 0
    neutral_count = 0
    positive_count = 0

    for comment in video_comments:
        sentiment_dict = sentiment_object.polarity_scores(pipeline(comment))
        polarity.append(sentiment_dict["compound"])
        comments.append(comment)
        if sentiment_dict["compound"] >= -1 and sentiment_dict["compound"] <= (-1 / 3):
            negative_count += 1
        elif sentiment_dict["compound"] > (-1 / 3) and sentiment_dict["compound"] < (
            1 / 3
        ):
            neutral_count += 1
        else:
            positive_count += 1

    negaitve_percentage = negative_count / len(video_comments)
    neutral_percentage = neutral_count / len(video_comments)
    positive_percentage = positive_count / len(video_comments)

    score_index_pairs = [(score, i) for i, score in enumerate(polarity)]
    sorted_pairs = sorted(score_index_pairs, key=lambda x: x[0], reverse=True)
    scores, sorted_indices = zip(*sorted_pairs)
    comments = [comments[i] for i in sorted_indices]
    return (
        sum(polarity) / len(polarity),
        len(polarity),
        comments[0],
        scores[0],
        (negaitve_percentage, neutral_percentage, positive_percentage),
    )


def comment_score(comment):
    sentiment_object = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_object.polarity_scores(pipeline(comment))
    return sentiment_dict["compound"]

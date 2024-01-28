from analyzer import AnalysisResult
from analyzer_prowritingaid import filler, analyze, getTotal
from transcriber_deepgram import TranscriptionData, transcriber


#result = transcriber(filepath)
#first_alt_transcript = result.alternatives[0].transcript


def score_generator(analysis: TranscriptionData) -> float:
    score = 100
    total = 0
    weights = [2, 2, 2, 2, 3]

    word = getTotal(analysis)

    i = analyze(analysis)
    for num in range(len(weights)):
        total += weights[num] * i[num]
    return  round((99 - ((50*total)/word + (filler(analysis))/2)))


print(score_generator("Along the way, he must face like a host of mythological like enemies determined to stop him. Most like of all, he must come to terms um with a uh father he has never known, and an Oracle that has warned him of betrayal by a friend."))


# def score_generator1(analysis: AnalysisResult) -> float:
#     score = 100
#     for err in analysis.errors:
#         print(err)
#         size = err.error_len / 5  # characters per error

#         # https://www.w3.org/International/multilingualweb/lt/drafts/its20/its20.html#lqissue-typevalues
#         match err.issue_type:
#             case "misspelling":
#                 factor = 5.0

#         score -= size*factor

#     return score


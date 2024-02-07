from analyzer import AnalysisResult
from analyzer_prowritingaid import filler, analyze, getTotal
from transcriber_deepgram import TranscriptionData, transcriber


#result = transcriber(filepath)
#first_alt_transcript = result.alternatives[0].transcript


def score_generator(transcript: str, issue_scores: list[int], filler_ratio: float) -> int:
    score = 100
    total = 0
    weights = [2, 2, 2, 2, 3]

    word = getTotal(transcript)

    # i = analyze(analysis)
    for num in range(len(weights)):
        total += weights[num] * issue_scores[num]
        score = round(99 - ((50*total)/word + (filler_ratio/2)))
        if (score >= 11):
            return score
        else:
            return 11

def improvement_message(transcript: str) -> str:
    nums = (analyze(transcript))
    a = nums[0][0]
    b = nums[0][1]
    c = nums[0][2]
    d = nums[0][3]
    e = nums[0][4]
    if a == (max(a,b,c,d,e)):
        return "Pay more attention to your grammar!"
    elif b == (max(a,b,c,d,e)):
        return "Speak in a more active voice!"
    elif c == (max(a,b,c,d,e)):
        return "Avoid using the same words too much!"
    elif d == (max(a,b,c,d,e)):
        return "Avoid using the same phrases too much!"
    else:
        return "Be more specific and precise!"
        

#"grammar", "passive", "overused", "wordsphrases", "vague"],
#print(improvement_message("Along the way, he must face like a host of mythological like enemies determined to stop him. Most like of all, he must come to terms um with a uh father he has never known, and an Oracle that has warned him of betrayal by a friend."))


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


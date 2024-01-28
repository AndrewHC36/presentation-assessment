from analyzer import AnalysisResult


def score_generator(analysis: AnalysisResult) -> float:
    score = 100
    for err in analysis.errors:
        print(err)
        size = err.error_len / 5  # characters per error

        # https://www.w3.org/International/multilingualweb/lt/drafts/its20/its20.html#lqissue-typevalues
        match err.issue_type:
            case "misspelling":
                factor = 5.0

        score -= size*factor

    return score


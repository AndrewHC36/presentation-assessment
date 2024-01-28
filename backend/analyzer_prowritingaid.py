import time
from dataclasses import dataclass

import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException

from analyzer import AnalysisResult


@dataclass
class ErrorTag:
    category: str
    # sub_category: str
    start_pos: int
    end_pos: int


@dataclass
class ProWritingAidAnalysis:
    word_count: int
    errors: list[ErrorTag]
    filler_word_counts: int


def analyze(transcription: str) -> ProWritingAidAnalysis:
    configuration = ProWritingAidSDK.Configuration()

    configuration.api_key['licenseCode'] = '5FE9BDA7-A576-4887-A7F0-840F49043575'
    configuration.host = 'https://api.prowritingaid.com'

    api_instance = ProWritingAidSDK.TextApi(ProWritingAidSDK.ApiClient('https://api.prowritingaid.com'))

    raw_words = transcription.split(" ")
    filler_words = raw_words.count("uh")+raw_words.count("um")+raw_words.count("mhmm")+ \
        raw_words.count("mm-mm")+raw_words.count("uh-uh")+raw_words.count("uh-huh")+ \
        raw_words.count("nuh-uh")

    req = ProWritingAidSDK.TextAnalysisRequest(
        transcription,
        [
            "acronym", "allsentences", "cliche", "complex", "consistency", "grammar",
            "overused", "pacing", "passive", "sentiment", "overview", "vague"],
        "General",
        "en"
    )

    try:
        # Tries to get the result of a request using the task id of the request
        api_response = api_instance.post(req)
        # print(api_response)

        errors = api_response.result.tags
        word_count = api_response.result.word_count
        summaries = api_response.result.summaries  # TODO: very complicated structure (for future impl)
        # print(api_response.task_id)
        # time.sleep(3)
        # data = api_instance.post(api_response.task_id)
        # print(data)

        return ProWritingAidAnalysis(
            word_count = word_count,
            filler_word_counts = filler_words,
            errors = [
                ErrorTag(
                    category = err.category,
                    # sub_category = err.subcategory,
                    start_pos = err.start_pos,
                    end_pos = err.end_pos,
                )
                for err in errors
            ]
        )
    except ApiException as e:
        print("Exception when calling TextApi->get: %s\n" % e)


if __name__ == '__main__':
    analysis = analyze("alright you know when when you uh like you know like that's uh and you you you when you you you uh you you do the things so that uh you yeah yes uh indeed")
    print(analysis)


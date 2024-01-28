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
    filler_word_count: int

def filler(transcription: str) -> ProWritingAidAnalysis:
    raw_words = transcription.split(" ")
    word_count = len(raw_words)
    filler_words_count = raw_words.count("uh")+raw_words.count("just")+raw_words.count("like")/2+ \
        raw_words.count("mm-mm")+raw_words.count("uh-uh")+raw_words.count("uh-huh")+ \
        raw_words.count("nuh-uh")+raw_words.count("basically")/2+raw_words.count("um")+\
        raw_words.count("mhmm")+raw_words.count("actually")/2+raw_words.count("right")
        # +\ raw_words.count("Uh")+ raw_words.count("Just")+raw_words.count("Like")+ \
        # raw_words.count("Mm-mm")+raw_words.count("Uh-uh")+raw_words.count("Uh-huh")+ \
        # raw_words.count("Nuh-uh")+raw_words.count("Basically")+raw_words.count("Um")+\
        # raw_words.count("Mhmm")+raw_words.count("Actually")+raw_words.count("Right")
    percentage = (round(filler_words_count/word_count * 100))
    return percentage

    #if(percentage <= 5):
    #    return("Amazing! {}% of your presentation is filler words!".format(percentage))
    #elif(percentage <=10):
    #    return("Good job! {}% of your presentation is filler words!".format(percentage))
    # elif(percentage <=25):
    #     return("Watch out! {}% of your presentation is filler words!".format(percentage))
    # else:
    #     return("You might want to use less filler words. {}% of your presentation is filler words!".format(percentage))



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
            "grammar", "passive", "overused", "wordsphrases", "vague"],
        "General",
        "en"
    )
    

    try:
        # Tries to get the result of a request using the task id of the request
        api_response = api_instance.post(req)
        #print(api_response)
        # json_text = api_response.read().decode(encoding='utf-8')
        # raw_data = json.loads(json_text)
        issue_weights = []
        issues = api_response.result.summaries
        issue_scores = []
        for i in issues:
            issue_scores.append(i.number_of_issues)
        grammar_issues = api_response.result.summaries[0].number_of_issues
        errors = api_response.result.tags
        word_count = api_response.result.word_count
        summaries = api_response.result.summaries  # TODO: very complicated structure (for future impl)
        # print(api_response.task_id)
        # time.sleep(3)
        # data = api_instance.post(api_response.task_id)
        # print(data)

        return issue_scores
    except ApiException as e:
        print("Exception when calling TextApi->get: %s\n" % e)



if __name__ == '__main__':
    #analysis = analyze("hello hi hello hi hello hi hello hi hello hi hi hello")
    analysis = analyze("Along the way, he must face a host of mythological enemies determined to stop him. Most of all, he must come to terms with a father he has never known, and an Oracle that has warned him of betrayal by a friend.")
    print(analysis)
    #print(filler("alright you know when when you uh like you know like that's uh and you \
       # you you when you you you uh you you do the things so that uh you yeah yes uh indeed")) #this will be a variable later on
#test cases
#if __name__ == '__main__':
#    analysis = analyze("alright you know when when you uh like you know like that's uh and you \
#        you you when you you you uh you you do the things so that uh you yeah yes uh indeed")
#    analysis1 = analyze("hi")
#    analysis2 = analyze("hi hi hi hi hi hi hi hi hi hi uh")
#    analysis3 = analyze("hi hi hi like")
#    analysis4 = analyze("like like like")
#    print(analysis)
#    print(analysis1)
#    print(analysis2)
#    print(analysis3)
#    print(analysis4)


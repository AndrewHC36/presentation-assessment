import requests
from enum import Enum
from dataclasses import dataclass


# https://www.w3.org/International/multilingualweb/lt/drafts/its20/its20.html#lqissue-typevalues
# class IssueTypes(Enum):
#     TERMINOLOY = 1
#     MISTRANSLATION = 2
#     OMISSION = 3
#     UNTRANSLATED = 4
#     ADDITION = 5
#     DUPLICATION = 6
#     INCONSISTENCY = 7
#     GRAMMAR = 8
#     LEGAL = 9
#     REGISTER = 10
#     LOCALE_SPECIFIC_CONTENT = 11
#     LOCALE_VIOLATION = 12
#     STYLE = 13
#     CHARACTERS = 14
#     MISSPELLING = 15
#     TYPOGRAPHICAL = 16
#     FORMATTING = 17
#     INCONSISTENT_ENTITIES = 18
#     NUMBERS = 19
#     MARKUP = 20
#     PATTERN_PROBLEM = 21
#     WHITESPACE = 22
#     INTERNATIONALIZATION = 23
#     LENGTH = 24
#     NON_CONFORMANCE = 25
#     UNCATEGORIZED = 26
#     OTHER = 27


@dataclass
class Error:
    replacements: list[str]
    error_offset: int
    error_len: int
    issue_type: str

@dataclass
class AnalysisResult:
    detected_lang: str  # e.g., en-US
    confidence: float
    errors: list[Error]



def analyze(transcription: str) -> AnalysisResult:
    resp = requests.get(  # TODO: post
        "https://api.languagetoolplus.com/v2/check",
        params = {
            "text": transcription,
            "language": "en-US"
        },
    )

    data = resp.json()

    # print("LANG:", data["language"])
    # for m in data["matches"]:
    #     print("ERROR MATCHED")
    #     print("Message:", m["message"])
    #     print("Short Message:", m["shortMessage"])
    #     print("Replacements:", m["replacements"])
    #     print("Error Offset:", m["offset"])
    #     print("Error Length:", m["length"])  # could be used for assessment
    #     print("Context:", m["context"])
    #     print("ISSUE TYPE:", m["rule"]["issueType"])  # could be used for assessment
    #     # print("CATEGORY:", m["rule"]["category"])  # could be used for assessment

    return AnalysisResult(
        detected_lang = data["language"]["detectedLanguage"]["code"],
        confidence = data["language"]["detectedLanguage"]["confidence"],
        errors = [
            Error(
                replacements = [r["value"] for r in m["replacements"]],
                error_offset = m["offset"],
                error_len = m["length"],
                issue_type = m["rule"]["issueType"],
            )
            for m in data["matches"]
        ]
    )


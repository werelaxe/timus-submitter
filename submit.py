import io
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}
SUBMIT_URL = "http://acm.timus.ru/submit.aspx"
LANGS = {
    "FreePascal 2.6": "31",
    "Visual C 2017": "39",
    "Visual C++ 2017": "40",
    "GCC 7.1": "45",
    "G++ 7.1": "46",
    "Clang++ 4.0.1": "47",
    "Java 1.8": "32",
    "Visual C# 2017": "41",
    "Python 2.7": "34",
    "Python 3.6": "48",
    "Go 1.3": "14",
    "Ruby 1.9": "18",
    "Haskell 7.6": "19",
    "Scala 2.11": "33",
    "Kotlin 1.1.4": "49",
    "Rust 1.9": "43",
}


def submit(judge_id, lang, task_id, source_code):
    data = {
        'JudgeID': io.BytesIO(judge_id.encode()),
        'Language': io.BytesIO(lang.encode()),
        'ProblemNum': io.BytesIO(str(task_id).encode()),
        'Source': io.BytesIO(source_code.encode()),
        'Action': io.BytesIO(b"submit"),
        'SpaceID': io.BytesIO(b"1")
    }
    response = requests.post(SUBMIT_URL, data=data, headers=HEADERS)
    response.raise_for_status()

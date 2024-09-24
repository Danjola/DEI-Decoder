import time
from src.utils.prompts import prompt

def check_ad_with_retry(job_posting_txt, masculine_coded, feminine_coded, llm, retries=3, delay=5):
    chain = prompt | llm
    for attempt in range(retries):
        try:
            res = chain.invoke({"job_posting": job_posting_txt, "masculine_coded": masculine_coded, "feminine_coded": feminine_coded})
            return res.content.replace("--", "")
        except Exception as e:
            if attempt + 1 < retries:
                time.sleep(delay)
            else:
                raise e
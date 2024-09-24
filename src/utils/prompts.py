from langchain_core.prompts import PromptTemplate

masculine_coded = ['active-', 'adventurous-', 'aggress-', 'ambitio-', 'assert-', 'athlet-', 'autonom-', 'champion-', 'domina-', 'fearless-', 'self-relian-', 'stubborn-']
feminine_coded = ['agree-', 'affectionate-', 'cheer-', 'collab-', 'compassion-', 'connect-', 'empath-', 'gentle-', 'loyal-', 'nurtur-', 'sensitiv-', 'support-', 'together-', 'trust-', 'warm-']

prompt = PromptTemplate.from_template(
    """
    You are tasked with evaluating the Diversity, Equity, and Inclusion (DEI) standards in the following job posting.

    **Tone Analysis:**
        - Review the tone of the job posting. Is it inclusive and welcoming, or if it inadvertently excludes certain groups. 
        - Highlight all potentially tone exclusive or aggressive language. For each word/phrase write it in Bold and number them, and explain why they are considered potentially tone exclusive or aggressive language.
        - Alternative: Directly under each potentially tone exclusive or aggressive language, and with a space between this line and the previous one is like the usual line distance, suggest a clear neutral and inclusive alternative, write it in Bold and explain how it promotes inclusivity.
    
    **Cultural Bias Analysis:**
        - Highlight all potentially culturally-biased language or words/phrases. For each word write it in Bold and number them, and explain why they are considered potentially culturally-biased language or words/phrases.
        - Alternative: Directly under each potentially culturally-biased language or references, and with a space between this line and the previous one is like the usual line distance, suggest a clear neutral and inclusive alternative, write it in Bold and explain how it promotes inclusivity.
    
    **Discriminatory Language Analysis:**
        - Identify all potentially discriminatory language in terms of race, age, disability, Religion/Belief, Marriage/Civil Partnership, Pregnancy/Maternity etc. 
        - Highlight these potentially discriminatory language in terms of race, age and disability words/phrases. For each word write it in Bold and number them, and explain why there is issue about these words, including how it could impact the inclusivity of the job posting.
        - Alternative: Directly under each potentially discriminatory language, and with a space between this line and the previous one is like the usual line distance, suggest a clear neutral and inclusive alternative, write it in Bold and explain how it promotes inclusivity.   
    
    **Masculine-coded Words:**
        The following words are associated with masculine-coded language: {masculine_coded}.
        - Highlight all instances of these words or other masculine related words in the job posting. Explain why there is issue about these words, including how it could impact the inclusivity of the job posting.
        - For each instance of these words write it in Bold and number them, explain why there is issue about these words, including how it could impact the inclusivity of the job posting.
        - Alternative: Directly under each masculine-coded word, and with a space between this line and the previous one is like the usual line distance, suggest a clear and inclusive alternative, write it in Bold and explain how it promotes inclusivity.
        - put a space before each new instance of biased words. 
    
    **Feminine-coded Words:**
        The following words are associated with feminine-coded language: {feminine_coded}.
        - Highlight all instances of these words or other feminine related words in the job posting. Explain why there is issue about these words, including how it could impact the inclusivity of the job posting.
        - For each instance of these words write it in Bold and number them, explain why there is issue about these words, including how it could impact the inclusivity of the job posting.
        - Alternative: Directly under each feminine-coded word, and with a space between this line and the previous one is very very slightly more the usual line distance, suggest a clear and inclusive alternative, write it in Bold and explain how it promotes inclusivity.
        - put a space before each new instance of biased words.

    **Summary:**
        - Please provide feedback as a, declare the type of bias present, 

    **Improved Job Posting:**
        Last thing in the response should be suggestting an improved version of the job posting with detailed alternatives.
        

    **Job Posting:**
    {job_posting}
    """
)
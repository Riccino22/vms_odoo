from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json

load_dotenv()

def translate_with_llm(word):
    template = """I am going to give you this word or phrase: "{phrase}" and you will translate this word or phrase from its language to English. Your response should be a Python object with the following structure:
    
    (opening curly brace)
    "word" : "word to translate",
    "translation" : "word translated to English. If the word is already in English, then use the same word",
    "category" : "the category of the word, that is, if it is a verb, a noun, etc. It should be one of the following options: 'Noun', 'Pronoun', 'Verb', 'Adjective', 'Adverb', 'Preposition', 'Conjunction', 'Interjection', 'Article', 'Determiner', 'Numeral', 'Phrase'",
    "definition": "definition of at least 25 words of the word in question, in English",
    "synonyms": "A list with at least one synonym of the word or phrase in English, separated by commas",
    "examples" : ["First example of the word usage in English","Second example of the word usage in English", "Third example of the word usage in English"]
    (closing curly brace)
    
    You should only respond with the structure described above, nothing more. If the word or phrase does not exist, then respond with a Python object with the following structure:
    
    (opening curly brace)
    "word" : "False",
    "translation" : "False",
    "category" : "False",
    "definition": "False",
    "synonyms":"False",
    "examples" : "False"
    (closing curly brace)
    
    Remember, the word or phrase is: "{phrase}"

    """
    
    llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")
    prompt_template = PromptTemplate(input_variables=["phrase"], template=template)
    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.invoke(input={
        "phrase": word,
    })
    print(response["text"])
    return json.loads(response["text"])
        
"""
while True:
    word = translate_with_llm(input("Insert a word: "))
    print(word)
"""

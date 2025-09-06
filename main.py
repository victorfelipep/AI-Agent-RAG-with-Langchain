from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#Define database path
db_path = "db"

#Define the prompt for OpenAI
prompt_template = """
Answer user questions:

{question}

based on these informations

{base_knowledge}
"""

#User question function
def ask():
    #Retrieve user question
    question = input("Write your question: ")

    #Load database
    embedding = OpenAIEmbeddings()

    db = Chroma(persist_directory=db_path,
                embedding_function=embedding
                )

    #Compare user question (embedding) with database
    results = db.similarity_search_with_relevance_scores(question, k=4)

    #Define if information in database is relevant to the question
    if len(results) == 0 or results[0][1] < 0.5:
        print("Relevant information not found on database")
        return
    #Transform relevant results in text
    result_texts = []
    for result in results:
        text = result[0].page_content
        result_texts.append(text)
        
    base_knowledge = "\n\n---\n\n".join(result_texts)
    
    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt.invoke({"question": question, "base_knowledge": base_knowledge}),
    model = ChatOpenAI()

    answer_text = model.invoke(prompt).content
    print("AI answer: ", answer_text)

ask()
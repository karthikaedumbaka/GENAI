import os
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Direct OpenAI-like call via HuggingFace Router
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key='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'
)

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b:fireworks-ai",
    messages=[
        {"role": "user", "content": "what is mean by RAG in genAi"}
    ],
)

print("Direct OpenAI-style output:", completion.choices[0].message.content)

# LangChain integration
llm = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key='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',
    model="openai/gpt-oss-20b:fireworks-ai"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
result = chain.invoke({
    "input_language": "English",
    "output_language": "German",
    "input": "I love programming."
})

print("LangChain output:", result.content)

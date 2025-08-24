from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

# Load environment variables (your OpenAI API key must be in .env file)
load_dotenv()

# Initialize ChatOpenAI model (using GPT-4o-mini here)
model = ChatOpenAI(model="gpt-4o-mini")

# Define structured schema using TypedDict
class Review(TypedDict):
    # Annotated helps give extra instructions for each field
    summary: Annotated[str, "A brief summary of review in 10 words"]
    device: str
    best_thing: Annotated[str, "Return the best thing in 1 or 2 words only"]

# Wrap the model so it always outputs data in the shape of Review
# Internally, LangChain adds a hidden system prompt + JSON parser here
structural_model = model.with_structured_output(Review)

# Normal input text (you did not give any special prompt for JSON)
result = structural_model.invoke(
    "This laptop delivers excellent performance with a sleek design. "
    "The display is crisp, battery life is reliable, and multitasking feels smooth. "
    "Ideal for both work and everyday use."
)

# Print full structured response
print(result)

# Accessing specific field from structured output
print(result["device"])


'''
Explanation:
------------
1. with_structured_output(Review)
   → LangChain secretly tells the LLM:
     "Return output as JSON with keys: summary, device, best_thing."

2. Even if you only give plain text as input,
   the model is forced to return structured JSON that matches Review.

3. Annotated[] descriptions
   → These act like field-level instructions passed to the model.
   For example:
     - summary must be short (10 words).
     - best_thing must be only 1–2 words.


{'summary': 'This laptop offers exceptional performance combined with a stylish and sleek design, making it suitable for both professional and personal use. Users will appreciate the sharp display and dependable battery life, while multitasking is seamless and efficient.', 'device': 'Laptop', 'best_thing': 'Sleek design and excellent multitasking performance.'}

'''

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Function to get the LLM response
def getLLMResponse(input_text, no_of_words, blog_style):
    # Construct the prompt template
    prompt_template = PromptTemplate(
        input_variables=["input_text", "no_of_words", "blog_style"],
        template="Write a {no_of_words} words blog on {input_text} in a {blog_style} style",
    )
    
    # Format the prompt with the input values
    prompt = prompt_template.format(input_text=input_text, no_of_words=no_of_words, blog_style=blog_style)

    try:
        # Set up the HuggingFace model endpoint
        llm = HuggingFaceEndpoint(
            repo_id="mistralai/Mistral-7B-Instruct-v0.3",
            task="text-generation",
        )
        # Generate the response
        response = llm.invoke(prompt)  # Example input for testing
        return response
    except Exception as e:
        return f"Error: {str(e)}"  # Error handling if something goes wrong

# Streamlit page configuration
st.set_page_config(page_title="LangChain with ctransformers", page_icon="☠️", layout="centered", initial_sidebar_state="collapsed")
st.header("Generate Blogs")

# Input text area for blog title
input_text = st.text_area("Enter the Blog Title")

# Layout columns for number of words and blog style
col1, col2 = st.columns(2)

with col1:
    no_of_words = st.number_input("Number of Words", min_value=1, step=1, value=100)

with col2:
    blog_style = st.selectbox('Writing the blog for', ('Research', 'Business', 'Education', 'Entertainment', 'Health', 'Technology'))

# Submit button for blog generation
submit = st.button("Generate Blog")

if submit:
    if input_text and no_of_words and blog_style:
        with st.spinner("Generating..."):
            response = getLLMResponse(input_text, no_of_words, blog_style)
            st.write(response)
    else:
        st.warning("Please fill in all the fields to generate the blog.")

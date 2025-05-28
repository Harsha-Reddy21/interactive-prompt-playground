import streamlit as st
import openai
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
st.set_page_config(
    page_title="Prompt Playground",
    page_icon="📝",
    layout="wide"
)


with st.sidebar:
    st.title("Prompt Playground")

    model = st.selectbox(
        "Select Model",
        ["gpt-3.5-turbo", "gpt-4"]
    )

    system_prompt = st.text_area(
        "System Prompt",
        "You are a professional product description writer. Write engaging and detailed product descriptions that highlight key features and benefits.",
        height=100
    )
    
    user_prompt = st.text_area(
        "User Prompt",
        "Write a detailed product description that highlights its key features and benefits.",
        height=75
    )
    
    st.subheader("Model Parameters")
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.2,
        value=0.7,
        step=0.1
    )
    
    max_tokens = st.slider(
        "Max Tokens",
        min_value=50,
        max_value=300,
        value=150,
        step=50
    )
    
    presence_penalty = st.slider(
        "Presence Penalty",
        min_value=0.0,
        max_value=1.5,
        value=0.0,
        step=1.5
    )
    
    frequency_penalty = st.slider(
        "Frequency Penalty",
        min_value=0.0,
        max_value=1.5,
        value=0.0,
        step=1.5
    )
    
    stop_sequence = st.text_input(
        "Stop Sequence",
        ""
    )

st.title("Product Description Generator")

product = st.text_input("Enter a product name (e.g., iPhone, Tesla, running shoes)", "iPhone")

if st.button("Generate"):
    full_prompt = user_prompt.format(product=product)
    params = {
        "temperature": temperature,
        "max_tokens": max_tokens,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty
    }
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_prompt}
            ],
            temperature=params["temperature"],
            max_tokens=params["max_tokens"],
            presence_penalty=params["presence_penalty"],
            frequency_penalty=params["frequency_penalty"],
            stop=stop_sequence if stop_sequence else None
        )
        result = {
            "Temperature": params["temperature"],
            "Max Tokens": params["max_tokens"],
            "Presence Penalty": params["presence_penalty"],
            "Frequency Penalty": params["frequency_penalty"],
            "Description": response.choices[0].message.content
        }
        

        st.subheader("Generated Description")
        st.markdown(f"**Parameters Used:**")
        st.markdown(f"- Temperature: {params['temperature']}")
        st.markdown(f"- Max Tokens: {params['max_tokens']}")
        st.markdown(f"- Presence Penalty: {params['presence_penalty']}")
        st.markdown(f"- Frequency Penalty: {params['frequency_penalty']}")
        st.markdown("---")
        st.markdown("**Description:**")
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"Error generating description: {str(e)}")

if st.button("Generate All"):
    full_prompt = user_prompt.format(product=product)
    parameter_combinations = [
        {
            "temperature": temp,
            "max_tokens": tokens,
            "presence_penalty": presence,
            "frequency_penalty": frequency
        }
        for temp in [0.0, 0.7, 1.2]
        for tokens in [50, 150, 300]
        for presence in [0.0, 0.5, 1.0]
        for frequency in [0.0, 0.5, 1.0]
    ]
    results = []
    for params in parameter_combinations:
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": full_prompt}
                ],
                temperature=params["temperature"],
                max_tokens=params["max_tokens"],
                presence_penalty=params["presence_penalty"],
                frequency_penalty=params["frequency_penalty"],
                stop=stop_sequence if stop_sequence else None
            )
            results.append({
                "Temperature": params["temperature"],
                "Max Tokens": params["max_tokens"],
                "Presence Penalty": params["presence_penalty"],
                "Frequency Penalty": params["frequency_penalty"],
                "Description": response.choices[0].message.content
            })
        except Exception as e:
            results.append({
                "Temperature": params["temperature"],
                "Max Tokens": params["max_tokens"],
                "Presence Penalty": params["presence_penalty"],
                "Frequency Penalty": params["frequency_penalty"],
                "Description": f"Error: {str(e)}"
            })

    # Display results in a table
    st.subheader("Generated Descriptions")
    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True)
    
    # Save all results to file
    filename = f"{product}_all_descriptions.csv"
    df.to_csv(filename, index=False)
    st.success(f"All results saved to {filename}")

    

# Interactive Prompt Playground

An interactive Streamlit application for exploring different OpenAI model parameters while generating product descriptions.

## Features

- Select between GPT-3.5-turbo and GPT-4 models
- Customize system and user prompts
- Adjust model parameters:
  - Temperature (0.0 to 1.2)
  - Max Tokens (50 to 300)
  - Presence Penalty (0.0 to 1.5)
  - Frequency Penalty (0.0 to 1.5)
- Two generation modes:
  - "Generate": Creates a single description using current parameters
  - "Generate All": Generates descriptions for all parameter combinations
- Results saved to CSV files automatically
- Clean, readable output format for single descriptions
- Comprehensive table view for multiple descriptions

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Select your preferred model (GPT-3.5-turbo or GPT-4)
2. Customize the system and user prompts
3. Adjust the model parameters using the sliders
4. Enter a product name
5. Choose between "Generate" or "Generate All" buttons
   - "Generate": Creates a single description with current parameters
   - "Generate All": Creates descriptions for all parameter combinations
6. View results in either text format (single) or table format (multiple)
7. Results are automatically saved to CSV files



## Parameter Effects

The application includes a built-in reflection section that explains how different parameters affect the output:

- Temperature: Controls creativity vs. focus
- Max Tokens: Determines description length
- Presence Penalty: Reduces topic repetition
- Frequency Penalty: Reduces word repetition

## Output Formats

- Single Description ("Generate"):
  - Clean, readable text format
  - Shows parameters used


- Multiple Descriptions ("Generate All"):
  - Comprehensive table view
  - All parameter combinations
  - Results saved to `{product}_all_descriptions.csv`



## Example

Based on the generated iPhone descriptions we can observe several interesting patterns:


1. **Temperature Impact**:
   - Lower temperatures (0.0): More consistent and focused descriptions
   - Higher temperatures (0.7-1.2): More creative and varied outputs, sometimes generating descriptions for different products
   - Temperature significantly affects the creativity and focus of the output

2. **Max Tokens Impact**:
   - 50 tokens: Very brief descriptions, often incomplete
   - 150 tokens: Balanced descriptions with key features
   - 300 tokens: More detailed descriptions with additional benefits and use cases

3. **Penalty Parameters**:
   - Presence Penalty: Minimal impact on iPhone descriptions
   - Frequency Penalty: Slightly affects word repetition but doesn't significantly change output quality
4. **Stop Sequences**:
   - It is used to stop the generation of text when a specific sequence of tokens is detected.

The analysis shows that temperature is the most influential parameter, with higher values leading to more creative but sometimes less focused outputs. The max tokens parameter directly correlates with description length and detail level. The penalty parameters have a more subtle effect on the output quality.

 -Note: The output of all combinations is saved to iPhone_all_descriptions.csv file.


# Example of synthetic dataset generation using NoisOCR
# Objective: Generate synthetic data for training a model to correct OCR errors in scanned documents

import pandas as pd
from ast import literal_eval
import random
import noisocr

df = pd.read_csv("https://raw.githubusercontent.com/lplnufpi/essay-br/main/extended-corpus/extended_essay-br.csv")

inputs = []
outputs = []

for index, row in df.iterrows():
    # Skip empty essays
    if len(row['essay']) < 5:
        continue

    # Convert array string to array

    essay = literal_eval(row['essay'][1:-1])

    print(f"Processing essay {index+1}/{len(df)}")

    lines = []

    # Split essay into lines
    for line in essay:
        lines.extend(noisocr.sliding_window_with_hyphenation(line))

    for index2, prompt in enumerate(lines):
        # Skip short prompts
        if (len(prompt) < 3):
            continue

        # Simulate OCR errors
        output = noisocr.simulate_annotation(prompt)
        text_error = noisocr.simulate_errors(output, random.randint(2, 6), seed=42)

        inputs.append(text_error)
        outputs.append(output)
        
df_output = pd.DataFrame({
    'input': input,
    'output': output,
})

# Save synthetic prompts to CSV
df_output.to_csv('synthetic_prompts.csv', index=False, header=True)

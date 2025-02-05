import json
import re

# File names
input_md_file = "manual_end.md"
output_ipynb_file = "converted_notebook.ipynb"

# Read the markdown file
with open(input_md_file, "r", encoding="utf-8") as f:
    markdown_content = f.read()

# Split the file by '---' markers
sections = re.split(r'(?m)^---$', markdown_content)

notebook = {
    "cells": [],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

# Regex to match Python code blocks
code_pattern = re.compile(r'```python\n(.*?)\n```', re.DOTALL)

for section in sections:
    section = section.strip()
    if not section:
        continue

    # Use finditer to iterate over code blocks and keep track of text segments
    last_index = 0
    for match in code_pattern.finditer(section):
        # Text before the code block becomes a markdown cell
        text_before = section[last_index:match.start()].strip()
        if text_before:
            notebook["cells"].append({
                "cell_type": "markdown",
                "metadata": {},
                "source": text_before.splitlines()
            })
        
        # Add the code block as a code cell
        code = match.group(1)
        notebook["cells"].append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": code.splitlines()
        })
        last_index = match.end()
    
    # Add any remaining text after the last code block as a markdown cell
    text_after = section[last_index:].strip()
    if text_after:
        notebook["cells"].append({
            "cell_type": "markdown",
            "metadata": {},
            "source": text_after.splitlines()
        })

# Write the resulting notebook to file
with open(output_ipynb_file, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=4)

print(f"Notebook saved as {output_ipynb_file}")

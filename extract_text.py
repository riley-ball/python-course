import nbformat
from nbconvert import MarkdownExporter

def get_notebook_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, nbformat.NO_CONVERT)
    
    exporter = MarkdownExporter()
    body, _ = exporter.from_notebook_node(notebook)
    
    return body

# Specify the path to your Jupyter Notebook file
notebook_file = "course_structure.ipynb"

# Specify the path to the output text file
output_file = "output.txt"

# Get the text from the Jupyter Notebook file
notebook_text = get_notebook_text(notebook_file)

# Write the extracted text to the output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(notebook_text)

print("Text extracted from the Jupyter Notebook has been written to the output file.")

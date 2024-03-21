# Importing necessary libraries
import streamlit as st
from Bio import SeqIO
from Bio.Seq import Seq
import io
#----------------------------
from PIL import Image
import requests
from io import BytesIO
import streamlit as st

# Computing GC sequence content (%)
def compute_gc(file_content):
    try:
        # Using StringIO to convert string content into a file-like object
        records = list(SeqIO.parse(io.StringIO(file_content), "fasta"))
        if not records:
            return "No sequences found in the file."
        
        # Extract header info.
        header = records[0].description
        sequence = records[0].seq
        gc_content = 100 * float(sequence.count("G") + sequence.count("C")) / len(sequence)
        
        # Return header and GC content
        return f"{header}\nGC-content: {gc_content:.2f}%"
    except Exception as e:
        return f"An error occurred: {e}"
    
# App title and instructions
st.title('GC-Content Calculator')
st.write('Upload a sequence in FASTA format. Click [here](https://www.ncbi.nlm.nih.gov/datasets/genome/) to download a FASTA file.')

# Manual input textbox
st.subheader('Enter Sequence')
sequence_input = st.text_area("", height=150)
calculate_button = st.button('Calculate')

# Browse a file
st.subheader('Or Upload a File')
uploaded_file = st.file_uploader("Choose file", type=['fa', 'fasta', 'txt'])

# Handling manual entries
if calculate_button:
    if sequence_input:
        gc_content = compute_gc(">Manual Input\n" + sequence_input)
        st.write(gc_content)
    else:
        st.write("Please enter a sequence.")

# Handling file upload
if uploaded_file is not None:
    # Read the contents of the file
    file_content = uploaded_file.getvalue().decode("utf-8")
    gc_content = compute_gc(file_content)
    st.write(gc_content)

######################

# URL of the image
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/CD28_structure.gif/250px-CD28_structure.gif"

# Fetch the image
response = requests.get(image_url)
if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
    st.image(image, caption='CD28 Structure')
else:
    st.error("Failed to load image.")
    
# Displaying the GIF
st.subheader('CD28 Structure')
gif_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/CD28_structure.gif/250px-CD28_structure.gif"
response = requests.get(gif_url)
image = Image.open(BytesIO(response.content))
st.image(image, caption='CD28 Molecular Structure')

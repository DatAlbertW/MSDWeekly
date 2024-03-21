# Importing necesary libraries
import streamlit as st
from Bio import SeqIO
from Bio.Seq import Seq
import io

# Computing GC sequence content (%)
def compute_gc(file):
    try:
        records = list(SeqIO.parse(file, "fasta"))
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
st.title('GC-Content')
st.write('Upload a sequence in FASTA format. Click [here](https://www.ncbi.nlm.nih.gov/datasets/genome/) to download FASTA file.')

# Manual input teztbox
st.subheader('Enter Sequence')
sequence_input = st.text_area("", height=150)
calculate_button = st.button('Calculate')

# Browse a file
st.subheader('Or Upload a File')
uploaded_file = st.file_uploader("Choose file", type=['fa', 'fasta', 'txt'])

# Handling manual entries
if calculate_button:
    if sequence_input:
        gc_content = compute_gc(io.StringIO(">Manual Input\n" + sequence_input))
        st.write(gc_content)
    else:
        st.write("Please enter a sequence.")

# Handling file upload
if uploaded_file is not None:
    gc_content = compute_gc(uploaded_file)
    st.write(gc_content)

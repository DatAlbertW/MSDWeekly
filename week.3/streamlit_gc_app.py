# Importing necessary libraries
import streamlit as st
from Bio import SeqIO
from Bio.Seq import Seq
import io

# Computing GC sequence content (%)
def compute_gc(file):
    try:
        records = list(SeqIO.parse(file, "fasta"))
        if not records:
            return ("No sequences found in the file.", None)

        # Extract header info and sequence
        header = records[0].description
        sequence = records[0].seq
        gc_content = 100 * float(sequence.count("G") + sequence.count("C")) / len(sequence)

        # Return header and GC content
        return header, gc_content
    except Exception as e:
        return (f"An error occurred: {e}", None)

# App title and instructions
st.title('GC Content Calculator')
st.write('Upload a sequence in FASTA format or enter it manually. Download FASTA files from [NCBI Genome](https://www.ncbi.nlm.nih.gov/datasets/genome/).')

# Display the GIF
st.image("week.3/250px-CD28_structure.gif", caption="CD28 Structure")

# Manual input textbox
st.subheader('Enter Sequence')
sequence_input = st.text_area("", height=150)
calculate_button = st.button('Calculate')

# Browse a file
st.subheader('Or Upload a File')
uploaded_file = st.file_uploader("Choose file", type=['fa', 'fasta', 'txt'])

# Handling manual entries
if calculate_button and sequence_input:
    header, gc_content = compute_gc(io.StringIO(">Manual Input\n" + sequence_input))
    if gc_content is not None:
        st.write(f"**Sequence Header:**\n{header}")
        st.write(f"**GC Content:** {gc_content:.2f}%")

# Handling file upload
if uploaded_file is not None:
    header, gc_content = compute_gc(uploaded_file)
    if gc_content is not None:
        st.write(f"**Sequence Header:**\n{header}")
        st.write(f"**GC Content:** {gc_content:.2f}%")

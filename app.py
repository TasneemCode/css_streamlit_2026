import streamlit as st
import time


t1, t2, t3 = st.tabs(["Introduction", "Research", "Contact"])

with t1:
    with st.empty():
        st.title("Hello, I'm Tasneem Ismail!")
        time.sleep(4)
        st.header("Welcome to my page")
        time.sleep(4)
        st.title('''A bit about me...\n 
        I completed my undergrad and Honours at UCT.
        Undergrad: BSc in Computer Science and Genetics
        Honours: Molecular & Cell Biology 
        The simplest way to describe my research interest: Computational Drug Discovery & Design. 
        Would you like to hear about my Honours research project?''')
        st.feedback("thumbs")

with t2:
    st.title("My Research")
    st.header("Background")
    st.write("Candida auris, network analysis, Mutation-Minimisation (MuMi)")
    st.header("Workflow")
    st.write("WT processing & minimization --> Mutant generation & Minimization --> Analysis")
    st.header("Results")
    st.write("Top effective residues and pathways")

with t3:
    st.title('''Have any questions?
    Contact me at tasneem.ismail2003@gmail.com
             ''')

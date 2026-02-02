import streamlit as st

st.title("Where IT meets biology")
t1, t2, t3 = st.tabs(["Introduction", "Research", "Contact"])

with t1:
    st.title("Hello, I'm Tasneem Ismail! Welcome to my researcher profile!")
    st.header(":red[A bit about me...]")

    with st.expander(":red[Qualifications]"):
        st.markdown('''I completed my undergrad and Honours at UCT.\n
Undergrad: :red[BSc in Computer Science and Genetics]\n
Honours: :red[Molecular & Cell Biology]''')
    
    with st.expander(":red[My Research Interests]"):
        st.markdown('''Software engineering\n
Bioinformatics\n
Computational Drug Discovery & Design''')
        st.image("md1.png")
    
    with st.expander(":red[Skills]"):
        st.markdown('''
1. Programming languages: 
   :red[Python, R, Java, JavaScript, SQL, HTML, CSS]

2. Full-stack development with :red[Flask, SQL and React]

3. Technical environment proficiency:
   :red[WSL, UBUNTU, VS CODE, CHPC, Git]

4. DNA and Protein sequence alignment

5. 3D protein modelling:
   :red[PyMOL, MODELLER, GROMACS, CHARMM-GUI, AUTODOCK]

6. Data analysis with :red[R, Python and Bash scripts]

7. Wet-lab techniques: 
   :red[DNA, RNA, and protein purification and quantification]''') 

with t2:
    st.title("My Research")
    with st.expander(":red[Background]"):
        st.markdown('''
:red[Candida auris] is a recently emergent fungal pathogen.
It has displayed resistance to all current classes of antifolate drugs which are orthosteric.
To counter this deadly pathogen, new classes of antifungal drugs need to be discovered.
:red[Allosteric regulation] can be studied to identify new drug targets.
Computational methods can speed up the drug discovery process.
:red[Network Analysis] is a computational method used to map allosteric networks to identify new drrug targets.''')
        
    with st.expander(":red[Mutation-Minimisation (MuMi)]"):
        st.markdown(''':red[Energy-minimization:]
Reach the most stable protein conformation by applying forces to proteins in a simulated environment.

:red[Alanine-Scanning for Mutagenesis (Mutant Generation):]
Mutate every single amino acid residue to alanine one at a time, generating single-alanine mutants

:red[Linear Algebra:]
Store C-alplha atom coordinates in matrices for wildtype-mutant comparisons

:red[Network Analysis:]
Represent proteins as networks of nodes and edges to identify key pathways in protein function

:red[Molecular Dynamic Simulations:]
Simulate the movement of proteins in an enivironment to identify normal protein movement

:red[Computational Ligand Design]
Use the properties of proteins to design drugs that will bind to the protein selectively and efficiently.''')


with t3:
    st.title("Have any questions?")
    st.info(''':red[Contact me at tasneem.ismail2003@gmail.com]
             ''')


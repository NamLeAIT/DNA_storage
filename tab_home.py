import streamlit as st

def render_home():
    st.title("Welcome to DNA Data Storage Project")
    st.caption("End-to-end, headerless DNA storage workflow with domain-aware compression and sequencing-aware mapping.")

    hero = st.container(border=True)
    with hero:
        col1, col2 = st.columns([1.25, 1.0], gap="large")
        with col1:
            st.markdown(
                """
                #### Exploring the Future of Data Storage
                This system transforms digital files into a **single DNA string** suitable for synthesis and sequencing-based retrieval.

                **Key process**
                1. **Encoding:** Binary → DNA mapping rules
                2. **Optimization:** GC / homopolymer constraints
                3. **Decoding:** DNA → original file (integrity-checked)
                """
            )
        with col2:
            st.image("endtoend.jpg", caption="DNA Data Storage: End-to-end System Overview", use_container_width=True)

    st.divider()

    wf = st.container(border=True)
    with wf:
        st.subheader("🧬 Indicated Workflow")
        st.caption("Digital data → DNA synthesis → sequencing → decoding (end-to-end).")
        st.image(
            "workflow.jpg",
            caption="End-to-End DNA Data Storage Workflow: Encoding, Wet-lab, and Decoding",
            use_container_width=True,
        )

    st.info(
        "This workflow supports robust retrieval via integrity checks and biological constraint-aware mapping."
    )

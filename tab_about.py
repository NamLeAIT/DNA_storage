import streamlit as st

def render_about():
    st.title("About the DNA Data Storage System")
    st.caption("Research-grade, end-to-end DNA storage with robust encoding, biological constraints, and reliable retrieval.")

    overview = st.container(border=True)
    with overview:
        st.subheader("System Overview")
        st.markdown(
            """
            - **Objective:** Develop an end-to-end system for high-density, long-term DNA data storage with robust encoding,
              error correction, and reliable data retrieval.
            - DNA stores information as a sequence of four bases (A/C/G/T). This project treats DNA as a storage medium by
              mapping digital data to base sequences, applying integrity checks and biologically informed constraints, and
              enabling decoding back to the original file.
            """
        )

    st.divider()

    members = st.container(border=True)
    with members:
        st.subheader("Members and Contact")
        st.write("If you have questions or feedback, please contact:")

        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown(
                """
                **Prof. Sung Ha Park**  
                Principal Investigator  
                Email: sunghapark@skku.edu  
                Phone: 010-xxxx-xxxx
                """
            )
        with c2:
            st.markdown(
                """
                **Dr. Dinosaur N.K.U**  
                App Developer  
                Email: kimuyendlu@gmail.com  
                Phone: 010-xxxx-xxxx
                """
            )

    st.divider()

    loc = st.container(border=True)
    with loc:
        st.subheader("Location")
        st.markdown(
            """
            **Address:** Department of Physics, Sungkyunkwan University  
            2066, Seobu-ro, Jangan-gu, Suwon, Gyeonggi-do, 16419, Republic of Korea
            """
        )

        map_html = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3171.303975005891!2d126.97210167637823!3d37.2938883394593!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x357b56b21761867f%3A0xb38ea754e92d9bb0!2sSungkyunkwan%20University%20(Natural%20Sciences%20Campus)!5e0!3m2!1sen!2skr!4v1700000000000!5m2!1sen!2skr"
    width="100%"
    height="430"
    style="border:0; border-radius: 14px;"
    allowfullscreen=""
    loading="lazy"
    referrerpolicy="no-referrer-when-downgrade">
</iframe>
"""
        st.components.v1.html(map_html, height=480)

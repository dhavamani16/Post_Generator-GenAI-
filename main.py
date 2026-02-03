import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post



length_options = ["Short", "Medium", "Long"]
language_options = ["English", "English"]

def main():
    st.subheader("LinkedIn Post Generator: Codebasics")

    
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
    
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        
        selected_language = st.selectbox("Language", options=language_options)

    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.write(post)

if __name__ == "__main__":
    main()

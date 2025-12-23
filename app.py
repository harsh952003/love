import streamlit as st

st.set_page_config(page_title="Ask Her Out", page_icon="❤️")

# Function to read HTML files
def get_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# HTML content for each page
index_html = get_html('templates/index.html')
yes_html = get_html('templates/yes.html')
no1_html = get_html('templates/no1.html')
no2_html = get_html('templates/no2.html')
no3_html = get_html('templates/no3.html')

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Display current page
if st.session_state.page == 'home':
    st.markdown(index_html, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Yes', key='yes_home'):
            st.session_state.page = 'yes'
            st.rerun()
    with col2:
        if st.button('No', key='no_home'):
            st.session_state.page = 'no1'
            st.rerun()

elif st.session_state.page == 'yes':
    st.markdown(yes_html, unsafe_allow_html=True)
    if st.button('Start Over'):
        st.session_state.page = 'home'
        st.rerun()

elif st.session_state.page == 'no1':
    st.markdown(no1_html, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Yes', key='yes_no1'):
            st.session_state.page = 'yes'
            st.rerun()
    with col2:
        if st.button('No', key='no_no1'):
            st.session_state.page = 'no2'
            st.rerun()

elif st.session_state.page == 'no2':
    st.markdown(no2_html, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Yes', key='yes_no2'):
            st.session_state.page = 'yes'
            st.rerun()
    with col2:
        if st.button('No', key='no_no2'):
            st.session_state.page = 'no3'
            st.rerun()

elif st.session_state.page == 'no3':
    st.markdown(no3_html, unsafe_allow_html=True)
    if st.button('Yes', key='yes_no3'):
        st.session_state.page = 'yes'
        st.rerun()
    st.markdown('<p style="color: red; font-size: 1.5rem;">No more "No" options! 😜</p>', unsafe_allow_html=True)
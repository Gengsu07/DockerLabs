import streamlit as st

st.title('COBA DOCKER STREAMLIT')

a,d,f = st.columns(3)
with a:
    st.header('ini kolom 1 kiri')
with d:
    st.header('ini kolom tengah')
    
with f:
    st.header('ini kolom kanan')
  
with st.expander(label='Buka engga ya'):
    st.write('In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available.')
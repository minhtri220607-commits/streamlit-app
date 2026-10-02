import streamlit as st

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀"
)

st.title("My First Streamlit App")

st.write("Xin chào! Đây là ứng dụng Streamlit đầu tiên của tôi.")

name = st.text_input("Bạn tên gì?")

if name:
    st.success(f"Xin chào {name}! 👋")

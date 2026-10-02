import streamlit as st

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀"
)

st.title("My First Streamlit App")
st.write("Xin chào! Đây là ứng dụng Streamlit đầu tiên của tôi.")

# Tạo một form (biểu mẫu) độc lập
with st.form("my_form"):
    name = st.text_input("Bạn tên gì?")
    
    # Nút bấm bắt buộc phải có trong form để gửi dữ liệu đi
    submitted = st.form_submit_button("Xác nhận")
    
    if submitted and name:
        st.success(f"Xin chào {name}! 👋")

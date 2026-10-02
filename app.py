import streamlit as st

# 1. Cấu hình trang web của tiệm
st.set_page_config(
    page_title="Hệ Thống Tính Tiền Trà Sữa",
    page_icon="🧋",
    layout="centered"
)

st.title("🧋 Hệ Thống Tính Tiền Trà Sữa")
st.write("Ứng dụng quản lý gọi món và tính tiền nhanh cho nhân viên.")

# 2. Định nghĩa Menu món và giá tiền (Bạn có thể tự sửa tên món và giá ở đây)
MENU_MON = {
    "Trà sữa truyền thống": 25000,
    "Trà sữa Thái xanh": 28000,
    "Trà sữa Ô long": 30000,
    "Sữa tươi trân châu đường đen": 35000,
    "Trà đào cam sả": 32000,
    "Trà trái cây nhiệt đới": 35000
}

MENU_TOPPING = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 6000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese (Macchiato)": 8000
}

# Sử dụng Form để gom toàn bộ quá trình gọi món
with st.form("pos_form"):
    st.subheader("📋 Chi tiết đơn hàng")
    
    # Chọn món chính và số lượng
    col1, col2 = st.columns([3, 1])
    with col1:
        mon_da_chon = st.selectbox("Chọn loại nước uống:", list(MENU_MON.keys()))
    with col2:
        so_luong = st.number_input("Số lượng:", min_value=1, max_value=20, value=1)
        
    # Chọn các loại Topping đi kèm (cho phép chọn nhiều loại cùng lúc)
    topping_da_chon = st.multiselect("Thêm Topping (Tùy chọn):", list(MENU_TOPPING.keys()))
    
    # Ghi chú thêm (Ví dụ: 50% đá, 100% đường...)
    ghi_chu = st.text_input("Ghi chú đơn hàng (Ví dụ: Ít đá, nhiều đường...):")
    
    # Nút bấm tính tiền
    nut_tinh_tien = st.form_submit_button("💰 Tính Tiền & Xuất Hóa Đơn")

# 3. Xử lý logic tính tiền khi bấm nút
if nut_tinh_tien:
    # Tính giá tiền món chính
    gia_mon_chinh = MENU_MON[mon_da_chon] * so_luong
    
    # Tính tổng giá tiền của các topping đã chọn
    gia_topping = sum([MENU_TOPPING[tp] for tp in topping_da_chon]) * so_luong
    
    # Tổng cộng hóa đơn
    tong_tien = gia_mon_chinh + gia_topping
    
    # Hiển thị hóa đơn ra màn hình
    st.success("### 🧾 HÓA ĐƠN TẠM TÍNH")
    
    # Tạo bảng hiển thị thông tin chi tiết bằng Markdown
    st.markdown(f"**Tên món:** {mon_da_chon} x {so_luong}")
    
    if topping_da_chon:
        st.markdown(f"**Topping đi kèm:** {', '.join(topping_da_chon)}")
    else:
        st.markdown("**Topping:** Không có")
        
    if ghi_chu:
        st.markdown(f"**Yêu cầu thêm:** *{ghi_chu}*")
        
    st.markdown("---")
    st.markdown(f"### 💵 Tổng thanh toán: **{tong_tien:,} VNĐ**")


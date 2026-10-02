import streamlit as st

# 1. Cấu hình trang web của tiệm
st.set_page_config(
    page_title="Hệ Thống Tính Tiền Trà Sữa",
    page_icon="🧋",
    layout="centered"
)

st.title("🧋 Hệ Thống Tính Tiền Trà Sữa")
st.write("Ứng dụng quản lý gọi món và tính tiền nhanh cho nhân viên.")

# 2. Danh sách Menu món và giá tiền
MENU_MON = {
    "Trà sữa truyền thống": 25000,
    "Trà sữa Thái xanh": 28000,
    "Trà sữa Ô long": 30000,
    "Sữa tươi trân châu đường đen": 35000,
    "Trà đào cam sả": 32000,
    "Trà trái cây nhiệt đới": 35000,
    "Hồng trà vải thiều": 30000,
    "Trà sữa full topping": 45000
}

# Cấu hình giá cộng thêm theo Size
MENU_SIZE = {
    "Size S": 0,
    "Size M": 5000,
    "Size L": 10000,
    "Size XL": 15000
}

# Danh sách Topping phong phú (Đã thêm Bánh flan)
MENU_TOPPING = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 6000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese (Macchiato)": 8000,
    "Thạch dừa": 5000,
    "Trân châu ngũ sắc": 7000,
    "Hạt thủy tinh củ năng": 8000,
    "Trân châu matcha phô mai": 9000,
    "Chân mèo": 8000,
    "Khúc bạch": 7000,
    "Phô mai mặn": 8000,
    "Phô mai tươi": 9000,
    "Bánh flan": 7000                    # Topping mới thêm
}

# Cập nhật danh sách các mức đường và đá đồng bộ theo yêu cầu
MUC_DUONG = ["100% đường", "70% đường", "50% đường", "30% đường", "0% đường"]
MUC_DA = ["100% đá", "70% đá", "50% đá", "30% đá", "0% đá"]

# Sử dụng Form để gom quá trình gọi món
with st.form("pos_form"):
    st.subheader("📋 Chi tiết đơn hàng")
    
    # Dòng 1: Chọn món và Số lượng
    col1, col2 = st.columns(2)
    with col1:
        mon_da_chon = st.selectbox("Chọn loại nước uống:", list(MENU_MON.keys()))
    with col2:
        so_luong = st.number_input("Số lượng (ly):", min_value=1, max_value=50, value=1)
        
    # Dòng 2: Chọn Size và Chọn mức đường
    col3, col4 = st.columns(2)
    with col3:
        size_da_chon = st.selectbox("Chọn Size:", list(MENU_SIZE.keys()), index=1) # Mặc định chọn Size M
    with col4:
        duong_da_chon = st.selectbox("Chọn mức đường:", MUC_DUONG)
        
    # Dòng 3: Chọn mức đá và Ghi chú thêm
    col5, col6 = st.columns(2)
    with col5:
        da_da_chon = st.selectbox("Chọn mức đá:", MUC_DA)
    with col6:
        ghi_chu = st.text_input("Ghi chú khác (Ví dụ: Mang đi, chia ly...):")
    
    # Dòng 4: Chọn các loại Topping đi kèm
    topping_da_chon = st.multiselect("Thêm Topping (Tùy chọn):", list(MENU_TOPPING.keys()))
    
    # Nút bấm tính tiền
    nut_tinh_tien = st.form_submit_button("💰 Tính Tiền & Xuất Hóa Đơn")

# 3. Xử lý logic tính tiền khi bấm nút
if nut_tinh_tien:
    # Lấy giá gốc món chính
    gia_goc = MENU_MON[mon_da_chon]
    
    # Lấy tiền cộng thêm của Size
    tien_size = MENU_SIZE[size_da_chon]
    
    # Tính tổng giá tiền của các topping đã chọn
    gia_topping = sum([MENU_TOPPING[tp] for tp in topping_da_chon])
    
    # Tổng cộng tiền của 1 ly
    tien_mot_ly = gia_goc + tien_size + gia_topping
    
    # Tổng hóa đơn cho toàn bộ số lượng ly
    tong_tien = tien_mot_ly * so_luong
    
    # Hiển thị hóa đơn ra màn hình
    st.success("### 🧾 HÓA ĐƠN TẠM TÍNH")
    
    # Hiển thị thông tin chi tiết bằng Markdown
    st.markdown(f"**Món chính:** {mon_da_chon} (**{size_da_chon}**) x {so_luong}")
    st.markdown(f"**Tùy chọn:** {duong_da_chon} | {da_da_chon}")
    
    if topping_da_chon:
        st.markdown(f"**Topping đi kèm:** {', '.join(topping_da_chon)}")
    else:
        st.markdown("**Topping:** Không có")
        
    if ghi_chu:
        st.markdown(f"**Yêu cầu thêm:** *{ghi_chu}*")
        
    st.markdown("---")
    # Hiển thị chi tiết cách tính tiền
    st.caption(f"Chi tiết: ({gia_goc:,} món + {tien_size:,} size + {gia_topping:,} topping) x {so_luong} ly")
    st.markdown(f"### 💵 Tổng thanh toán: **{tong_tien:,} VNĐ**")

        
    st.markdown("---")
    st.markdown(f"### 💵 Tổng thanh toán: **{tong_tien:,} VNĐ**")


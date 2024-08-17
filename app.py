import streamlit as st
from PIL import Image

def txt(a):  # 1 column - paragraph
    _, col, _ = st.columns((1,3,1))
    with col:
        st.markdown(a)

def txt1(a, b):  # 2 columns with offset to the left (2:1)
  _, col1, col2, _ = st.columns([1,2,1,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):  # 2 columns with offset to the right (1:2)
  _, col1, col2, _ = st.columns([1,1,2,1])
  with col1:
    st.markdown(f'`{a}`')  # highlight text
  with col2:
    st.markdown(b)

def txt3(a, b):  # 2 columns with offset to the right (1:2)
  _, col1, col2, _ = st.columns([1,1,2,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c): # 3 columns
  _, col1, col2, _, col3, _ = st.columns([1,0.65,1.5, 0.1,0.75,1])
  with col1:
    st.markdown(f'`{a}`')  # highlight text
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

st.set_page_config(page_title='Trần Duy Hoàng - Portfolio',page_icon="☀", layout="wide")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
image = Image.open('./image/my_portrait.jpg')
header_img,header_title,_ = st.columns((1,2,1))
header_img.image(image, width = 200)
header_title.write('''





    
    # TRẦN DUY HOÀNG
    ##### Business Intelligence - Data Analyst
    ''')
tab1, tab2, tab3 = st.tabs(["    About me", "    My Projects", "    References"])
with tab1:
    txt2('April 2024 - now','Chuyên gia Quản trị hiệu quả vận hành')
    txt2('','#Ngân hàng TMCP Kỹ thương Việt Nam')
    txt2('May 2022 - Mar 2024','Chuyên viên cao cấp Quản trị hiệu quả vận hành')
    txt2('Jul 2020 - Apr 2022','Chuyên viên Thanh toán & Tài trợ thương mại')

with tab2:
    col1,col2,col3,_ = st.columns([3,3,3,1])
    with col1:
        st.write('## Phân tích & cải tiến chất lượng')
        st.markdown("Domain: :blue-background[Trade Finance] :blue-background[Loans]")
        con11 = st.container(border=True)
        con11.write('### Dịch vụ vận hành')

        con12 = st.container(border=True)
        con12.write('### Tuân thủ & văn hóa trải nghiệm')
        
    with col2:
        st.write('## Giám sát rủi ro hoạt động')
        st.markdown("Domain: :blue-background[Trade Finance] :blue-background[Loans]")
        con2 = st.container(border=True)
        con2.write('### Sản phẩm LC')
    with col3:
        st.write('## Tự động hóa quy trình')
        st.markdown("Domain: :blue-background[Trade Finance] :blue-background[Loans] :blue-background[Collections] :blue-background[Credit Cards Telesales]")
        con31 = st.container(border = True)
        con31.write('### Tác nghiệp thu nợ tại hiện trường')

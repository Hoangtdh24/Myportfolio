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

def myprj_thumbnail(title,domains,description,tools,skills):
    ctn = st.container(border=True)
    ctn.write(f'#### {title}')
    ctn.markdown('Domain: '+' '.join([f':blue-background[{i}]' for i in domains]))
    ctn.markdown(description)
    ctn.markdown('Tools: '+' '.join([f':orange-background[{i}]' for i in tools]))
    ctn.image(image,width =150)

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
        st.write('## Phân tích & cải tiến')
        con11 = st.container(border=True)
        con11.write('#### Dịch vụ vận hành')
        con11.markdown("Domain: :blue-background[International Payment] :blue-background[Trade Finance]")
        con11.markdown('''*Hoạt động vận hành tại các đơn vị hội sở và chi nhánh được kiểm soát thường xuyên thông qua phân tích dữ liệu xử lý giao dịch.  
        Phân tích chuyên sâu các chỉ số rời rạc (FTR/SLA/TAT) nhằm cải thiện trải nghiệm khách hàng.  
        Kể câu chuyện về trải nghiệm khách hàng về chất lượng dịch vụ thông qua mô hình RFM, qua quan sát hành trình khách hàng.*''')
        con11.markdown("Tools: :orange-background[Oracle DWH] :orange-background[DataBricks] :orange-background[OBIEE] :orange-background[PowerBI] :orange-background[Excel]")
        con11.image(image,width =150)

        con12 = st.container(border=True)
        con12.write('#### Tuân thủ chính sách nhân sự & văn hóa trải nghiệm')
        con12.markdown('''*Phân tích hành vi tuân thủ giờ làm việc của CBNV toàn hàng, phát hiện hành vi không tốt của một bộ phận CBNV.  
        Báo cáo kết quả tham gia hoạt động văn hóa tổ chức.*''')

        con13 = st.container(border = True)
        con13.write('#### Follow kích hoạt và chi tiêu thẻ tín dụng')
    
    with col2:
        st.write('## Giám sát rủi ro hoạt động')
        st.markdown("Domain: :blue-background[Trade Finance] :blue-background[Loans]")
        con2 = st.container(border=True)
        con2.write('#### Sản phẩm LC')
    with col3:
        st.write('## Tự động hóa quy trình')
        st.markdown("Domain: :blue-background[Trade Finance] :blue-background[Loans] :blue-background[Collections] :blue-background[Credit Cards Telesales]")
        con31 = st.container(border = True)
        con31.write('#### Tác nghiệp thu nợ tại hiện trường')
        con31.markdown('''*Cán bộ thu nợ tại hiện trường ghi nhận vị trí tác nghiệp, kết quả tác nghiệp hoặc điều chỉnh kế hoạch tác nghiệp một cách nhanh chóng và di động.  Giám đốc thu hồi nợ có thể giám sát kết quả trực tiếp và thường xuyên.
        *''')
        con32 = st.container(border = True)
        con32.write('#### Tác nghiệp chuyển tiền quốc tế ghi nhận kết quả xử lý ngoại lệ cho khách hàng')
        con32.markdown('''*CV/CVCC trong quá trình tác nghiệp được trao quyền xử lý ngoại lệ, cần gọi điện cho KH và lưu thông tin cuộc gọi*''')

        con33 = st.container(border = True)
        con33.write('#### Đối chiếu số dư trên tài khoản trung gian')
        con33.markdown('''*Công cụ xử lý hàng triệu dòng dữ liệu để đối chiếu giao dịch.*''')

        con34 =st.container(border = True)
        con34.write('#### Gửi thông báo nghĩa vụ tài chính/phi tài chính cho khách hàng')
        con34.markdown('''*Tổng hợp dữ liệu nghĩa vụ của khách hàng, tự động gửi mail thông báo định kỳ:  
        + Nghĩa vụ tài chính: thanh toán gốc/lãi vay, thanh toán BCT theo LC, lãi/phí LC UPAS, phí bảo lãnh, phí định giá lại, phí tái tục bảo hiểm tài sản...  
        + Nghĩa vụ phi tài chính: nghĩa vụ bổ sung nợ chứng từ*''')

        myprj_thumbnail('abv',['d','e','f'],'*sao lại.  không.  xuống dòng.*',['a','b'],['a'])
        myprj_thumbnail('abc',['d','e','f'],'*sao lại.  không.  xuống dòng.*',['a','b'],['a'])


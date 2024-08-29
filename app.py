import streamlit as st
from PIL import Image
#Version2---------------------------------------------------------------------------------
st.set_page_config(page_title='Trần Duy Hoàng - Portfolio',page_icon=":material/badge:", layout="wide")

def w_hocvan(v_hinhthuc, v_truong, v_nganh, v_ketqua, v_tgian, v_kynang):  # 2 columns with offset to the right (1:2)
  col1, col2, col3, col4,col5 = st.columns([1.5,5,1.5,1,1])
  with col1:
    st.markdown(v_hinhthuc)
  with col2:
    st.markdown(f'**{v_nganh}**') 
    st.markdown(f'*{v_truong}*')
  with col3:
    for item in v_kynang:
      st.markdown(f':red-background[{item}]')
  with col4:
    st.markdown(f':blue-background[{v_ketqua}]')
  with col5:
    st.markdown(v_tgian)

def w_lamviec(v_cty,v_vitri,v_nhiemvu,v_ketqua,v_kynang,v_thanhtich,v_tgian):
  col1, col2, col3, col4,col5 = st.columns([1.5,5,1.5,1,1])
  with col1:
    st.markdown(f'**{v_vitri}**') 
    st.markdown(f'*{v_cty}*')
  with col2:
    st.markdown('***Nội dung công việc***')
    for item in v_nhiemvu:
      st.markdown(item)
    st.markdown('***Sản phẩm & ý nghĩa***')
    for item in v_ketqua:
      st.markdown(item)
  with col3:
    for item in v_kynang:
      st.markdown(f':red-background[{item}]')
  with col4:
    st.markdown(f':blue-background[{v_thanhtich}]')
  with col5:
    st.markdown(v_tgian)
    
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

_,header_name,_ = st.columns([1,2,1],vertical_alignment = "center")
header_name.write('# Trần Duy Hoàng')
header_name.write('##### SENIOR DATA ANALYTICS - EXPERT BUSINESS INTELLIGENCE')
_,inf_phone,inf_mail,inf_linkedin,inf_address,_ = st.columns([1,2,2,2,2,1],vertical_alignment ='center')
with inf_phone:
    st.info('097 879 8348',icon = ":material/phone_in_talk:")
with inf_mail:
    st.info('hoangtdh24@gmail.com',icon = ":material/mail:")
with inf_linkedin:
    st.info('linkedin.com/hoangtdh24',icon = ":material/link:")
with inf_address:
    st.info('Hà Đông, Hà Nội',icon = ":material/location_on:")

st.header('MỤC TIÊU NGHỀ NGHIỆP',divider ='gray')
st.markdown('Trở thành chuyên gia về phân tích dữ liệu và khoa học dữ liệu')
st.header('HỌC VẤN & CHỨNG CHỈ',divider ='gray')
w_hocvan("Đại học chính quy","Đại học Ngoại thương","Kinh tế đối ngoại","Xuất sắc","2016-2020",["Hoạt động kinh doanh","Nghiệp vụ ngoại thương"])
w_hocvan("THPT","THPT Chuyên Thái Bình","Chuyên Toán","Giải nhì VMO 2016","2013-2016",[])
w_hocvan("Chứng chỉ","Trường Công nghệ thông tin Truyền thông - Đại học Bách khoa Hà Nội","Phân tích định lượng","","2021",["Quantity analytics","R","Python"])
w_hocvan("Chứng chỉ","HackerRank","SLQ Skill (Advanced)","","2022",["PLSQL","SQLLite","MySQL"])
w_hocvan("Chứng chỉ","Great Learning","Visualizing Data with Microsoft Power BI","","2022",["PowerBI","Data Story Telling"])
w_hocvan("Chứng chỉ","Databricks","Databricks Lakehouse Fundamentals","","2024",["Databricks","Spark"])
w_hocvan("Chứng chỉ","Doodle Design","Design Thinking","","2024",[])
st.header('KINH NGHIỆM LÀM VIỆC',divider ='gray')
w_lamviec("Techcombank","Chuyên gia Giám sát chất lượng Dịch vụ vận hành"
          ,["+ Giám sát chất lượng dịch vụ thông qua lắng nghe trực tiếp phản hồi từ khách hàng & các phân tích sâu về hành trình khách hàng"
            ,"+ Tư vấn giải pháp tự động hóa, nâng cao năng lực xử lý dữ liệu tới các bộ phận khác"
            ,"+ Triển khai chuyển đổi các sản phẩm từ DWH sang Datalake/Lakehouse với Databricks."]
          ,["+ Xây dựng ma trận giao dịch có vấn đề, nhận diện và đưa khách hàng vào mẫu khảo sát nhằm lắng nghe ý kiến khách hàng có trải nghiệm không tốt để khắc phục và cải tiến"
             ,"+ Dashboard hành vi KHDN và chất lượng dịch vụ của ngân hàng từ góc độ khách hàng, xây dựng bộ ngưỡng cảnh báo phối hợp giữa các chỉ số chất lượng dịch vụ & các chỉ số tài chính"
             ,"+ Tổ chức khóa học PowerApps & tư vấn logic cho các đơn vị xây dựng App quản lý hoạt động văn hóa, App quản lý nhân tài, App đào tạo; Xây dựng báo cáo hoạt động văn hóa toàn hàng & báo cáo tuân thủ thời gian làm việc tại HO (~12k user sử dụng)"
             ,"+ Hỗ trợ tự động hóa hoạt động của đơn vị Tetesales sản phẩm vay KHCN thông qua báo cáo tự động: báo cáo lịch sử tương tác & trạng thái giao dịch của khách hàng, ma trận khuyến nghị về chiến dịch cần thực hiện giúp thay thế việc tra cứu thủ công và tối ưu hiệu quả bán."
             ,"+ ~ 130 rules giám sát rủi ro hoạt động KHDN: mở tài khoản, phát vay, bảo lãnh, tài sản, hạn mức, chuyển tiền quốc tế, tài trợ thương mại"]
          ,["PowerBI Report Server","PowerBI Services","Python","PowerApps","Databricks (SQL warehouse, Allert, Notebooks, Dashboard)"]
          ,"","04/2024-nay")
w_lamviec("Techcombank","Chuyên viên cao cấp Quản trị hiệu quả vận hành"
          ,["+ Kiểm soát các chỉ số vận hành (SLA/FTR/TAT/FCR) & các phân tích chuyên sâu đảm bảo chất lượng vận hành của đơn vị nghiệp vụ"
            ,"+ Tối ưu hiệu quả vận hành thông qua các giải pháp tự động hóa bằng dữ liệu (đối chiếu giao dịch/công cụ truy vấn theo quy định sản phẩm/công cụ tạo thông báo tự động...)"
            ,"+ Kiểm soát rủi ro hoạt động qua bộ rule giám sát giao dịch"]
          ,["+ Bộ báo cáo các chỉ số vận hành KHDN: SLA/FTR/TAT/FCR"
             ,"+ Bộ báo cáo quản lý năng lực nhân viên: Báo cáo hiệu suất, tỷ lệ đạt SLA, đạt thời gian xử lý tiêu chuẩn (SUT), tỷ lệ lỗi"
             ,"+ Công cụ tự động: Tổng hợp & gửi email nghĩa vụ cho KHDN, Đối chiếu số dư tài khoản trung gian, Tạo công văn và phương án xử lý nợ tự động cho hoạt động thu hồi nợ"
             ,"+ Apps: Quản lý dịch vụ tòa nhà tại HO (quản lý thẻ ra vào, đối tác, học viên, thẻ đi lại...); Check-in QR Code; Booking công tác; Theo dõi đòi tiền BCT cho nghiệp vụ TTTM"
             ,"+ ~ 50 rules giám sát rủi ro hoạt động vận hành KHDN thuộc Tài trợ thương mại."]
          ,["OracleDWH", "OBIEE", "PowerBI services", "Python", "PowerApps", "PowerAutomate","Agile"]
          ,"","05/2022-03/2024")
w_lamviec("Techcombank","Chuyên viên Thanh toán & Tài trợ thương mại"
          ,["+ Thực hiện nghiệp vụ tài trợ thương mại (phát hành LC, thông báo LC, kiểm tra chứng từ, giải ngân chiết khấu, phát hành bảo lãnh…)"
            ,"+ Đào tạo nhân viên mới (xây dựng tài liệu & trực tiếp hướng dẫn)"
            ,"+ Tham gia dự án xây dựng hệ thống BPM với vai trò đóng góp ý tưởng cho hệ thống & tester"
            ,"+ Review quy trình nghiệp vụ"]
          ,["+ Xây dựng công cụ đối chiếu phát hiện sai lệch, công cụ nhập liệu & truy vấn (VBA) giúp giảm sai sót & giảm thời gian xử lý giao dịch"]
          ,["Excel", "VBA", "OCR", "BRD", "CustomerCentric"]
          ,"","05/2022-03/2024")



#Version1---------------------------------------------------------------------------------
# def txt(a):  # 1 column - paragraph
#     _, col, _ = st.columns((1,3,1))
#     with col:
#         st.markdown(a)

# def txt1(a, b):  # 2 columns with offset to the left (2:1)
#   _, col1, col2, _ = st.columns([1,2,1,1])
#   with col1:
#     st.markdown(a)
#   with col2:
#     st.markdown(b)

# def txt2(a, b):  # 2 columns with offset to the right (1:2)
#   _, col1, col2, _ = st.columns([1,1,2,1])
#   with col1:
#     st.markdown(f'`{a}`')  # highlight text
#   with col2:
#     st.markdown(b)

# def txt3(a, b):  # 2 columns with offset to the right (1:2)
#   _, col1, col2, _ = st.columns([1,1,2,1])
#   with col1:
#     st.markdown(a)
#   with col2:
#     st.markdown(b)
  
# def txt4(a, b, c): # 3 columns
#   _, col1, col2, _, col3, _ = st.columns([1,0.65,1.5, 0.1,0.75,1])
#   with col1:
#     st.markdown(f'`{a}`')  # highlight text
#   with col2:
#     st.markdown(b)
#   with col3:
#     st.markdown(c)

# def myprj_thumbnail(title,domains,description,tools,skills,imagename):
#     ctn = st.container(border=True)
#     ctn.write(f'#### {title}')
#     ctn.markdown('Domain: '+' '.join([f':blue-background[{i}]' for i in domains]))
#     ctn.markdown(description)
#     ctn.markdown('Tools: '+' '.join([f':orange-background[{i}]' for i in tools]))
#     ctn.markdown('Skills: '+' '.join([f':green-background[{i}]' for i in skills]))
#     ctn_image = Image.open(f'./image/{imagename}')
#     ctn.image(ctn_image,use_column_width =True)

# st.set_page_config(page_title='Trần Duy Hoàng - Portfolio',page_icon="☀", layout="wide")

# with open("style.css") as f:
#     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
# image = Image.open('./image/my_portrait.jpg')
# header_img,header_title,_ = st.columns((1,2,1))
# header_img.image(image, width = 200)
# header_title.write('''
 
 
 
 
 
     
#     # TRẦN DUY HOÀNG
#     ##### Business Intelligence - Data Analyst
#     ''')
# tab1, tab2, tab3 = st.tabs(["    About me", "    My Projects", "    References"])
# with tab1:
#     txt2('April 2024 - now','Chuyên gia Quản trị hiệu quả vận hành')
#     txt2('','#Ngân hàng TMCP Kỹ thương Việt Nam')
#     txt2('May 2022 - Mar 2024','Chuyên viên cao cấp Quản trị hiệu quả vận hành')
#     txt2('Jul 2020 - Apr 2022','Chuyên viên Thanh toán & Tài trợ thương mại')

# with tab2:
#     col1,col2,col3,_ = st.columns([3,3,3,1])
#     with col1:
#         st.write('## Phân tích & cải tiến')
#         con11 = st.container(border=True)
#         con11.write('#### Dịch vụ vận hành')
#         con11.markdown("Domain: :blue-background[International Payment] :blue-background[Trade Finance]")
#         con11.markdown('''*Hoạt động vận hành tại các đơn vị hội sở và chi nhánh được kiểm soát thường xuyên thông qua phân tích dữ liệu xử lý giao dịch.  
#         Phân tích chuyên sâu các chỉ số rời rạc (FTR/SLA/TAT) nhằm cải thiện trải nghiệm khách hàng.  
#         Kể câu chuyện về trải nghiệm khách hàng về chất lượng dịch vụ thông qua mô hình RFM, qua quan sát hành trình khách hàng.*''')
#         con11.markdown("Tools: :orange-background[Oracle DWH] :orange-background[DataBricks] :orange-background[OBIEE] :orange-background[PowerBI] :orange-background[Excel]")
#         con11.image(image,width =150)

#         con12 = st.container(border=True)
#         con12.write('#### Tuân thủ chính sách nhân sự & văn hóa trải nghiệm')
#         con12.markdown('''*Phân tích hành vi tuân thủ giờ làm việc của CBNV toàn hàng, phát hiện hành vi không tốt của một bộ phận CBNV.  
#         Báo cáo kết quả tham gia hoạt động văn hóa tổ chức.*''')

#         con13 = st.container(border = True)
#         con13.write('#### Follow kích hoạt và chi tiêu thẻ tín dụng')
    
#     with col2:
#         st.write('## Giám sát rủi ro hoạt động')
#         st.markdown("Domain: :blue-background[Trade Finance] :blue-background[Loans]")
#         con2 = st.container(border=True)
#         con2.write('#### Sản phẩm LC')
#     with col3:
#         st.write('## Tự động hóa quy trình')
#         st.markdown("Domain: :blue-background[Trade Finance] :blue-background[Loans] :blue-background[Collections] :blue-background[Credit Cards Telesales]")
#         con31 = st.container(border = True)
#         con31.write('#### Tác nghiệp thu nợ tại hiện trường')
#         con31.markdown('''*Cán bộ thu nợ tại hiện trường ghi nhận vị trí tác nghiệp, kết quả tác nghiệp hoặc điều chỉnh kế hoạch tác nghiệp một cách nhanh chóng và di động.  Giám đốc thu hồi nợ có thể giám sát kết quả trực tiếp và thường xuyên.
#         *''')
#         con32 = st.container(border = True)
#         con32.write('#### Tác nghiệp chuyển tiền quốc tế ghi nhận kết quả xử lý ngoại lệ cho khách hàng')
#         con32.markdown('''*CV/CVCC trong quá trình tác nghiệp được trao quyền xử lý ngoại lệ, cần gọi điện cho KH và lưu thông tin cuộc gọi*''')

#         con33 = st.container(border = True)
#         con33.write('#### Đối chiếu số dư trên tài khoản trung gian')
#         con33.markdown('''*Công cụ xử lý hàng triệu dòng dữ liệu để đối chiếu giao dịch.*''')

#         con34 =st.container(border = True)
#         con34.write('#### Gửi thông báo nghĩa vụ tài chính/phi tài chính cho khách hàng')
#         con34.markdown('''*Tổng hợp dữ liệu nghĩa vụ của khách hàng, tự động gửi mail thông báo định kỳ:  
#         + Nghĩa vụ tài chính: thanh toán gốc/lãi vay, thanh toán BCT theo LC, lãi/phí LC UPAS, phí bảo lãnh, phí định giá lại, phí tái tục bảo hiểm tài sản...  
#         + Nghĩa vụ phi tài chính: nghĩa vụ bổ sung nợ chứng từ*''')

#         myprj_thumbnail('Gửi thông báo nghĩa vụ tới chi nhánh phục vụ khách hàng',['Trade Finance'],'''*Vào ngày phát sinh nghĩa vụ của khách hàng, thông báo cho chi nhánh thực hiện chuẩn bị nguồn ngoại tệ, giá, phí với khách hàng.  
#         Căn cứ để đơn vị hội sở điều động nguồn vốn.*''',['Oracle DWH','Python'],[''],'my_portrait.jpg')
#         myprj_thumbnail('Check in tự động tại sự kiện',['HR'],'''*CBNV sử dụng mã QR được cấp để check in tại sự kiện nội bộ quy mô 1xxx người.  
#         Ban tổ chức nắm được toàn bộ tình hình tham gia của các đơn vị.  
#         Tận dụng nguồn lực nội bộ thay vì thuê ngoài mà vẫn giữ được trải nghiệm tích cực cho CBNV*''',['Python','PowerApps'],['Hành trình khách hàng'],'my_portrait.jpg')


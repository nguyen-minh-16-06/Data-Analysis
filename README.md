# CONSUMER FINANCE PLATFORM (Hệ thống Chấm điểm Tín dụng, Cảnh báo Gian lận & Robo-Advisor)

Dự án này là một nền tảng phân tích hành vi tài chính tiêu dùng ứng dụng Machine Learning. Hệ thống bao gồm 3 luồng xử lý độc lập giúp giải quyết 3 bài toán cốt lõi của ngành tài chính: Dự báo khả năng vỡ nợ tín dụng, Cảnh báo gian lận thẻ và một Robo-Advisor cho phép khách hàng cá nhân nhập thông tin, tự động phân tích tâm lý rủi ro của họ bằng AI và đưa ra khuyến nghị phân bổ vốn đầu tư tự động.

## Cấu trúc thư mục dự án
```text
Data-Analysis/
├── 01_Report/
│   ├── Đồ án PTDLL - Nhóm 4 - KHDL&TTNT K4.docx/
│   ├── Đồ án PTDLL - Nhóm 4 - KHDL&TTNT K4.pdf/
├── 02_Source_Code/
│   ├── Dash-Dashboard/
│   │   ├── app.py
│   │   ├── finalized_model.sav
│   │   ├── notebook_risk_tolerance.ipynb
│   │   └── requirements.txt
│   ├── Fraud-Detection/
│   │   └── notebook_fraud_detection.ipynb
│   ├── Lending-Club/
│   │   └── notebook_loan_default_model.ipynb
│   └── SCF-Clustering/
│       ├── finalized_model.sav
│       ├── notebook_investor_clustering.ipynb
│       └── notebook_risk_tolerance.ipynb
├── 03_Dataset/
│   ├── Lending-Club/
│   │   └── loan_dataset.csv
│   ├── Credit-Card-Fraud/
│   │   └── creditcard.csv
│   └── SCF/
│       ├── InputData.csv
│       ├── ProcessedData.xlsx
│       ├── SCFP2009panel.xlsx
│       └── SP500Data.csv
├── 04_Figures/
│   ├── Dashboard/
│   │   ├── Compare Models.png
│   │   ├── Correlation Matrix.png
│   │   ├── Dashboard Robo-Advisor.png
│   │   └── Feature Importance.png
│   ├── Fraud-Detection/
│   │   ├── Compare Models.png
│   │   ├── Confusion matrix GBM Model.png
│   │   └── Confusion matrix LDA Model.png
│   ├── Lending-Club/
│   │   ├── Compare Models.png
│   │   ├── Confusion Matrix GBM Model.png
│   │   └── Features Importance.png
│   └── SCF-Clustering/
│       ├── Cluster Optimization Evaluation (Silhouette score).png
│       ├── Cluster Optimization Evaluation (SSE).png
│       ├── Correlation Matrix.png
│       ├── Demographics Analysis.png
│       ├── Financial and Risk Profile Analysis.png
│       └── Heatmap.png
├── 05_Slides/
│   └── Slide N4.pptx
└── 06_Demo_Video/
    ├── Demo Consumer Finance platform.mp4
    └── Video demo.mp4
```
LƯU Ý: Có một số folder vì dung lượng khá lớn nên không thể upload lên Repo này, tham khảo qua đường link sau: https://drive.google.com/drive/folders/19E9kLLxbRfBFrhC9NwSox5LbU4gTvsGn?usp=sharing

## Cài đặt và thiết lập

### 1. Yêu cầu hệ thống

- Python 3.10.11 hoặc cao hơn.
- `pip` và `venv`.

### 2. Cài đặt thư viện

Clone project và cài đặt các thư viện cần thiết:

```bash
# Clone kho lưu trữ về máy tính của bạn
git clone https://github.com/nguyen-minh-16-06/Data-Analysis.git

# Điều hướng đến thư mục của dự án
cd Data-Analysis

# Tạo và kích hoạt môi trường ảo
python -m venv venv
# Dành cho Windows:
venv\Scripts\activate
# Dành cho MacOS/Linux:
# source venv/bin/activate

# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

## Huấn luyện & đánh giá mô hình

Trước khi chạy ứng dụng dash, có thể xem quá trình tiền xử lý dữ liệu, huấn luyện mô hình và các chỉ số đánh giá bằng cách mở Jupyter Lab.

Mở terminal tại thư mục Data-Analysis và chạy lệnh:
```bash
jupyter lab
```

Quá trình phân tích trong các file notebook bao gồm:
- notebook_loan_default_model.ipynb: Làm sạch dữ liệu Lending Club (loại bỏ biến missing > 80%, loại biến có correlation < 0.03 và loại bỏ các biến không có ý nghĩa). Đánh giá mô hình bằng chỉ số ROC-AUC.
- notebook_fraud_detection.ipynb: Sử dụng random undersampling để ép tỷ lệ gian lận thẻ về 50/50. Tối ưu hóa mô hình GBM và LDA bằng chỉ số Recall để hạn chế tối đa việc bỏ lọt tội phạm.
- notebook_investor_clustering.ipynb: Phân cụm K-Means tập dữ liệu SCF, tìm `K` tối ưu bằng phương pháp Elbow và Silhouette score.
- notebook_risk_tolerance.ipynb: Huấn luyện Random Forest Regressor dự đoán điểm rủi ro và xuất ra file model finalized_model.sav.

## Khởi chạy Ứng dụng Web (Robo-Advisor)

Đảm bảo hãy đang ở trong thư mục 01_Source_Code/Dash-Dashboard và đã kích hoạt môi trường ảo. Thực thi câu lệnh sau để bật hệ thống:

```bash
python app.py
```
Sau khi terminal báo chạy thành công, hãy mở trình duyệt web và truy cập vào địa chỉ sau:
👉 **http://127.0.0.1:8050/**

### Thao tác trên Dashboard:
- Sử dụng các thanh trượt và ô nhập liệu bên cột trái để thiết lập hồ sơ khách hàng (Tuổi, Thu nhập, Tài sản ròng, Tình trạng hôn nhân...).
- Hệ thống tự động tính toán mức độ chấp nhận rủi ro thông qua mô hình Random Forest Regressor.
- Quan sát các biểu đồ bên phải để xem tỷ lệ phân bổ tài sản an toàn và rủi ro qua Pie chart, cơ cấu danh mục chi tiết qua Bar chart và mô phỏng hiệu suất sinh lời quá khứ bằng kỹ thuật backtesting qua Line chart.

## Quy trình hoạt động của hệ thống

### 1. Luồng xử lý ngầm
- Khai phá các tập tabular data có kích thước lớn.
- Khắc phục triệt để vấn đề mất cân bằng dữ liệu trong bài toán lừa đảo tài chính.
- Tự động hóa quá trình xác định khả năng rủi ro, thay thế cho các bảng khảo sát thủ công truyền thống.

### 2. Tư vấn trực quan
- Load file mô hình `finalized_model.sav` đã huấn luyện.
- Tiếp nhận input theo thời gian thực từ người dùng thông qua giao diện Dash.
- Áp dụng logic tài chính để quy đổi điểm số dự đoán từ AI thành tỷ lệ phần trăm phân bổ vốn đầu tư tự động (cổ phiếu, trái phiếu).

## Kết quả đầu ra mong đợi
- **Notebooks:** - Chỉ số ROC-AUC so sánh các mô hình dự báo nợ xấu.
  - Ma trận nhầm lẫn chứng minh tỷ lệ False Negatives thấp.
  - Các cluster được phân tách và gán nhãn rõ ràng.
- **Dashboard:**
  - Một ứng dụng tương tác trực tiếp, phản hồi ngay lập tức khi thay đổi thông số đầu vào.

## Thư viện sử dụng

- `pandas` & `numpy` (Xử lý dữ liệu dạng bảng)
- `scikit-learn` (Huấn luyện các mô hình Machine Learning)
- `imbalanced-learn` (Kỹ thuật Under-sampling)
- `dash` & `dash-bootstrap-components` (Xây dựng giao diện Dashboard)
- `plotly` (Vẽ biểu đồ tương tác)

*(Chi tiết phiên bản xem trong `requirements.txt`)*

## Ghi chú:
- **Hướng có thể mở rộng:**
  - Kết nối API lấy dữ liệu chứng khoán realtime để Robo-advisor tư vấn sát thực tế hơn.
  - Áp dụng các thuật toán Deep Learning/Neural Network cho bộ dữ liệu Fraud Detection.
  - Nâng cấp giao diện Dash thêm tính năng lưu trữ lịch sử tư vấn của người dùng.

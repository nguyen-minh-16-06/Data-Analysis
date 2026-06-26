import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objs as go
import pickle
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

app = dash.Dash(__name__)

try:
    model = pickle.load(open('finalized_model.sav', 'rb'))
    model_loaded = True
    print("Đã load thành công mô hình finalized_model.sav!")
except Exception as e:
    model_loaded = False
    print(f"LỖI: Không thể load mô hình. Chi tiết: {e}")

app.layout = html.Div(style={'font-family': 'Arial, sans-serif', 'padding': '20px', 'backgroundColor': '#f4f6f9'},
                      children=[

                          html.H1("HỆ THỐNG ROBO-ADVISOR TƯ VẤN ĐẦU TƯ",
                                  style={'textAlign': 'center', 'color': '#2c3e50', 'paddingBottom': '20px',
                                         'marginBottom': '40px', 'fontWeight': 'bold'}),

                          # Container chính chứa 2 cột
                          html.Div(style={'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'wrap',
                                          'justifyContent': 'space-between'}, children=[

                              html.Div(style={'width': '20%', 'backgroundColor': 'white', 'padding': '20px',
                                              'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'},
                                       children=[
                                           html.H3("THÔNG TIN CÁ NHÂN",
                                                   style={'borderBottom': '2px solid #3498db',
                                                          'paddingBottom': '20px',
                                                          'textAlign': 'center',
                                                          'fontSize': '25px',
                                                          'fontWeight': 'bold'}),

                                           html.Label("Độ tuổi", style={'fontWeight': 'bold'}),
                                           dcc.Input(id='input-age', type='text', value='25',
                                                     style={'width': '100%', 'marginBottom': '15px', 'padding': '8px'}),

                                           html.Label("Học vấn",
                                                      style={'fontWeight': 'bold'}),
                                           dcc.Input(id='input-edu', type='text', value='2',
                                                     style={'width': '100%', 'marginBottom': '15px', 'padding': '8px'}),

                                           html.Label("Hôn nhân",
                                                      style={'fontWeight': 'bold'}),
                                           dcc.Input(id='input-married', type='text', value='1',
                                                     style={'width': '100%', 'marginBottom': '15px', 'padding': '8px'}),

                                           html.Label("Số con", style={'fontWeight': 'bold'}),
                                           dcc.Input(id='input-kids', type='text', value='0',
                                                     style={'width': '100%', 'marginBottom': '15px', 'padding': '8px'}),

                                           html.Label("Nghề nghiệp",
                                                      style={'fontWeight': 'bold'}),
                                           dcc.Input(id='input-occ', type='text', value='1',
                                                     style={'width': '100%', 'marginBottom': '15px', 'padding': '8px'}),

                                           html.Label("Thu nhập hàng năm (USD)",
                                                      style={'fontWeight': 'bold'}),
                                           dcc.Input(id='input-income', type='text', value='50000',
                                                     style={'width': '100%', 'marginBottom': '15px', 'padding': '8px'}),

                                           html.Label("Rủi ro",
                                                      style={'fontWeight': 'bold'}),
                                           dcc.Input(id='input-risk', type='text', value='2',
                                                     style={'width': '100%', 'marginBottom': '15px', 'padding': '8px'}),

                                           html.Label("Tổng tài sản ròng (USD)",
                                                      style={'fontWeight': 'bold'}),
                                           dcc.Input(id='input-networth', type='text', value='100000',
                                                     style={'width': '100%', 'marginBottom': '25px', 'padding': '8px'}),

                                           html.Button('DỰ ĐOÁN KHẢ NĂNG RỦI RO', id='submit-button', n_clicks=0,
                                                       style={'width': '100%', 'backgroundColor': '#3498db',
                                                              'color': 'white', 'padding': '12px', 'fontSize': '16px',
                                                              'border': 'none', 'borderRadius': '5px',
                                                              'cursor': 'pointer'})
                                       ]),

                              html.Div(style={'width': '77.25%'}, children=[

                                  html.Div(
                                      style={'backgroundColor': '#fff3cd', 'padding': '20px', 'borderRadius': '10px',
                                             'marginBottom': '30px', 'border': '1px solid #ffeeba'},
                                      children=[
                                          html.H4("CHÚ THÍCH",
                                                  style={'margin': '0 0 15px 0', 'textAlign': 'center',
                                                         'fontSize': '18px', 'fontWeight': 'bold'}),
                                          html.Div([
                                              html.Div([html.B("Học vấn: "),
                                                        "1 (Không có bằng C3), 2 (Tốt nghiệp C3), 3 (Cao đẳng/Đại học), 4 (Sau Đại học)"],
                                                       style={'marginBottom': '10px', 'fontSize': '15px'}),
                                              html.Div([html.B("Hôn nhân: "), "1 (Đã kết hôn), 2 (Độc thân)"],
                                                       style={'marginBottom': '10px', 'fontSize': '15px'}),
                                              html.Div([html.B("Nghề nghiệp: "),
                                                        "1 (Quản lý), 2 (Bán hàng), 3 (Lao động), 4 (Thất nghiệp)"],
                                                       style={'marginBottom': '10px', 'fontSize': '15px'}),
                                              html.Div([html.B("Rủi ro: "),
                                                        "1 (Rủi ro cao), 2 (Rủi ro khá), 3 (Rủi ro TB), 4 (Không có)"],
                                                       style={'marginBottom': '0', 'fontSize': '15px'})
                                          ], style={'paddingLeft': '10px'})
                                      ]),

                                  html.Div(id='output-area',
                                           style={'display': 'none', 'backgroundColor': 'white', 'padding': '20px',
                                                  'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'},
                                           children=[
                                               html.H3("KẾT QUẢ",
                                                       style={'borderBottom': '2px solid #3498db',
                                                              'paddingBottom': '10px',
                                                              'textAlign': 'center',
                                                              'marginBottom': '20px',
                                                              'fontSize': '25px',
                                                              'fontWeight': 'bold'}),
                                               html.H3(id='risk-score-output',
                                                       style={'textAlign': 'center', 'color': '#e74c3c',
                                                              'marginBottom': '30px'}),

                                               # Flexbox để chứa Pie và Bar ngang hàng
                                               html.Div(style={'display': 'flex', 'justifyContent': 'space-between',
                                                               'marginBottom': '20px'}, children=[
                                                   dcc.Graph(id='allocation-chart', style={'width': '48%'}),
                                                   dcc.Graph(id='bar-chart', style={'width': '48%'})
                                               ]),

                                               dcc.Graph(id='performance-chart')
                                           ])
                              ])
                          ])
                      ])


@app.callback(
    [Output('output-area', 'style'),
     Output('risk-score-output', 'children'),
     Output('allocation-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('performance-chart', 'figure')],
    [Input('submit-button', 'n_clicks')],
    [State('input-age', 'value'),
     State('input-edu', 'value'),
     State('input-married', 'value'),
     State('input-kids', 'value'),
     State('input-occ', 'value'),
     State('input-income', 'value'),
     State('input-risk', 'value'),
     State('input-networth', 'value')]
)
def update_output(n_clicks, age, edu, married, kids, occ, income, risk, networth):
    if n_clicks == 0:
        return {'display': 'none'}, "", {}, {}, {}

    def to_num(val, default_val):
        try:
            return float(val)
        except (ValueError, TypeError):
            return default_val

    inputs = [
        to_num(age, 25),
        to_num(edu, 2),
        to_num(married, 1),
        to_num(kids, 0),
        to_num(occ, 1),
        to_num(income, 50000),
        to_num(risk, 2),
        to_num(networth, 100000)
    ]

    if model_loaded:
        input_features = np.array([inputs])
        risk_score = float(model.predict(input_features)[0]) * 100
    else:
        risk_score = 50

    risk_score = min(max(risk_score, 0), 100)
    stock_pct = risk_score
    bond_pct = 100 - stock_pct

    risk_text = f"DỰ ĐOÁN MỨC ĐỘ RỦI RO: {risk_score:.2f}/100"

    labels_pie = ['Cổ phiếu', 'Trái phiếu']
    values_pie = [stock_pct, bond_pct]
    colors_pie = ['#e74c3c', '#2ecc71']

    fig_pie = go.Figure(data=[go.Pie(labels=labels_pie, values=values_pie, hole=.4, marker=dict(colors=colors_pie))])
    fig_pie.update_layout(title_text="PHÂN BỔ TÀI SẢN", title_x=0.5, margin=dict(t=40, b=10), )

    tickers = ['GOOGL', 'FB', 'GS', 'MS', 'GE', 'MSFT']
    np.random.seed(int(risk_score) + 42)
    raw_weights = np.random.rand(len(tickers))
    ticker_weights = (raw_weights / raw_weights.sum()) * stock_pct

    fig_bar = go.Figure(data=[go.Bar(
        x=tickers,
        y=ticker_weights,
        marker=dict(color='#e74c3c'),
        text=[f"{w:.1f}%" for w in ticker_weights],
        textposition='auto'
    )])
    fig_bar.update_layout(title_text="CHI TIẾT DANH MỤC CỔ PHIẾU", title_x=0.5, margin=dict(t=40, b=10),
                          yaxis_title="Tỷ trọng (%)")

    # 3. BIỂU ĐỒ LINE (BACKTESTING TỪ 2020 ĐẾN 2026)
    np.random.seed(42)
    months = 100  # Khoảng thời gian từ tháng 1/2020 đến tháng 6/2026

    # Giả lập biến động thực tế của thị trường
    stock_returns = np.random.normal(loc=0.01, scale=0.06, size=months)
    bond_returns = np.random.normal(loc=0.003, scale=0.01, size=months)

    # Tính toán lợi nhuận gộp mỗi tháng dựa trên tỷ trọng
    portfolio_returns = (stock_pct / 100) * stock_returns + (bond_pct / 100) * bond_returns

    cumulative_value = [100]
    for r in portfolio_returns:
        cumulative_value.append(cumulative_value[-1] * (1 + r))

    # Đặt mốc thời gian bắt đầu từ 01/01/2020
    time_index = pd.date_range(start='2020-01-01', periods=months + 1, freq='M')

    fig_line = go.Figure(
        data=[go.Scatter(
            x=time_index,
            y=cumulative_value,
            mode='lines',
            line=dict(color='red', width=1.5),
            hovertemplate='<b>Thời gian:</b> %{x|%m/%Y}<br><b>Giá trị:</b> $%{y:.2f}<extra></extra>'
        )])

    fig_line.update_layout(
        title_text="DIỄN BIẾN GIÁ TRỊ TÀI SẢN ĐẦU TƯ",
        title_x=0.5,
        xaxis_title="",
        yaxis_title="",
        margin=dict(t=40, b=20, l=40, r=20),
        plot_bgcolor='white',
        hovermode='x unified'
    )

    fig_line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#f1f2f6')
    fig_line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#f1f2f6')

    return {'display': 'block'}, risk_text, fig_pie, fig_bar, fig_line


if __name__ == '__main__':
    app.run(debug=True, port=8050)
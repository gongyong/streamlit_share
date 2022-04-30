import streamlit as st
import numpy as np
import pandas as pd
import datetime
import altair as alt
from PIL import Image

st.title("Streamlit 超入門")

st.write("Display Image")


text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

if st.checkbox('Show Image'):
    img = Image.open('screenshot.png')
    st.image(img,caption='hogecaption',use_column_width=True)

'あなたの趣味：',text
'コンディション；',condition

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if (button):
    right_column.write(
        'ここは右カラム'
    )



# st.write("DateFrame")

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })
# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35,69],
#     columns=['lat','lon']
# )
# st.dataframe(df.style.highlight_max(axis=0))
# st.bar_chart(df)

# import matplotlib.pyplot as plt
# import matplotlib

# dat = np.random.rand(20,4)
# df = pd.DataFrame(dat, columns=['baseball','soccer','basketball','golf',])
# # df_1 = df.set_index('baseball')
# df.index.name = 'Time'

# plt.style.use('ggplot')
# font = {'family': 'meiryo'}
# matplotlib.rc('font', **font)

# fig = plt.figure(figsize=(12,5))

# ax1 = plt.subplot(121)
# plt.plot(df.index, df.baseball, label='baseball')
# plt.scatter(df.index, df.golf, color='red', label='golf')
# ax1.set_title('test')
# ax1.set_xlim(0,22)
# ax1.set_xlabel('time', fontsize=20)
# ax1.set_ylabel('arb units', fontsize=24)
# plt.tick_params(labelsize=18)

# ax2 =plt.subplot(122)
# plt.scatter(df.index, df.basketball, color='red')
# ax2.set_title('test_2')
# ax2.set_xlim(0,22)
# ax2.set_xlabel('time', fontsize=20)
# ax2.set_ylabel('basketball', fontsize=24)
# plt.tick_params(labelsize=18)

# df_pie = pd.DataFrame({'company': ['company A', 'company B', 'company C', 'company D', 'company E', 'company F'],
#                        'share': [0.25, 0.21, 0.15, 0.09, 0.17, 0.13]})

# fig = plt.Figure()
# fig.add_trace(plt.Pie(labels=df_pie['company'],
#                      values=df_pie['share'],
#                      textinfo='label+percent'),
# )
# fig.update_layout(showlegend=False)
# fig.show()

# plt.tight_layout()
# st.pyplot(fig)
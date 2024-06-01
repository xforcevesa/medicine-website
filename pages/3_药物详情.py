import random
import streamlit as st
import json

import sys
sys.path.append("..")

st.set_page_config(layout="wide")

from data import data, length, fetch_image

query_params = st.query_params.to_dict()

data_id = 1

if "id" in query_params:
    data_id = int(query_params["id"])
    if data_id > length:
        raise ValueError("Invalid ID")
    
col1, col2, col3 = st.columns([1, 3, 1], gap='large')
    
with col1:
    st.link_button('上一页', f'药物详情?id={data_id - 1}', disabled=not data_id > 1)
    
with col3:
    st.link_button('下一页', f'药物详情?id={data_id + 1}', disabled=not data_id < length)

# import base64
# from pathlib import Path

# def img_to_bytes(img_path):
#     img_bytes = Path(img_path).read_bytes()
#     encoded = base64.b64encode(img_bytes).decode()
#     return encoded

# def img_to_html(img_path):
#     img_html = "<img style='max-width: 50%;' src='data:image/png;base64,{}' class='img-fluid'>".format(
#       img_to_bytes(img_path)
#     )
#     return img_html

st.title(f"{data['药材名称'][data_id - 1]} - 药物详情")
        
output = []

# output.append('<style>.img-container { display: flex; flex-wrap: wrap; justify-content: center; }</style>')

# output.append('<div class="img-container">')

# for image_path in fetch_image(data_id):
#     output.append(img_to_html(image_path))

output.append('</div>')

for key in data.keys():
    key = str(key).strip()
    output.append('')
    output.append(f'## {key}')
    output.append('')
    field = str(data[key][data_id - 1])
    field = field.strip()
    if field in ['nan', 'None', '']:
        field = 'N/A'
    field = field.replace('\n', '<br>')
    field = field.replace('\r', '<br>')
    output.append(field)
    output.append('')


output.append(f'## 相关图片')

st.markdown('\n'.join(output), unsafe_allow_html=True)

for image_path in fetch_image(data_id):
    st.image(image_path, width=500)


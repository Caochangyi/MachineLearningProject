# 用来创建最终展示效果的streamlit web page
# 显示输入框，提交按钮，
# 后台调用模型，做预测
# 显示预测的情感分类结果

import streamlit as st

st.title("请输入反馈意见")

st.divider()

txt = st.text_input(label="评论",
              placeholder="请输入评论 ..."
              )

btn = st.button("提交")

if btn:
    print("提交内容:")
    print(txt)   #后台显示
    st.write("您反馈的内容是：",txt) #前台显示
    st.success("提交成功！")

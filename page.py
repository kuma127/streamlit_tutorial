import streamlit as st


def page1():
    st.title("What's your name?")

    def chanege_page():
        st.session_state["page-select"] = "page2"

    with st.form(key="name-form"):
        st.text_input("Message", key="name")
        st.form_submit_button(label="Submit", on_click=chanege_page)


def page2():
    name = st.session_state["name"]
    st.title(f"Hello, {name}")


pages = dict(
    page1="ページ1",
    page2="ページ2",
)

page_id = st.sidebar.selectbox(  # st.sidebar.*でサイドバーに表示する
    "ページ名",
    ["page1", "page2"],
    format_func=lambda page_id: pages[page_id],  # 描画する項目を日本語に変換
    key="page-select"
)

if page_id == "page1":
    page1()

if page_id == "page2":
    page2()

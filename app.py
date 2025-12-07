import streamlit as st
import streamlit.components.v1 as components
import zipfile
import os

st.set_page_config(layout="wide", page_title="트럭헬퍼 입지 분석")

st.title("🚛 트럭헬퍼 주차장 입지 분석 결과")

tab1, tab2 = st.tabs(["🗺️ 남양주 분석", "🗺️ 화성 분석"])

# --- [함수] 압축 풀고 HTML 읽어오는 기능 ---
def load_html_from_zip(zip_filename, html_filename):
    """zip 파일이 있으면 압축을 풀고 html을 읽어옵니다."""
    try:
        # html 파일이 없고 zip 파일만 있다면 압축 해제
        if not os.path.exists(html_filename):
            if os.path.exists(zip_filename):
                with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
                    zip_ref.extractall(".")
            else:
                return None # 파일 없음

        # html 파일 읽기
        with open(html_filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        st.error(f"파일 로드 중 오류 발생: {e}")
        return None

# --- [탭 1] 남양주 ---
with tab1:
    st.subheader("남양주시 주차장 입지 분석")
    # zip 파일 이름과 그 안의 html 파일 이름을 정확히 적어주세요
    html_data = load_html_from_zip("namyangju_map.zip", "namyangju_map.html")
    
    if html_data:
        components.html(html_data, height=700, scrolling=True)
    else:
        st.error("⚠️ 데이터 파일을 찾을 수 없습니다. (namyangju_map.zip)")

# --- [탭 2] 화성 ---
with tab2:
    st.subheader("화성시 주차장 입지 분석")
    # zip 파일 이름과 그 안의 html 파일 이름을 정확히 적어주세요
    html_data = load_html_from_zip("hwaseong_map.zip", "hwaseong_map.html")
    
    if html_data:
        components.html(html_data, height=700, scrolling=True)
    else:
        st.error("⚠️ 데이터 파일을 찾을 수 없습니다. (hwaseong_map.zip)")
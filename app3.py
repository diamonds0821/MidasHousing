import streamlit as st
import pandas as pd


st.set_page_config(page_title='미다스 페이지')


# ---  로그인 페이






# read excel
st.title('미다스하우징 매출')
st.subheader('기간: 23.01.01 ~ 23.01.18')


df = pd.read_csv('c:/data/n20230120.csv', thousands=',')
df1 = df.replace({'담당자':['대리점','반장창고','한샘']},'강실장')

df2 = df1.iloc[:,[1,5,6,11,17]]
df3 = pd.pivot_table(df2, index='담당자', values=['매출액','수금액'])


total_sales = (df['매출액'].sum())
total_sales1 = (df['총잔액'].sum())
total_sales2 = (df['수금액'].sum())

left_column,middle_column,right_column = st.columns(3)
with right_column:
    st.subheader('합계:')
    st.subheader(f'{total_sales1:,}원')
with middle_column:
    st.subheader('수금합계:')
    st.subheader(f"{total_sales2:,}원")
with left_column:
    st.subheader('매출합계:')
    st.subheader(f"{total_sales:,}원")

st.markdown('---')

groupby_column = st.selectbox(
    '',
    ('담당자','거래처명'
))
output_columns = ['매출액','수금액','총잔액']
df1_grouped = df1.groupby(by=[groupby_column], as_index=False)[output_columns].sum()
st.dataframe(df1_grouped)


st.markdown('------')

Ndf = pd.read_excel('c:/data/20230120.xlsx', thousands=',')
Ndf['날짜'] = pd.to_datetime(Ndf['전표일자'])
Ndf1 = Ndf.replace({'담당자':['대리점','반장창고','한샘']},'강실장')
Ndf2 = Ndf1.replace({'구분':'DC'},'반품')
Ndf3 = Ndf2.replace({'구분':'현매'},'매출')


groupby_column1 = st.selectbox(
    '',
    ('날짜','비고'
))
output_columns = ['총금액']
Ndf_grouped = Ndf3.groupby(by=[groupby_column1], as_index=False)[output_columns].sum()

dataset = pd.pivot_table(data=Ndf3, index='전표일자', columns='구분', values='총금액', aggfunc='sum')
st.dataframe(dataset)



options = st.multiselect(
    '거래처명을 입력하세요.',
    df2['거래처명'])

df_selection = df2.query(
    '거래처명 == @options'
)

st.dataframe(df_selection)
import pyodbc
import pandas

def Load_data(table_name, co_names):
    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 10.0};SERVER=192.168.2.10,1433;DATABASE=Yuqing;UID=sa;PWD=sinoimex2004*')
    cursor = conn.cursor()
    sql_search = "select id,title,details,currenttime from Yuqing.dbo.%s where DateDiff(hh,[currenttime],getDate())<=24 and details like '%%中国%%'" % table_name
    cursor.execute(sql_search)
    rows = cursor.fetchall()
    conn.commit()
    rows = list(zip(*rows))
    names = ['id', 'title', 'details', 'currenttime']
    df = DataFrame()
    for i in range(len(rows)):
        df[names[i]] = rows[i]
    return df[co_names]


conn = pyodbc.connect(
    r'DRIVER={SQL Server Native Client 10.0};SERVER=192.168.2.10,1433;DATABASE=Yuqing;UID=sa;PWD=sinoimex2004*')
cursor = conn.cursor()
sql_search = "select top 5 id,title,details,currenttime from Yuqing.dbo.China where DateDiff(hh,[currenttime],getDate())<=5 and details like '%%中国%%'"
cursor.execute(sql_search)
rows = cursor.fetchall()
print(rows)
conn.commit()
rows = list(zip(*rows))
print(rows)

header = ['企业名称', '法人代表', '联系电话', '传真电话', '业务联系人', '手机', '办公电话', '微信号', '出口产品海关编码', '所属行业', '企业人员总数', '管理人员', '技术人员', '登记注册类型', '企业工商登记日期', '企业注册地址', '所属区市县（先导区）', '企业通讯地址', '贸易方式', '企业网址', 'E-mail', '企业类型', '企业性质', '企业上市情况', '主营产品', '产品名称（英文名称）及产品描述', '近两年生产经营情况', '资产总额', '营业收入', '利润总额', '外贸出口额（万美元）', '上缴税金', '从业人员', '目前已进入的国际市场', '关注的国际市场']
print(header[0])
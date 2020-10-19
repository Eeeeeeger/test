import cx_Oracle
import os
import pandas as pd
from data.table_definitions import DATE_FORMAT_STRING, DB_TO_CONNECTION_STRING, TABLE_NAME_TO_DATE_COLUMN, TABLE_NAME_TO_COLUMNS_COMPLICATED_DAILY, TABLE_COLUMN_CONVERTERS, DB_ID_MAPPER, TABLE_TO_SQL

def get_df_from_db(sql):
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    columnDes = cursor.description #获取连接对象的描述信息
    columnNames = [columnDes[i][0] for i in range(len(columnDes))]
    df = pd.DataFrame([list(i) for i in data],columns=columnNames)
    return df

db_name='JY'
db_connection_string = DB_TO_CONNECTION_STRING[db_name]
db = cx_Oracle.connect(db_connection_string)


sql=(
"select "
    "T2.SECU_CODE, T2.ASHARES, T2.NONRESTRICTEDSHARES, T2.XGRQ "
"from ("
    "select "
        "T1.SECU_CODE, T1.ASHARES, T1.NONRESTRICTEDSHARES, T1.XGRQ, "
        "row_number() over (partition by T1.SECU_CODE order by T1.ENDDATE_STR desc) as RN "
    "from ("
        "select "
            "T0.SECU_CODE as SECU_CODE, T0.ASHARES as ASHARES, "
            "T0.NONRESTRICTEDSHARES as NONRESTRICTEDSHARES, T0.ENDDATE_STR, T0.XGRQ "
        "from ("
            "select "
                "concat(M.SECUCODE, case when M.SECUMARKET = 83 then '.SH' when M.SECUMARKET = 90 then '.SZ' ELSE '.UNKNOWN' end) as SECU_CODE, "
                "to_char(A.INFOPUBLDATE, 'yyyymmdd') as INFOPUBLDATE_STR, to_char(A.ENDDATE, 'yyyymmdd') as ENDDATE_STR, A.ASHARES as ASHARES, "
                "A.NONRESTRICTEDSHARES as NONRESTRICTEDSHARES, to_char(A.XGRQ, 'yyyymmdd HH24:MI:SS') as XGRQ "
            "from "
                "LC_SHARESTRU A "
            "join "
                "SECUMAIN M on M.COMPANYCODE = A.COMPANYCODE "
            "join "
                "LC_ASHAREIPO IPO on IPO.INNERCODE = M.INNERCODE"
            ") T0 "
        "where "
            "T0.ENDDATE_STR <= {} and T0.INFOPUBLDATE_STR <= {}"
        ") T1"
    ") T2 "
"where T2.RN = 1").format(20201012,20201012)
#df = get_df_from_db(sql)
df = pd.read_sql(sql,db)
print(df)

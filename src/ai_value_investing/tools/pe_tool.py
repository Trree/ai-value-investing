import baostock as bs
from datetime import datetime, timedelta
from crewai.tools import tool

class StockInfoTools():
    @tool("get_stock_pe")
    def get_stock_pe(code : str):
        """Clear description for what this tool is useful for, your agent will need this information to use it."""
        #### 登陆系统 ####
        lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)
        today = datetime.today()
        yesterday = today - timedelta(days=1)
        yesterday_date = yesterday.strftime("%Y-%m-%d")
        today_date = today.strftime("%Y-%m-%d")
        #### 获取沪深A股估值指标(日频)数据 ####
        # peTTM    滚动市盈率
        # psTTM    滚动市销率
        # pcfNcfTTM    滚动市现率
        # pbMRQ    市净率

        rs = bs.query_history_k_data_plus(code,
                                          "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
                                          start_date=yesterday_date, end_date=today_date,
                                          frequency="d", adjustflag="3")
        print('query_history_k_data_plus respond error_code:' + rs.error_code)
        print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)
        #### 登出系统 ####
        bs.logout()
        return rs.data[-1]

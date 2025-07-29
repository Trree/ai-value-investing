import baostock as bs
from datetime import datetime, timedelta
from tabulate import tabulate

def sort_key(row):
    value = float(row[4])
    if value >= 0:
        return 0, value
    else:
        return 1, -value

def get_stock_pe(code_list : list):
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
    result_list = []
    for code_name in code_list:
        code = code_name[0]
        rs = bs.query_history_k_data_plus(code,
                                          "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
                                          start_date=yesterday_date, end_date=today_date,
                                          frequency="d", adjustflag="3")
        print('query_history_k_data_plus respond error_code:' + rs.error_code)
        print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)
        result_list.append([code_name[1]] + rs.data[-1])

    #### 登出系统 ####
    bs.logout()
    # flattened_data = [item[-1] for item in result_list]
    sorted_data = sorted(result_list, key = sort_key)
    return sorted_data


if __name__ == '__main__':
    result = [['sh.601919', 'a']] 
    pe = get_stock_pe(result)
    headers = ["name", "date", "code", "close", "peTTM", "pbMRQ", "psTTM", "pcfNcfTTM"]
    print(tabulate(pe, headers=headers, tablefmt="pretty"))


# 實驗中

import pandas as pd
import pytz
from datetime import datetime, timedelta
import parsedatetime as pdt
import difflib

class CustomerService:
    def __init__(self):
        # 課表網址 https://docs.google.com/spreadsheets/d/1KLJx_tAMwKixMVeG1u5_V4TX1SaMUMVOteMJpSDKeKA/edit?gid=0#gid=0
        self.sheet_id = "1KLJx_tAMwKixMVeG1u5_V4TX1SaMUMVOteMJpSDKeKA"
        self.course_data = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/export?format=csv")

    # parsedatetime 僅支援英文, 輸入錯字/中文/空白/亂碼, 會變成返回今天
    def get_date(self, date_string):
        date_string = date_string [0] if isinstance(date_string, list) else date_string
        tz = pytz.timezone('Asia/Taipei')  # 設定時區
        now = datetime.now(tz)  # 取得日期 # 沒設定時區的結果會是GMT+0
        current_date = now.strftime("%Y-%m-%d")
        
        cal = pdt.Calendar()
        
        print(date_string.lower())
        
        ans, _ = cal.parseDT(date_string, now)
      
        # 如果輸入的字串包含"month" 返回一整個月的日期
        if 'month' in date_string.lower():
            start_date = ans.replace(day=1)
            next_month = start_date.replace(day=28) + timedelta(days=4)
            end_date = next_month - timedelta(days=next_month.day)
            date_list = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end_date - start_date).days + 1)]
            return date_list
        
        # 如果輸入的字串包含"week" 返回一整周的日期 (from 1 to 7)
        elif 'week' in date_string.lower():
            start_date = ans - timedelta(days=ans.weekday())
            end_date = start_date + timedelta(days=6)
            date_list = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]
            return date_list
        
        # 否則返回某一天
        else:
            date_list = [ans.strftime("%Y-%m-%d")]
            return date_list
        
    def get_course_topic(self, dates=[], relative_dates_describtion=""):
        if relative_dates_describtion:
            dates = self.get_date(relative_dates_describtion)
        
        if not isinstance(dates, list):
            dates = [dates]

        results = []
        for date in dates:
            index_date = self.course_data["Date"] == date
            if index_date.any():
                idx = self.course_data[index_date].index[0]
                ans = self.course_data.loc[idx, "社課主題"]
                results.append({'date': date, 'course_topic': ans})

        if not results:
            return {'course_topic': f"您指定的日期:{dates}，沒有課程。"}

        return results
    
    def get_course_location(self, dates=[], relative_dates_describtion=""):
        if relative_dates_describtion:
            dates = self.get_date(relative_dates_describtion)
        
        if not isinstance(dates, list):
            dates = [dates]

        results = []
        for date in dates:
            index_date = self.course_data["Date"] == date
            if index_date.any():
                idx = self.course_data[index_date].index[0]
                ans = self.course_data.loc[idx, "地點"]
                results.append({'date': date, 'location': ans})

        if not results:
            return {'location': f"您指定的日期:{dates}，沒有課程。"}

        return results

    def get_course_time(self, dates=[], relative_dates_describtion=""):
        if relative_dates_describtion:
            dates = self.get_date(relative_dates_describtion)
        
        if not isinstance(dates, list):
            dates = [dates]

        results = []
        for date in dates:
            index_date = self.course_data["Date"] == date
            if index_date.any():
                idx = self.course_data[index_date].index[0]
                ans = self.course_data.loc[idx, "Time"]
                results.append({'date': date, 'time': ans})

        if not results:
            return {'time': f"您指定的日期:{dates}，沒有課程。"}

        return results
      
    def find_course_by_topic(self, query):
        topics = self.course_data["社課主題"].tolist()
        closest_matches = difflib.get_close_matches(query, topics, n=1, cutoff=0.1)
        
        if not closest_matches:
            return {'result': f"找不到與 '{query}' 相符的課程主題。"}
        
        closest_match = closest_matches[0]
        index_topic = self.course_data["社課主題"] == closest_match
        idx = self.course_data[index_topic].index[0]
        
        date = self.course_data.loc[idx, "Date"]
        time = self.course_data.loc[idx, "Time"]
        
        return {
            'query': query,
            'closest_match': closest_match,
            'date': date,
            'time': time
        }

if __name__ == "__main__":
    my_service = CustomerService()
    print(my_service.get_course_topic(relative_dates_describtion="last week"))
    print(my_service.get_course_topic(['2024/11/04', '2024/11/05', '2024/11/06', '2024/11/07', '2024/11/08', '2024/11/09', '2024/11/10']))
    print(my_service.get_course_topic(my_service.get_date("last week")))
    print(my_service.get_course_topic('2024/11/04'))
    print(my_service.get_course_topic(relative_dates_describtion="today"))
    print(my_service.find_course_by_topic("期末發表"))
    print(my_service.find_course_by_topic("創業課程"))
    print(my_service.find_course_by_topic("專案討論"))
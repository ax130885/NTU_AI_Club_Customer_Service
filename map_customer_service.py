# 導入必要的模組
from customer_service import CustomerService

# 初始化 CustomerService
my_service = CustomerService()

# 函數映射
mapping = {
    'get_course_topic': my_service.get_course_topic,
    'get_course_location': my_service.get_course_location,
    'get_course_time': my_service.get_course_time,
    'find_course_by_topic': my_service.find_course_by_topic
}

# 函數描述
functions = [
    {
        "name": "get_course_topic",
        "description": "Get the course topic based on the input variable {dates} or {relative_dates_describtion}. The dates formats which you want to query must be like yyyy-mm-dd.",
        "parameters": {
            "type": "object",
            "properties": {
                "dates": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "The string list of specific dates to get the course topic."
                },
                "relative_dates_describtion": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "The string of relative dates, like: 'today', 'yesterday', 'tomorrow', 'next week', 'last month', '3 years ago'..."
                }
            },
            "required": []
        }
    },
    {
        "name": "get_course_location",
        "description": "Get the course location based on the input variable {dates} or {relative_dates_describtion}. The dates formats which you want to query must be like yyyy-mm-dd.",
        "parameters": {
            "type": "object",
            "properties": {
                "dates": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "The string list of specific dates to get the course location."
                },
                "relative_dates_describtion": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "The string of relative dates, like: 'today', 'yesterday', 'tomorrow', 'next week', 'last month', '3 years ago'..."
                }
            },
            "required": []
        }
    },
    {
        "name": "get_course_time",
        "description": "Get the course time based on the input variable {dates} or {relative_dates_describtion}. The dates formats which you want to query must be like yyyy-mm-dd.",
        "parameters": {
            "type": "object",
            "properties": {
                "dates": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "The string list of specific dates to get the course time."
                },
                "relative_dates_describtion": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "The string of relative dates, like: 'today', 'yesterday', 'tomorrow', 'next week', 'last month', '3 years ago'..."
                }
            },
            "required": []
        }
    },
    {
        "name": "find_course_by_topic",
        "description": "Find the course date and time based on the input variable {query}. The query should be a string that matches or is similar to the course topic.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The string to query the course topic."
                }
            },
            "required": ["query"]
        }
    }
]
def response_formatter(status: str, message: str, data=None):
    """
    統一 API 回傳格式
    :param status: "success" or "error"
    :param message: 說明訊息
    :param data: 可選的資料內容 (dict / list / None)
    :return: dict
    """
    return {
        "status": status,
        "message": message,
        "data": data
    }
def main(trans, webhook, params):
    error = ''
    data = {
        'somedata': '12345'
    }
    return {"success": not error, "error": error, "data": data}
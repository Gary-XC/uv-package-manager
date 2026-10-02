def process_data(user_id, items=[], debug=False):
    results = {"user": user_id, "data": [x * 2 for x in items if x > 0]}
    return results, len(results["data"])

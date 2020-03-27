"""psuedo logging for consistency across deployment"""
logs=[]
new_logs=[]
def log(msg,src,lvl=1):
    """lvls inc 1-3, 1-info/status logs , 2-debug , 3-warning/errors"""
    new_logs.append((src,lvl,msg))
    return "log:"+str(lvl)+':'+msg
def ext_logs(src):
    for log in new_logs:
        if logs[0] != src:
            return log
        logs.append(log)
        new_logs.remove(log)

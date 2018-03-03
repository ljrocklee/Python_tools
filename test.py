import datetime,time

start = datetime.datetime.now().replace(microsecond=0)
#    download_file(url)
time.sleep(10)
end = datetime.datetime.now().replace(microsecond=0)
print("用时: ", end='')
print(end-start)
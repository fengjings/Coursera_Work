import psutil

def check_cpu_usage(per):
    usage = psutil.cpu_percent()
    return usage < per

if not check_cpu_usage(75):
    print('overloaded')
else:
    print('good')
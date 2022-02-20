from flask import Flask
from flask import render_template
import platform
import psutil

app = Flask(__name__)

@app.route('/')
def home():

    hdd = psutil.disk_usage('/')
    total = int(hdd.total) / (2**30)
    used = int(hdd.used) / (2**30)
    free =  hdd.free / (2**30)
    mem = psutil.virtual_memory()
    proc = psutil.process_iter()
    print(proc)
    """Landing page."""
    return render_template(
        'index.html',
        title="Exadel Task 2",
        description="Flask generate Page.",
        os_name=platform.system(),
        os_version=str(platform.version()),
        os_release=str(platform.release()),
        disk_total=f'{round(total)} GB',
        disk_used=f'{round(used)} GB',
        disk_free=f'{round(free)} GB',
        mem_free=f'{mem.free} B',
        mem_total=f'{mem.total} B',
        mem_used=f'{mem.used} B',
        processes=proc
    )

# @app.route('/process')
# def processes():
#     proc = os.popen('ps')
#     return render_template(
#         'proc.html',
#         processes=proc
#     )

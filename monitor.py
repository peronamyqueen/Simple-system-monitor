import psutil
import time
from rich.console import Console
from rich.table import Table

console = Console()

def show_stats():
    table = Table(title="System Resource Monitor")

    table.add_column("Metric", justify="left", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    # CPU
    cpu_percent = psutil.cpu_percent(interval=1)
    table.add_row("CPU Usage", f"{cpu_percent} %")

    # RAM
    mem = psutil.virtual_memory()
    table.add_row("RAM Usage", f"{mem.used // (1024 ** 2)} MB / {mem.total // (1024 ** 2)} MB ({mem.percent} %)")

    # Disk
    disk = psutil.disk_usage('/')
    table.add_row("Disk Usage", f"{disk.used // (1024 ** 3)} GB / {disk.total // (1024 ** 3)} GB ({disk.percent} %)")

    # Network
    net = psutil.net_io_counters()
    table.add_row("Net Sent", f"{net.bytes_sent // (1024 ** 2)} MB")
    table.add_row("Net Received", f"{net.bytes_recv // (1024 ** 2)} MB")
    
    #Battery
    battery = psutil.sensors_battery()
    table.add_row("Battery Power", f"{battery.percent}")
    table.add_row("Minutes before power loss" , f"{battery.secsleft // 60}")

    console.clear()
    console.print(table)

while True:
    show_stats()
    time.sleep(0.5)


import platform
import psutil
import os
from datetime import datetime


def get_size(bytes, suffix="B"):
    """
    Преобразует байты в читаемый формат (например, 1024B -> 1KB)
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# Информация о системе
print("="*40, "Информация о системе", "="*40)
uname = platform.uname()
print(f"Система: {uname.system}")
print(f"Имя узла: {uname.node}")
print(f"Релиз: {uname.release}")
print(f"Версия: {uname.version}")
print(f"Машина: {uname.machine}")
print(f"Процессор: {uname.processor}")

# Информация о загрузке
print("="*40, "Информация о загрузке", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Время загрузки: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# Информация о ЦПУ
print("="*40, "Информация о ЦПУ", "="*40)
print("Физические ядра:", psutil.cpu_count(logical=False))
print("Всего ядер:", psutil.cpu_count(logical=True))
cpufreq = psutil.cpu_freq()
print(f"Макс. частота: {cpufreq.max:.2f}Mhz")
print(f"Мин. частота: {cpufreq.min:.2f}Mhz")
print(f"Текущая частота: {cpufreq.current:.2f}Mhz")
print("Загрузка ЦПУ по ядрам:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Ядро {i}: {percentage}%")
print(f"Общая загрузка ЦПУ: {psutil.cpu_percent()}%")

# Информация о памяти
print("="*40, "Информация о памяти", "="*40)
svmem = psutil.virtual_memory()
print(f"Всего: {get_size(svmem.total)}")
print(f"Доступно: {get_size(svmem.available)}")
print(f"Используется: {get_size(svmem.used)}")
print(f"Процент: {svmem.percent}%")
print("="*20, "Подкачка", "="*20)
swap = psutil.swap_memory()
print(f"Всего: {get_size(swap.total)}")
print(f"Свободно: {get_size(swap.free)}")
print(f"Используется: {get_size(swap.used)}")
print(f"Процент: {swap.percent}%")

# Информация о дисках
print("="*40, "Информация о дисках", "="*40)
print("Разделы и использование дисков:")
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Диск: {partition.device} ===")
    print(f"  Точка монтирования: {partition.mountpoint}")
    print(f"  Файловая система: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    print(f"  Общий размер: {get_size(partition_usage.total)}")
    print(f"  Используется: {get_size(partition_usage.used)}")
    print(f"  Свободно: {get_size(partition_usage.free)}")
    print(f"  Процент: {partition_usage.percent}%")

# Информация о сетевой статистике
net_io = psutil.net_io_counters()
print(f"Всего байт отправлено: {get_size(net_io.bytes_sent)}")
print(f"Всего байт получено: {get_size(net_io.bytes_recv)}")

import subprocess

def run_adb_command(command):
    adb_path = "/caminho/completo/para/adb"  # Substitua pelo caminho real
    result = subprocess.run([adb_path] + command, stdout=subprocess.PIPE, text=True)
    return result.stdout


def run_adb_command(command):
    result = subprocess.run(['adb'] + command, stdout=subprocess.PIPE, text=True)
    return result.stdout

def test_battery_level():
    battery_info = run_adb_command(['shell', 'dumpsys', 'battery'])
    print(battery_info)

def test_device_info():
    device_info = run_adb_command(['shell', 'getprop'])
    print(device_info)

if __name__ == "__main__":
    test_battery_level()
    test_device_info()

import subprocess

# Get all saved Wi-Fi profiles
data = subprocess.check_output("netsh wlan show profiles").decode("utf-8", errors="ignore")

profiles = []

for line in data.split("\n"):
    if "All User Profile" in line:
        profile = line.split(":")[1].strip()
        profiles.append(profile)

print("{:<30} {}".format("WiFi Name", "Password"))
print("-" * 50)

for profile in profiles:
    try:
        results = subprocess.check_output(
            f'netsh wlan show profile name="{profile}" key=clear'
        ).decode("utf-8", errors="ignore")

        password = "No Password"

        for line in results.split("\n"):
            if "Key Content" in line:
                password = line.split(":")[1].strip()

        print("{:<30} {}".format(profile, password))

    except:
        print("{:<30} {}".format(profile, "Error"))

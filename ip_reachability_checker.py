import subprocess


def check_ip_reachability(ip):
    try:
        # Send 4 pings with a timeout of 2 seconds each
        result = subprocess.run(['ping', '-n', '4', '-w', '2000', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, timeout=10)

        if "Lost = 0 (0% loss)" in result.stdout:
            return "Reachable"
        else:
            return "Filtered or Unreachable"

    except subprocess.TimeoutExpired:
        return "Filtered or Unreachable"
    except Exception as e:
        return "Error"


def main():
    choice = input("Do you want to check a list of IPs or one by one? (list/one): ")

    if choice.lower() == "list":
        ip_list = input("Enter a list of IPs separated by spaces: ").split()
        for ip in ip_list:
            result = check_ip_reachability(ip)
            print(f"IP {ip} is {result}")
    elif choice.lower() == "one":
        while True:
            ip = input("Enter an IP address (or 'exit' to quit): ")

            if ip.lower() == "exit":
                break

            result = check_ip_reachability(ip)
            print(f"IP {ip} is {result}")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()

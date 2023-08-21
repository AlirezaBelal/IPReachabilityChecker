The **IP Reachability Checker** is a simple Python script that allows you to test the reachability of IP addresses using the ICMP ping protocol. It sends ping requests to the specified IP addresses and determines whether they are reachable, filtered, or unreachable based on the received replies and timeouts.

## Prerequisites

- Python 3.x (https://www.python.org/downloads/)

## Usage

1. Clone or download this repository.

2. Open a terminal or command prompt and navigate to the directory containing the `ip_reachability_checker.py` file.

3. Run the script using the following command:

    ```bash
    python ip_reachability_checker.py
    ```

4. The script will prompt you to enter an IP address. You can enter an IP address you want to test or type `exit` to quit the program.

5. The script will perform the ping test and display the results based on the received replies and timeouts.

## Example

Enter an IP address (or 'exit' to quit): 8.8.8.8
IP 8.8.8.8 is Reachable

Enter an IP address (or 'exit' to quit): 10.0.0.1
IP 10.0.0.1 is Filtered or Unreachable

Enter an IP address (or 'exit' to quit): exit


## Notes

- The script sends multiple ping requests to the specified IP address and checks for 0% packet loss to determine reachability. However, reachability can be influenced by network conditions and security settings.

- This script is intended for educational and informational purposes and may not work in all network configurations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# pyScan - A Simple Multithreaded Service Enumerator

pyScan is a simple command-line tool built using Python for enumerating services on a target IP address. It scans a range of ports and identifies open ports along with their default service names.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Usage

```shell
./pyScan.py target_ip [-h] [-t TIMEOUT] [-p PORTS]
```

- `target_ip`: The IP address of the target to scan.
- `-t, --timeout`: Set the scanner timeout (optional).
- `-p, --ports`: Port range to scan (e.g., 1-100). Default is "1-100".

## Example

To scan a target IP address with the default port range (1-100):

```shell
./pyScan.py target_ip
```

To specify a custom timeout:

```shell
./pyScan.py target_ip -t 5
```

To scan a specific port range:

```shell
./pyScan.py target_ip -p 80-1000
```

## Output

The output of the script includes information about open ports on the target IP address:

```shell
Target: <target_ip>  Port: <port> is open  Default Service: <service_name>
```

If the default service name for a port is unknown, it will be displayed as "Unknown".

## Multithreading

pyScan utilizes multithreading to improve the scanning performance. By default, it uses up to 10 threads (`max_workers=10`) to concurrently scan the ports.

## Error Handling

If an error occurs during the scan, an error message will be displayed.

## License

This project is licensed under the [MIT License](LICENSE).

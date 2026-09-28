ips = [
    "10.10.1.10",
    "10.10.1.11",
    "10.10.1.10",
    "10.10.1.12",
    "10.10.1.11",
    "10.10.1.13"
]

unique_ips = list(set(ips))
print(unique_ips)
print(f"Total unique IPs are: {len(unique_ips)}")
import ipaddress

from File_reader import log_first_100k


def sort_log(log, index):
    try:
        return sorted(log, key=lambda x: x[index])
    except IndexError:
        print("Błąd: Podany indeks przekracza rozmiar krotek.")
        return log
    except TypeError:
        print("Błąd: Nieprawidłowy format danych – oczekiwano listy krotek.")
        return log


def test_sort_log():
    log_data = log_first_100k()
    sorted_log = sort_log(log_data, 3)

    for line in sorted_log:
        print(line)


def get_entries_by_addr(log, addr):
    try:
        addr_ip  = ipaddress.ip_address(addr)
        return [entry for entry in log if entry[7] == addr_ip]
    except ValueError:
        print(f"{addr} is not a valid IP address.")
        return []

def test_get_entries_by_addr():
    log_data = log_first_100k()
    filtered_log = get_entries_by_addr(log_data, '192.168.22.252')
    for entry in filtered_log:
        print(entry)

if __name__ == '__main__':
    test_get_entries_by_addr()
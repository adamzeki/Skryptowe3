from file_reader import log_first_100k


def entry_to_dict(log_entry):
    keys = ['ts', 'uid', 'id_orig_h', 'id_oirg_p', 'id_resp_h', 'id_resp_p', 'method', 'host', 'uri', 'stat_code']
    return dict(zip(keys, log_entry))

def log_to_dict(log):
    log_dict = {}

    for entry in log:
        entry_dict = entry_to_dict(entry)
        uid = entry_dict['uid']

        if uid not in log_dict:
            log_dict[uid] = []

        log_dict[uid].append(entry_dict)

    return log_dict

def test_entry_to_dict():
    log = log_first_100k()
    log_entry_dict = entry_to_dict(log[7])
    print(log_entry_dict)

def test_log_to_dict():
    log = log_first_100k()
    log_dict = log_to_dict(log)
    for key, entries in log_dict.items():
        print(f"UID: {key}")
        for entry in entries:
            print(entry)

if __name__ == '__main__':
    #test_entry_to_dict()
    test_log_to_dict()
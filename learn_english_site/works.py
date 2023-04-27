def get(csv):
    data = []
    with open(csv , "r", encoding="utf-8") as f:
        for cnt, line in enumerate(f.readlines()[1:]):
            data_line = [cnt + 1] + line.split(";")
            data.append(data_line)
    return data


def write(csv, data):
    new_line = ";".join(data)
    with open(csv, "r", encoding="utf-8") as f:
        existing_data = [l.strip("\n") for l in f.readlines()]
        title = existing_data[0]
        old_data = existing_data[1:]
    new_data = old_data + [new_line]
    new_data.sort()
    new_data = [title] + new_data
    with open(csv, "w", encoding="utf-8") as f:
        f.write("\n".join(new_data))
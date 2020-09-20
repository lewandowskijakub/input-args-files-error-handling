import sys

NAME_INDEX = 0


def get_filename(my_args):
    if len(my_args) >= 3:
        filename = my_args[1]
        return filename
    else:
        print("[ WARNING ] You should run this program by calling: python parser.py input_file_name output_file_name")
        return ""

def get_madefile(my_args):
    if len(my_args) >= 3:
        madefile = my_args[2]
        return madefile
    else:
        return ""

def read_from_file_to_list(filename):
    output = []

    with open(filename,"r") as file_to_read:
        for line in file_to_read.readlines():
            row = line.replace("\n","").split(" ")
            output.append(row)
    
    return output

def get_names(data_list):
    names = []

    for line in data_list:
        names.append(line[NAME_INDEX])

    return ", ".join(names)

def generate_report(filename, data_list, madefile):
    output = []
    output.append(f"Nazwa Twojego pliku zrodlowego to: {filename}")
    output.append(f"Nazwa utworzonego pliku to: {madefile}")
    output.append(f"Ilosc danych {len(data_list)}")
    output.append(f"Imiona: {get_names(data_list)}")

    return output

def save_report_to_file(report, filename):
    with open(filename, "w+") as file_to_read:
        for report_data in report:
            file_to_read.write(report_data + "\n")

def main():
    my_args = list(sys.argv)
    filename = get_filename(my_args)
    madefile = get_madefile(my_args)

    if len(filename) == 0:
        return
    
    print(f"File to parse: {filename}")
    data_list = read_from_file_to_list(filename)
    report = generate_report(filename, data_list, madefile)
    save_report_to_file(report, madefile)


if __name__ == "__main__":
    main()
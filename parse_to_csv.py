import os
import csv

from ACHFileParser import ACHFileParser

def write_to_csv(ach_object, csv_writer):
    for record in ach_object.records:
        csv_writer.writerow(record.to_dict()) 

if __name__ == "__main__":
    ach_folder = "path/to/your/ach/files"
    output_csv = "parsed_ach_records.csv"

    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = [...]  # Fill this in
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        csv_writer.writeheader()

        for ach_file in os.listdir(ach_folder):
            if ach_file.endswith(".ach") or ach_file.endswith(".txt"):  # Adapt the condition to your needs
                ach_path = os.path.join(ach_folder, ach_file)
                ach_object = ACHFileParser(ach_path)
                write_to_csv(ach_object, csv_writer)

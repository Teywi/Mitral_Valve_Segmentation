import csv

# Open the input file and the output file
with open('submission_005.csv', 'r') as infile, open('submission_005_good_format.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Write the header row if present
    header = next(reader)
    writer.writerow(header)
    
    # Iterate over the rows
    for row in reader:
        # Modify the 'value' field by adding a space after the comma
        row[1] = row[1].replace(',', ', ')
        # Write the modified row to the output file
        writer.writerow(row)

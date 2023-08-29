from ACHFileParser import *

# header_line='101 065503681 0655036811202170910A094101HANCOCK BANK           MY COMPANY USA  '
# file_header = FileHeaderRecord(header_line)
# print(file_header.__dict__)

# batch_header_line = "5200MY COMPANY USA                      9123456789PPDPAYROLL   120220120220   1065503680000001"
# batch_header = BatchHeaderRecord(batch_header_line)
# print(batch_header.__dict__)

# batch_control_line = "6230655033481111111          0000000000000001309      JOHN M SMITH            0065503680000001"
# batch_control = BatchControlRecord(batch_control_line)
# print(batch_control.__dict__)

parser = ACHFileParser("/Users/rjsimpson/code/ach-parser/ach_sample.ach")
parser.parse()
for record in parser.records:
    print(record.__dict__)

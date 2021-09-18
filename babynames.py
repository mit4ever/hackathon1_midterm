#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Python for Tester - OneMount Class
# Quang Le - quangdle@gmail.com - 09/2021

from os import error, linesep
import sys
import re
import getopt

"""Baby Names exercise

Định nghĩa hàm extract_names() dưới đây và gọi từ hàm main().

Cấu trúc các tag html trong các file baby.html như sau:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Các bước nên làm tuần tự:
 -Trích xuất năm
 -Lấy và in ra tên và thứ hạng phổ biến
 -Xây danh sách [year, 'name rank', ... ] và in ra
 -Sửa hàm main() để dùng hàm extract_names.
"""


def extract_names(filename):
  """
  Cho một file .html, trả ra list bắt đầu bằng năm, 
  theo sau bởi các chuỗi tên-xếp hạng theo thứ tự abc.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  pattern_year = "Popularity in (\\d+)"
  pattern_name = 'tr align="right"><td>(\d+)<\/td><td>(\w+)<\/td><td>(\w+)<'


  list_rank = []

  with open(filename, 'r') as reader:
    lines = reader.readlines()


    for line in lines:
          #print(line)
          for match_year in re.findall(pattern_year, line):
                list_rank.append(match_year)
                #print(match_year)

          for match_name in re.findall(pattern_name, line):
                #print(f'{(match_name)[0]} | {(match_name)[1]} | {(match_name)[2]}' )
                     
                list_rank.append(f'{(match_name)[1]}  {(match_name)[0]}')
                list_rank.append(f'{(match_name)[2]}  {(match_name)[0]}')
          
    return (sorted(list_rank, reverse=False))
    #print(reg_year)

    # for line in reader:
    #       reg_year = re.search(pattern_year, line)

  # for i, line in enumerate(open('baby1990.html')):
        
  #       for match in re.findall(pattern_year, line):
                         
  #             print(match)


def main():
  # Chương trình này có thể nhận đối số đầu vào là một hoặc nhiều tên file
  # args = sys.argv[1:]
  # summaryfile = None

  # if not args:
  #   print('usage: [--summaryfile] file [file ...]')
  #   sys.exit(1)
  
  # # Notice the summary flag and remove it from args if it is present.
  # summary = False
  # if args[0] == '--summaryfile':
  #   summary = True
  #   del args[0]

  
  # +++your code here+++
  # Với mỗi tên file, gọi hàm extract_names ở trên và in kết quả ra stdout
  # hoặc viết kết quả ra file summary (nếu có input --summaryfile).
  # try:

  #   opts, arg = getopt.getopt(args, "s:",["summaryfile="])

    # for opt, arg in opts:
    #       if opts in ["-s", "--summaryfile"]:
    #             summaryfile = arg

    #             print(summaryfile)
    #print(arg[0])            
    #data = extract_names()
    #print(data)
          
  #except getopt.error as err:
    #print(error)
  data = extract_names("baby1990.html")
  print(data)


if __name__ == '__main__':
  main()
  #extract_names("baby1990.html")

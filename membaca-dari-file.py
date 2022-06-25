import requests
# from contextlib import closing
# import csv
import pandas as pd

# #lokasi file csv
# url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'
#
# # Baca file csv streaming
# with closing(requests.get(url, stream = True)) as  r:
#     f = (line.decode('utf-8') for line in r.iter_lines())
#
#     reader = csv.reader(f, delimiter=',')
#
#     # membaca baris per baris
#     for row in reader:
#         print(row)
#
# # tentukan lokasi file, nama file, dan inisialisasi csv
# f = open('https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv', 'r')
# reader = csv.reader(f)
#
# # membaca baris per baris
# for row in reader:
#     print(row)
#
# # menutup file csv
# f.close()
# Mengimpor Modul Calendar
import calendar
 
# Menginput Tahun dan Bulan
yyyy = int(input("Masukkan Tahun: "))
mm = int(input("Masukkan Bulan: "))
 
# Menampilkan Kalender Bulanan
print(calendar.month(yyyy, mm))
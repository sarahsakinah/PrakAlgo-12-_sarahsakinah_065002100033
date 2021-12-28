# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:02:24 2021

nama :sarah sakinah
nim:065002100033
prodi:sistem informasi

"""
print("@@@@  @@@  @@@@  @@@  @   @")
print("@     @ @  @  @  @ @  @   @")
print("@@@@  @@@  @@@@  @@@  @@@@@")
print("   @  @ @  @@    @ @  @   @")
print("   @  @ @  @ @   @ @  @   @")
print("@@@@  @ @  @  @  @ @  @   @")

def linear_search(nomor,mark_dicari,kiri,kanan):
    while kiri <= kanan:
        mid = (kiri + kanan)//2
        if mark_dicari == nomor[mid]:
            return mid
        elif mark_dicari > nomor[mid]:
            kiri = mid + 1
        else:
            kanan = mid - 1
    return -1
nomor =[]
askfor=int(input('masukkan jumblah angka pada list: '))
for i in range(askfor):
    i+=1
    nomor.append(int(input(f'masukan angka ke {i}:')))
print(nomor)
mark_dicari = int(input('masukkan angka yang dicari: '))
results = linear_search(nomor,mark_dicari,0,len(nomor)-1)
if results != -1:
    print("hasil linear search ditemukan pada index ke " + str(results))
else:
    print("Angka tidak ditemukan")
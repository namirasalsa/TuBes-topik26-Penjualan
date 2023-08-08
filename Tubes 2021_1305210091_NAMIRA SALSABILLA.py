# Namira Salsabilla (1305210091)
def read(file): #fungsi membaca file txt
    return open('fileteks.txt')

#fungsi membuat Dictionary dari filetxt
def makeDict(file):
    penjualan = {}
    for line in file:
        data  = line.split() #menjadi list
        #nama menjadi key dan data penjualan menjadi value
        penjualan[data[0]] = [int(i) for i in data[1:]] 
    return penjualan

#membuat list dari dictionary
def makeList(dict):
    penjualan_list = list() #list kosong 
    penjualan_list.append(dict) #menambah dictionary ke list
    return penjualan_list


#mencari 'penjualan' tertinggi, return string nama
def tertinggi(list):
    max = 0
    for i in list:
        for key,value in i.items():
            jumlah = sum(value)
            if max<jumlah:
                nama = key
    return nama


#rerata 
def report(list):
    for i in list:
        print(('-' * 22))
        print("RATA-RATA TIAP PENJUAL")
        print(('-' * 22))
        print('{:6} {} {:8}'.format('NAMA', '|', 'RATA-RATA'))
        print(('-' * 22))
        for key,value in i.items():
            rata = sum(value)/len(value)
            print(key, ": ", rata)
            
#show list-dict
def Penjualan(list):
    for i in list:
        for key,value in i.items():
            print(key, ": ", ' '.join(str(x) for x in value))


#main program
def main():
    file = read("fileteks")
    penjualan_dict = makeDict(file) #memanggil fungsi makeDict
    print(penjualan_dict)
    print()

    #tabel dan pemanggilan fungsi yang menampilkan data penjualan
    print('-' * 35)
    print('{:^34}'.format('DATA PENJUALAN'))
    print('-' * 35)
    penjualan_list = makeList(penjualan_dict)
    Penjualan(penjualan_list)
    print('-' * 35)
    print()
    
    #memanggil fungsi tertinggi
    #dengan return nama penjual
    print("PENJUALAN TERTINGGI: ", tertinggi(penjualan_list))
    print()

    #memanggil fungsi report
    report(penjualan_list)

if __name__ == '__main__':
    main()
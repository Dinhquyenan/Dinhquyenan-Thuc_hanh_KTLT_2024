def dem_chu_cai va chu_so (cau):
    dem _chu_cai sum(c.isalpha() for c in cau) =
    dem_chu_so = sum(c.isdigit() for c in cau)
    return  dem _chu_cai, dem_chu_so
nhap_cau=input ("Enter a sentence: ") =
chu_cai, chu_so=dem_chu_cai_va_chu_so (nhap_cau)
print (f"The number of letters is: (chu_cai}")
print (f"Number of digits is: (chu_so}")

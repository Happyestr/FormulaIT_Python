# TODO Найдите количество книг, которое можно разместить на дискете
memory = 1.44
kol_stran = 100
kol_strok = 50
kol_sim = 25
memory_for_sim = 4

print("Количество книг, помещающихся на дискету:", int((memory*1024*1024) // (memory_for_sim*kol_sim*kol_strok*kol_stran)))

import luas


def test_luas_segitiga():
    result = luas.LuasSegititiga()
    assert result.hitung(10,5)==25 , 'perhitungan salah'
    assert result.hitung(10,-5)==25 , 'input salah'

def test_luas_kubus():
    result = luas_kubus_balok.LuasKubus()
    assert result.hitung_LuasKubus(6)==216, 'perhitungan salah'
    print("Luas Kubus = ", result.hitung_LuasKubus(6))

def test_luas_balok():
    result = luas_kubus_balok.LuasBalok()
    assert result.hitung_LuasBalok(3, 4, 5)==94, 'perhitungan salah'
    print("Luas Balok = ", result.hitung_LuasBalok(3, 4, 5))

test_luas_segitiga()

#test_kubus_balok 
test_luas_kubus()
test_luas_balok()
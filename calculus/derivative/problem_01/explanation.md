## Penjelasan

Turunan suatu fungsi didefinisikan sebagai limit:

$$
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

Definisi ini menyatakan laju perubahan fungsi di suatu titik.

---

## Pendekatan Komputer

Komputer tidak dapat menghitung limit secara langsung.
Oleh karena itu, nilai \( h \) dipilih sangat kecil
untuk mendekati konsep limit.

Pendekatan ini disebut **finite difference**.

Secara numerik, turunan dapat dihampiri dengan:

$$
f'(x) \approx \frac{f(x + h) - f(x)}{h}
$$

---

## Penerapan pada Soal

Pada soal ini:
- Fungsi: \( f(x) = 3x^2 + 2x \)
- Titik evaluasi: \( x = 1 \)
- Nilai \( h \): bilangan kecil (misalnya 0.0001)

Nilai turunan dihitung dengan memasukkan nilai tersebut
ke dalam rumus finite difference.

---

## Hubungan dengan Kode

Pada file `solution.py`:
- Fungsi matematika direpresentasikan sebagai fungsi Python
- Perhitungan turunan dilakukan menggunakan selisih hingga
- Hasil yang diperoleh merupakan aproksimasi nilai turunan

Hasil yang mendekati nilai 8 dianggap benar.

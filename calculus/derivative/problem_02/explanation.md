# Derivative – Problem 02

## Penjelasan

Pada problem ini digunakan pendekatan **turunan numerik** untuk menghitung nilai turunan suatu fungsi di titik tertentu.

---

## Konsep Dasar

Turunan suatu fungsi didefinisikan sebagai limit:

$$
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

Definisi ini menyatakan laju perubahan fungsi terhadap variabelnya.

Namun, komputer tidak dapat menghitung limit secara eksak. Oleh karena itu, nilai ( h ) dipilih sangat kecil untuk mendekati konsep limit tersebut.

Pendekatan ini dikenal sebagai **finite difference (forward difference)**.

---

## Pendekatan Numerik

Secara numerik, turunan dapat dihitung dengan rumus:

$$
f'(x) \approx \frac{f(x + h) - f(x)}{h}
$$

Dengan:

* ( h ) adalah bilangan kecil (misalnya 0.0001)
* Semakin kecil ( h ), semakin mendekati nilai turunan sebenarnya

Namun, jika ( h ) terlalu kecil, error numerik dapat muncul karena keterbatasan presisi komputer.

---

## Penerapan pada Soal

Diketahui fungsi:

$$
f(x) = x^3 - 4x^2 + 2x
$$

Titik evaluasi:

$$
x = 2
$$

Langkah penyelesaian:

1. Mendefinisikan fungsi ( f(x) )
2. Memilih nilai ( h ) kecil
3. Menghitung nilai ( f(2 + h) ) dan ( f(2) )
4. Menghitung selisih hingga untuk memperoleh aproksimasi turunan

---

## Validasi Hasil

Turunan analitik dari fungsi adalah:

$$
f'(x) = 3x^2 - 8x + 2
$$

Nilai eksak di titik ( x = 2 ):

$$
f'(2) = -2
$$

Hasil numerik yang mendekati nilai ini dianggap benar.

---

## Hubungan dengan Kode

Pada file `solution.py`:

* Fungsi matematika direpresentasikan sebagai fungsi Python
* Turunan dihitung menggunakan finite difference
* Hasil numerik dibandingkan dengan nilai analitik untuk melihat error

> Fokus problem ini adalah memastikan **alur konsep → pendekatan numerik → kode** berjalan konsisten.

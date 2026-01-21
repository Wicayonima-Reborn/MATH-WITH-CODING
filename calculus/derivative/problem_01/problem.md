# Derivative – Problem 01

## Soal

Diberikan fungsi:

$$
f(x) = 3x^2 + 2x
$$

Tentukan nilai turunan fungsi tersebut di titik:

$$
x = 1
$$

Gunakan **pendekatan numerik**, bukan rumus turunan langsung.

---

## Tujuan Soal

Soal ini bertujuan untuk:

* Memahami definisi dasar turunan
* Menghubungkan konsep limit dengan implementasi kode
* Melatih cara berpikir numerik (bukan simbolik)

---

## Konsep Matematika

Turunan didefinisikan sebagai:

$$
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

Karena komputer tidak dapat menghitung limit secara langsung, maka:

* Nilai ( h ) dipilih **sangat kecil**
* Pendekatan ini disebut **finite difference**

---

## Langkah Penyelesaian

1. Tentukan fungsi ( f(x) )
2. Pilih titik ( x = 1 )
3. Pilih nilai ( h ) kecil (misalnya 0.0001)
4. Hitung:

$$
\frac{f(1 + h) - f(1)}{h}
$$

Hasil perhitungan ini adalah **aproksimasi** dari nilai turunan di titik tersebut.

---

## Hasil yang Diharapkan

Secara analitik, turunan fungsi adalah:

$$
f'(x) = 6x + 2
$$

Sehingga:

$$
f'(1) = 8
$$

Hasil numerik yang mendekati nilai ini dianggap **benar**.

---

## Catatan

* Selisih kecil dari nilai 8 adalah normal
* Semakin kecil nilai ( h ), semakin akurat hasilnya
* Namun nilai ( h ) yang terlalu kecil dapat menimbulkan error numerik

---

> Fokus soal ini bukan kecepatan atau library,
> tapi memahami **apa itu turunan dan bagaimana komputer menghampirinya**

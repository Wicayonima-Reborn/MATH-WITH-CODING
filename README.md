# Calculus With Code

Repository ini fokus pada **kalkulus dari nol**, ditujukan untuk programmer yang ingin memahami konsep matematika sekaligus implementasinya ke dalam kode.

Bahasa pemrograman yang digunakan:

* Python (utama, dari nol)
* C++ (numerical approach)
* JavaScript (demo visual, opsional)

---

## 1. Apa itu Kalkulus?

Kalkulus adalah cabang matematika yang mempelajari **perubahan** dan **akumulasi**.

Secara garis besar, kalkulus terbagi menjadi:

* **Turunan (Derivative)** → mengukur perubahan
* **Integral** → mengukur akumulasi

Contoh real-life:

* Turunan → kecepatan dari posisi
* Integral → jarak dari kecepatan

---

## 2. Konsep Dasar Fungsi

Sebelum masuk kalkulus, kita butuh fungsi.

Contoh fungsi:

[
f(x) = 3x^2 + 2x
]

Artinya:

* Input: x
* Output: nilai dari rumus

Dalam kode (Python):

```text
f(x) = 3*x*x + 2*x
```

---

## 3. Limit (Fondasi Kalkulus)

Limit menjawab pertanyaan:

> "Jika x mendekati suatu nilai, apa yang terjadi pada f(x)?"

Contoh:

[
\lim_{x \to 2} (3x^2 + 2x)
]

Karena fungsi ini kontinu, kita bisa langsung substitusi:

[
= 3(2)^2 + 2(2) = 16
]

Limit adalah **dasar** dari turunan dan integral.

---

## 4. Turunan (Derivative)

Turunan mengukur **seberapa cepat suatu nilai berubah**.

Definisi matematis:

[
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
]

Untuk fungsi:

[
f(x) = 3x^2 + 2x
]

Turunannya:

[
f'(x) = 6x + 2
]

Makna:

* Jika x = 1 → perubahan = 8
* Jika x besar → perubahan makin besar

---

## 5. Integral (Anti-Turunan)

Integral adalah kebalikan dari turunan.

Jika:

[
f'(x) = 6x + 2
]

Maka:

[
\int (6x + 2) dx = 3x^2 + 2x + C
]

Integral juga bisa diartikan sebagai **luas di bawah kurva**.

---

## 6. Integral Tentu

Integral tentu menghitung nilai **akumulasi dalam rentang tertentu**.

Contoh:

[
\int_0^2 (3x^2 + 2x) dx
]

Hasil manual:

[
= [x^3 + x^2]_0^2 = 12
]

Makna:

* Total akumulasi nilai fungsi dari x=0 sampai x=2

---

## 7. Kenapa Programmer Perlu Kalkulus?

* Game → movement, physics
* AI → gradient descent
* Data → optimisasi
* Grafik → kurva & animasi

Kalau bisa koding **dan** paham kalkulus:

> otak kiri dan kanan nyala barengan

---

## Next Step

Langkah selanjutnya di repo ini:

1. Implementasi fungsi dari nol (Python)
2. Turunan numerik (tanpa library)
3. Integral numerik (trapezoidal & Simpson)
4. Visualisasi integral dengan JavaScript

---

> Fokus repo ini bukan cepat, tapi **paham**.
> Kode boleh sederhana, logika harus jelas.
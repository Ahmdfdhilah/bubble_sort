# Bubble Sort

## Kenapa Bubble Sort memiliki kompleksitas waktu O(n^2)

Karena algoritma menggunakan **Nested Loop** (Loop Bersarang) - loop luar dan dalam untuk membandingkan masing-masing elemen terdekat.

**Note:**
- Loop luar untuk menentukan berapa kali proses penggelembungan dilakukan
- Loop dalam membandingkan dan menukar elemen yang berdekatan

Jadi setiap elemen dibandingkan dengan hampir semua elemen lainnya.

---

## Contoh Analisis

Untuk array dengan 5 elemen:

```
arr = [5, 3, 8, 4, 2]
n = 5
```

### Proses per Pass:
- **Pass 1 (i=0)**: Melakukan (n-1) pembandingan
- **Pass 2 (i=1)**: Melakukan (n-2) pembandingan
- **Pass 3 (i=2)**: Melakukan (n-3) pembandingan
- Dan seterusnya...

### Gambaran Detail:
- **Pass 1 (i=0)**: → 4 perbandingan
- **Pass 2 (i=1)**: → 3 perbandingan
- **Pass 3 (i=2)**: → 2 perbandingan
- **Pass 4 (i=3)**: → 1 perbandingan

**TOTAL** = 4 + 3 + 2 + 1 = **10 perbandingan**

---

## Formula Umum

Bentuk umum: `(n-1) + (n-2) + (n-3) + ... + 2 + 1`

Total perbandingan:
```
Total = n × (n-1) / 2
      = (n^2 - n) / 2
      = 1/2n^2 - 1/2n
```

### Analisis Big O

Dalam analisis Big O, fokus pada **suku dengan pangkat tertinggi**: **n^2**

Oleh karena itu, kompleksitas waktu Bubble Sort adalah **O(n^2)**
# PENJELASAN SETIAP KODE DALAM PEMBUATAN NOTEPAD DENGAN BAHASA PYTHON
## Notepad Sederhana Kelompok 2
##### Ahmad Fadhila G1F022005
##### Citra Safira Irawan G1F022021
##### Dwi Saputra G1F022069

### FITUR DALAM NOTEPAD
- Save
- Open
- Exit
- Undo
- Redo
- Find
- Date

## KEGUNAAN 

- Mengedit Dokumen Sederhana: Notepad digunakan untuk membuat, mengedit, dan menyimpan teks dalam format sederhana.
- Menulis Catatan: Baik itu catatan harian, ide, atau informasi penting lainnya, Notepad memberikan tempat untuk menulis secara cepat.
- Pemrograman: Kadang-kadang digunakan oleh programmer untuk menulis kode sederhana, catatan, atau bahkan skrip kecil.
- Mengedit Berkas Konfigurasi: Digunakan untuk mengedit dan memodifikasi file konfigurasi yang sederhana, seperti file teks biasa.




## Aplikasi yang dibutuhkan


- [https://code.visualstudio.com/] - Apliasi Visual Studio Code
- [https://www.python.org/downloads/windows/] - Python
- [https://github.com/] - Github

## Penjelasan Kode
![image](https://github.com/Ahmadfadhila/UAS-PBO/assets/150579766/dcc82646-38a8-4ce5-82c9-e25815c34fb7)

Kode yang tunjukkan merupakan implementasi sederhana dari aplikasi Notepad menggunakan Tkinter di Python. Ini mencakup beberapa elemen utama:

    tkinter: Modul dasar untuk pembuatan antarmuka grafis (GUI) dalam Python.
    filedialog: Menggunakan dialog file untuk membuka dan menyimpan file.
    scrolledtext: Menyediakan area teks yang bisa digulir untuk menampilkan dan mengedit teks.
    messagebox: Digunakan untuk menampilkan pesan informasi, peringatan, atau kesalahan kepada pengguna.

Aplikasi ini memiliki fungsi dasar seperti membuka dan menyimpan file teks, serta fitur edit sederhana seperti undo, redo, pencarian teks, dan menyisipkan tanggal. Ini adalah kerangka dasar yang dapat diperluas dengan lebih banyak fitur sesuai kebutuhan.

![image](https://github.com/Ahmadfadhila/UAS-PBO/assets/150579766/2ed393e1-1c05-4649-97de-93de112abea3)

Kode tersebut adalah implementasi dari dua fungsi dalam Python menggunakan modul Tkinter:

    save_file(): Fungsi ini bertujuan untuk menyimpan teks yang ada di dalam area teks (dalam konteks ini, mungkin dari sebuah ScrolledText) ke dalam sebuah file. Langkah-langkahnya adalah sebagai berikut:
        file_path = filedialog.asksaveasfilename(...): Ini membuka dialog penyimpanan file yang memungkinkan pengguna memilih atau menentukan lokasi dan nama file yang akan disimpan.
        Jika pengguna memilih file (artinya, file_path tidak kosong), maka fungsi akan membuka file tersebut dengan mode penulisan ('w'), kemudian menulis teks dari text_area ke dalam file yang dipilih.

    open_file(): Fungsi ini bertujuan untuk membuka sebuah file teks yang telah ada dan menampilkannya di dalam area teks (dalam hal ini, mungkin sebuah ScrolledText). Langkah-langkahnya adalah sebagai berikut:
        file_path = filedialog.askopenfilename(...): Ini membuka dialog untuk memilih file yang akan dibuka.
        Jika pengguna memilih file (artinya, file_path tidak kosong), maka fungsi akan membuka file tersebut dengan mode membaca ('r'), membaca teks dari file, menghapus konten yang ada di text_area, dan memasukkan teks dari file ke dalam text_area untuk ditampilkan kepada pengguna.

Kedua fungsi tersebut berguna dalam interaksi antara aplikasi dengan berkas teks, memungkinkan pengguna untuk menyimpan dan membuka berkas teks dari aplikasi yang dibuat menggunakan Tkinter.

![image](https://github.com/Ahmadfadhila/UAS-PBO/assets/150579766/aee1fba6-abe8-4546-8991-ffd3e0be5988)

Kode di atas mengimplementasikan beberapa fungsi yang berkaitan dengan manipulasi teks dan interaksi dengan pengguna di aplikasi menggunakan modul Tkinter:

    undo(): Fungsi ini bertujuan untuk melakukan perintah "undo" pada area teks (misalnya, ScrolledText). Langkah-langkahnya adalah sebagai berikut:
        text_area.edit_undo(): Melakukan operasi "undo" pada area teks. Jika perintah undo tersedia, maka akan mengembalikan keadaan sebelumnya. Jika tidak, akan menampilkan pesan yang memberitahu bahwa tidak ada yang bisa dibatalkan.

    redo(): Fungsi ini bertujuan untuk melakukan perintah "redo" pada area teks. Langkah-langkahnya mirip dengan fungsi undo(), namun kali ini mengeksekusi perintah "redo" jika tersedia.

    find_text(): Fungsi ini membuka jendela pop-up (Toplevel) untuk pencarian teks dalam area teks. Langkah-langkahnya adalah sebagai berikut:
        Membuat jendela pop-up dengan judul "Find" menggunakan tk.Toplevel(root).
        Menambahkan Entry di dalam jendela pop-up, memungkinkan pengguna untuk memasukkan teks yang ingin dicari.
        Ketika tombol "Find" ditekan, fungsi find() akan dijalankan.
        Fungsi find() akan mencari teks yang dimasukkan oleh pengguna di dalam area teks, menyoroti setiap penemuan dengan latar belakang warna merah.

    insert_date(): Fungsi ini bertujuan untuk menyisipkan tanggal saat ini ke dalam area teks. Ini dilakukan dengan membuat variabel string (now) yang berisi tanggal dan waktu saat ini menggunakan tk.Tk().strftime("%Y-%m-%d %H:%M:%S"), lalu memasukkan nilai dari variabel tersebut ke dalam area teks pada posisi terakhir (tk.END).

Secara keseluruhan, fungsi-fungsi tersebut memberikan interaksi tambahan kepada pengguna untuk mengedit, mencari, dan menambahkan konten teks ke dalam area teks yang telah dibuat dalam aplikasi menggunakan Tkinter.

![image](https://github.com/Ahmadfadhila/UAS-PBO/assets/150579766/2aba8bde-ccbc-4952-89e3-f92efcfddf46)

Kode di atas adalah kerangka dasar dari pembuatan aplikasi Notepad sederhana menggunakan Tkinter di Python. Mari kita bahas bagian-bagian utamanya:

    Membuat Jendela Utama (root = tk.Tk()):
        Membuat jendela utama menggunakan modul Tkinter dengan perintah tk.Tk().
        Memberikan judul pada jendela utama dengan menggunakan method root.title("Notepad Kelompok 2").

    Membuat Area Teks yang Dapat Digulir (text_area = scrolledtext.ScrolledText(root, wrap="word")):
        Membuat area teks yang dapat digulir menggunakan scrolledtext.ScrolledText.
        Area teks ini ditempatkan di dalam jendela utama (root) dengan menggunakan text_area.pack(expand=True, fill="both").

    Membuat Menu Bar (menu_bar = tk.Menu(root)):
        Membuat menu bar yang akan berisi menu "File" dan "Edit".

    Menu "File":
        Membuat menu "File" dengan opsi "Open", "Save", sebuah garis pemisah (add_separator()), dan "Exit".
        Setiap opsi memiliki fungsi terkait: membuka file, menyimpan file, keluar dari aplikasi.

    Menu "Edit":
        Membuat menu "Edit" dengan opsi "Undo", "Redo", sebuah garis pemisah, "Find", dan "Date".
        Setiap opsi memiliki fungsi terkait: melakukan undo dan redo, mencari teks, dan memasukkan tanggal.

    Mengonfigurasi Menu Bar:
        Menu "File" dan "Edit" ditambahkan ke dalam menu bar secara hierarkis menggunakan menu_bar.add_cascade(label="File", menu=file_menu) dan menu_bar.add_cascade(label="Edit", menu=edit_menu).
        Menyetel menu bar sebagai menu utama di jendela utama menggunakan root.config(menu=menu_bar).

    Menjalankan Loop Utama (root.mainloop()):
        Mengeksekusi jendela utama dan menjaga aplikasi berjalan, menunggu interaksi dari pengguna.

Kode ini membentuk kerangka dasar dari aplikasi Notepad dengan antarmuka sederhana yang memiliki fungsi dasar seperti membuka, menyimpan, mengedit, dan mencari teks. Ia memanfaatkan widget dari modul Tkinter untuk membuat antarmuka pengguna yang interaktif.





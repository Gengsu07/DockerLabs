# import baseImage
FROM alpine:latest

#membuat direktori
RUN mkdir latihan
# Menulis move some data into a file
RUN echo "This is Sugeng Wahyudi Image" > "latihan/latihan.txt" && echo "Belajar Docker"> "latihan/latihan1.txt"

#memberikan label/informasi metadata tentang image yg kita buat
LABEL pembuat="Sugeng Wahyudi"
LABEL Company="DJP" jabatan="Administrator Sistem"

#menampilkan isi, ist the contents of a file on the standard output
CMD cat "latihan/latihan.txt" "latihan/latihan1.txt"
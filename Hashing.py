CHUNK_SIZE = 1024*1024
file_number = 1
PATH = 'Kho_Gaye_Hum_kahan.mp3'
with open(PATH, 'rb') as f:
    chunk = f.read(CHUNK_SIZE)
    while chunk:
        with open('my_file_part_' + str(file_number) + '.mp3', 'wb') as chunk_file:
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE)

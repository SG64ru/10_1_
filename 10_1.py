# import threading
# import time
# from time import sleep
# from pprint import pprint
# from threading import Thread
#
# time_start_1 = time.time()
# def write_words(word_count, file_name):
#     # time_start = time.time() # Взятие текущего времени
#     with open(file_name, "a", encoding="utf-8") as file: # Объявление функции write_words
#         for i in range(word_count):
#             file.write(f'Какое-то слово № {i + 1}\n')
#             time.sleep(0.1)
#     print(f"Завершилась запись в файл {file_name}")
#     # time_end = time.time()  # Взятие текущего времени завершения
#     # print(time_end - time_start) # время выполнения потока
#
#
#
# write_words(10, "example1.txt")
# write_words(30, "example2.txt")
# write_words(200, "example3.txt")
# write_words(100, "example4.txt")
#
# time_end_1 = time.time()
# print(f"{time_end_1 - time_start_1} общее время функции")
#
#
# time_start_2= time.time()
#
# thread_1 = Thread(target=write_words, args= (10, "example5.txt"))
# thread_2 = Thread(target=write_words, args=(30, "example6.txt"))
# thread_3 = Thread(target=write_words, args=(200, "example7.txt"))
# thread_4 = Thread(target=write_words, args=(100, "example8.txt"))
#
# # time_start = time.time()
# thread_1.start()
# # time_end = time.time()
#
# # print(f"{time_end - time_start} общее время потока")
# # time_start = time.time()
# thread_2.start()
# # time_end = time.time()
#
# # print(f"{time_end - time_start} общее время потока")
# # time_start = time.time()
# thread_3.start()
# # time_end = time.time()
#
# # print(f"{time_end - time_start} общее время потока")
# # time_start = time.time()
# thread_4.start()
# # time_end = time.time()
#
# # print(f"{time_end - time_start} общее время потока")
# thread_1.join()
# thread_2.join()
# thread_3.join()
# thread_4.join()
#
# time_end_2 = time.time()
# print(f"{time_end_2 - time_start_2} общее время  потоков")

import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        voin = 100
        counter = 1
        # counter = 0
        print(f"{self.name} , на нас напали!")
        while voin:
            voin -= self.power
            # counter += 1
            time.sleep(1)
            counter += 1

            print(f"{self.name} сражается {counter} дней, осталось воинов {voin}\n")
            # counter += 1

        else:
            print(f"{self.name} одержал победу спустя {counter}")



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
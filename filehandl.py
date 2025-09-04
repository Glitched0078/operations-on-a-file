file_read = open('trial.txt', 'r')
print("Hello my name is Lucas")
print(file_read.read())
file_read.close()

file_write = open('trial.txt', 'w')
file_write.write("Hi! I live in switzerland.")
file_write.close()

file_append = open('trial.txt', 'a')
file_append.write("\n Hello my name is Lucas")
file_append.write("\n Hi! I live in switzerland.")
file_append.close()
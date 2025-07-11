msg = input('Digite algo: ')
print(f'{type(msg)} \nEstá minúsculo? {msg.islower()} \nÉ apenas espaço? {msg.isspace()} \nÉ um número? {msg.isnumeric()} \nÉ alfabético? {msg.isalpha()}')
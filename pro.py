#Импортируем библиотеку subprocess

# Определяем функцию git_config_list, которая будет выполнять команду Git 
# (нужно в консоль вывести результат работы команды git: git config --global --list)

    # Удаляем заглушку, создаем переменную result:
    # Используем subprocess.run для выполнения команды в переменной result
    # Выводим результат выполнения команды result.stdout
    

# вызываем git_config_list()


import subprocess

def git_config_list():
#    pass

    result = subprocess.run(["git", "config", "--global", "--list"])
    
    print(result.stdout)
    
    
git_config_list()

import logging

# Створення логерів
baseloader_logger = logging.getLogger('baseloader')
coinbaseloader_logger = logging.getLogger('coinbaseloader')

# Встановлення рівня логування
baseloader_logger.setLevel(logging.DEBUG)
coinbaseloader_logger.setLevel(logging.DEBUG)

# Створення формату для логів
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Створення файлового обробника
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Додавання обробника до логерів
baseloader_logger.addHandler(file_handler)
coinbaseloader_logger.addHandler(file_handler)

# Зміна рівня логування для baseloader_logger
baseloader_logger.setLevel(logging.INFO)

# Створення власного формату для логів
class CustomFormatter(logging.Formatter):
    def format(self, record):
        formatted_message = super().format(record)
        return f'[CUSTOM] {formatted_message}'

# Встановлення власного формату для файлового обробника
custom_formatter = CustomFormatter()
file_handler.setFormatter(custom_formatter)

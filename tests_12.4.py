import unittest
import logging
from rt_with_exceptions import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='UTF-8',
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'  # Добавлено время и имя функции
)

class RunnerTest(unittest.TestCase):
    def setUp(self):
        logging.info("Начало выполнения теста")
        
    def tearDown(self):
        logging.info("Завершение теста")
        logging.info("-" * 50)  # Разделитель между тестами

    def test_walk(self):
        logging.info("Запуск test_walk")
        try:
            speed = -5
            name = "Тест"
            logging.info(f"Попытка создания Runner с параметрами: name='{name}', speed={speed}")
            
            runner = Runner(name, speed)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
            
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")
            logging.debug(f"Полное сообщение об ошибке: {str(e)}", exc_info=True)
    
    def test_run(self):
        logging.info("Запуск test_run")
        try:
            invalid_name = 123
            logging.info(f"Попытка создания Runner с параметрами: name={invalid_name}, speed=default")
            
            runner = Runner(invalid_name)
            runner.run()
            logging.info('"test_run" выполнен успешно')
            
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")
            logging.debug(f"Полное сообщение об ошибке: {str(e)}", exc_info=True)

    def test_valid_runner(self):
        logging.info("Запуск test_valid_runner")
        try:
            name = "Валидный бегун"
            speed = 10
            logging.info(f"Попытка создания Runner с корректными параметрами: name='{name}', speed={speed}")
            
            runner = Runner(name, speed)
            runner.walk()
            logging.info(f"Успешно создан Runner: {runner}, текущая дистанция: {runner.distance}")
            
            runner.run()
            logging.info(f"Успешно выполнен бег, новая дистанция: {runner.distance}")
            
        except Exception as e:
            logging.error(f"Неожиданная ошибка: {e}", exc_info=True)

if __name__ == '__main__':
    logging.info("=" * 50)
    logging.info("НАЧАЛО ТЕСТИРОВАНИЯ")
    logging.info("=" * 50)
    unittest.main() 
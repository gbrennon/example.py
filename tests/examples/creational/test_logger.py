from src.examples.creational.logger import Logger

class TestLogger:
    def test_logger(self):
        logger1 = Logger()
        logger2 = Logger()

        assert logger1 is logger2

    def test_log_prints_message(self, capsys):
        # Assert
        logger = Logger()

        # Act
        # Log a message
        # This will be printed to the console
        logger.log('test message')

        # Assert
        captured = capsys.readouterr()
        assert captured.out == 'test message\n'

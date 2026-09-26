from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._counter: int = 0

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            return (-1, "No data to process")
        self._counter += 1
        data = self._storage.pop(0)
        return (self._counter, data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(
            self,
            data: Union[
                int,
                float,
                list[int],
                list[float],
                list[Union[int, float]]
                ]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, (int, float)):
            self._storage.append(str(data))
        else:
            for item in data:
                self._storage.append(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, str):
            self._storage.append(data)
        else:
            for item in data:
                self._storage.append(item)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and
                       isinstance(v, str) for k, v in data.items())
        if isinstance(data, list):
            return all(isinstance(item, dict) and
                       all(isinstance(k, str) and
                           isinstance(v, str) for
                           k, v in item.items()) for item in data)
        return False

    def ingest(
            self,
            data: Union[dict[str, str],
                        list[dict[str, str]]]
                        ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, dict):
            self._storage.append(f"{data.get('log_level', 'UNKNOWN')}:"
                                 f" {data.get('log_message', '')}")
        else:
            for item in data:
                self._storage.append(f"{item.get('log_level', 'UNKNOWN')}:"
                                     f" {item.get('log_message', '')}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    numeric_processor = NumericProcessor()

    print(f" Trying to validate input '42': {numeric_processor.validate(42)}")
    print(f" Trying to validate input 'Hello':"
          f" {numeric_processor.validate('Hello')}")

    try:
        numeric_processor.ingest('foo')
    except ValueError as e:
        print(f" Got exception: {e}")

    numeric_data = [1, 2, 3, 4, 5]
    print(f" Processing data: {numeric_data}")
    numeric_processor.ingest(numeric_data)
    print(" Extracting 3 values...")
    for _ in range(3):
        counter, value = numeric_processor.output()
        print(f" Numeric value {counter - 1}: {value}")

    print("\nTesting Text Processor...")
    text_processor = TextProcessor()
    print(f" Trying to validate input '42': {text_processor.validate(42)}")
    try:
        text_processor.ingest(1337)
    except ValueError as e:
        print(f" Got exception: {e}")

    text_data = ["Hello", "Nexus", "World"]
    print(f" Processing data: {text_data}")
    text_processor.ingest(text_data)
    print(" Extracting 1 value...")
    counter, value = text_processor.output()
    print(f" Text value {counter - 1}: {value}")

    print("\nTesting Log Processor...")
    log_processor = LogProcessor()
    print(f" Trying to validate input 'Hello':"
          f" {log_processor.validate('Hello')}")

    try:
        log_processor.ingest("Not a log entry")
    except ValueError as e:
        print(f" Got exception: {e}")

    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ]
    print(f" Processing data: {log_data}")
    log_processor.ingest(log_data)
    print(" Extracting 2 values...")
    for _ in range(2):
        counter, value = log_processor.output()
        print(f" Log entry {counter - 1}: {value}")


if __name__ == "__main__":
    main()

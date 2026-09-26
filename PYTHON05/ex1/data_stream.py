from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._counter: int = 0

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            return (-1, "No data to process")
        self._counter += 1
        data = self._storage.pop(0)
        return (self._counter, data)

    def total_processed(self) -> int:
        return self._counter + len(self._storage)

    def remaining(self) -> int:
        return len(self._storage)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(
            self,
            data: typing.Union[
                int,
                float,
                list[int],
                list[float],
                list[typing.Union[int, float]]
                ]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, (int, float)):
            self._storage.append(str(data))
        else:
            for item in data:
                self._storage.append(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: typing.Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, str):
            self._storage.append(data)
        else:
            for item in data:
                self._storage.append(item)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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
            data: typing.Union[dict[str, str],
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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            print("DataStream error - Can't register non-DataProcessor")
            return
        for existing_proc in self.processors:
            if isinstance(existing_proc, type(proc)):
                print(f"DataStream error - Processor of type "
                      f"{type(proc).__name__} already registered")
                return
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        if not self.processors:
            print("DataStream error -"
                  " No processor found, can't process stream")
            return
        for item in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - Can't "
                      f"process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            total_processed = proc.total_processed()
            remaining = proc.remaining()
            if isinstance(proc, NumericProcessor):
                print(f"Numeric Processor: total {total_processed} items "
                      f"processed, remaining {remaining} on processor")
            elif isinstance(proc, TextProcessor):
                print(f"Text Processor: total {total_processed} items "
                      f"processed, remaining {remaining} on processor")
            elif isinstance(proc, LogProcessor):
                print(f"Log Processor: total {total_processed} items "
                      f"processed, remaining {remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    data_stream.register_processor(NumericProcessor())

    data = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
            42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

    print("Send the same batch again")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    print("\nConsume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    for proc in data_stream.processors:
        if isinstance(proc, NumericProcessor):
            for _ in range(3):
                proc.output()
        elif isinstance(proc, TextProcessor):
            for _ in range(2):
                proc.output()
        elif isinstance(proc, LogProcessor):
            proc.output()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()

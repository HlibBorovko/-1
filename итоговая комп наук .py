import json

Income_Data = [
    "KNUTE;1101;1001;5",
    "KNUTE;1222;1002;5",
    "KNUTE;1029;1003;20",
    "KNUTE;1040;1004;5",
    "KNUTE;1050;1005;30",
    "KNEU;1100;1006;200",
    "KNEU;1101;1001;6",
    "KNEU;1029;1002;6",
    "KNEU;1040;1003;25",
    "KNEU;1040;1004;25",
    "KNEU;1050;1005;7",
    "KNEU;1100;1006;25"
    "KNU;1101;1001;8",
    "KNU;1222;1002;8",
    "KNU;1029;1003;23",
    "KNU;1040;1004;7",
    "KNU;1050;1005;28",
    "KNU;1100;1006;210",
]

Items_Data = {
    1001: {
        "Name": "Програмно-апаратна організація комп'ютера IBM PC",
        "Author": "П. Нортон",
        "Price": 400
    },
    1002: {
        "Name": "Посібник з експлуатації ПЕОМ IBM PC",
        "Author": "Р. Джордейн",
        "Price": 400
    }, 1003: {
        "Name": "Операційна система MS DOS 3.3",
        "Author": "Р. Джордейн и др",
        "Price": 700
    }, 1004: {
        "Name": "Асемблер для IBM PC",
        "Author": "А. Абель",
        "Price": 400
    }, 1005: {
        "Name": "Мова програмування С",
        "Author": "ПКерніган, Рітчі ",
        "Price": 300
    }, 1006: {
        "Name": "TURBO PASCAL для професіоналів ",
        "Author": "Г. Шилдт",
        "Price": 650
    }
}


class ResultItem:
    def __init__(self, data: str):
        splitted = data.split(";")
        self.name = splitted[0]
        self.item_code = int(splitted[2])
        self.item_name = Items_Data[self.item_code]["Name"]
        self.item_author = Items_Data[self.item_code]["Author"]
        self.item_price = Items_Data[self.item_code]["Price"]
        self.items_count = int(splitted[-1])
        self.tax = self.items_count * 8
        self.total = self.items_count * self.item_price + self.tax

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def toString(self):
        return f"{self.name}\t{self.item_code}\t{self.item_name}\t{self.item_name}\t{self.item_author}\t{self.item_price}\t{self.items_count}\t{self.tax}\t{self.total}"


def main():
    items_list = [ResultItem(i) for i in Income_Data]
    for item in items_list:
        print(item.toString())
    write_to_file(items_list, "json")


def write_to_file(data_array, mode='s'):
    s = ''
    for item in data_array:
        if mode == 's':
            s += item.toString() + "\n"
        elif mode == 'json':
            s += item.toJson() + "\n"
    with open('result.txt', 'w+', encoding='utf-8') as file:
        file.write(s)


if __name__ == "__main__":
    main()

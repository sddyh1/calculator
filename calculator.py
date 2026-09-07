import re


class Calculator:
    def evaluate(self, text: str) -> float:
        if not re.fullmatch(r"[0-9+\-*/(). ]+", text):
            raise ValueError("Разрешены только цифры, + - * / ( )")
        return eval(text)


def main():
    calc = Calculator()
    while True:
        text = input("calc> ").strip()
        if text in ("exit", "quit"):
            break
        if not text:
            continue
        try:
            print(calc.evaluate(text))
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
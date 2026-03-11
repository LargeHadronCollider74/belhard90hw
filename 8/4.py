'''

Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде дух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
'''

def CurrencyFormat(value:float, currencycode:str = "BIN") -> str:

    round_val = str(round(value, 2))
    amount, rest = "", ""
   
    try:
        amount, rest = round_val.split(".")
    except:
        amount = round_val
        pass

    return f"{" ".join([amount[::-1][i:i+3][::-1] for i in range(0, len(amount), 3)][::-1])}.{rest.zfill(2)} {currencycode}"

print(CurrencyFormat(12245))
print(CurrencyFormat(1234567.9827634))

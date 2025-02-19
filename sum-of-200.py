# Программа решает поставленную задану, но при этом все функции, константы и перечисления можно
# инкапсулировать в класс состояния, если его нужно будет встроить в часть какого-то большого кода.

from enum import Enum

class Operation(Enum):
    NONE = "_" # Услованое обозначение, что между цифрами ничего и их стоит обрабатывать как единое число
    PLUS = "+"
    MINUS = "-"
    def next(self):
        return ORDER[(ORDER.index(self) + 1) % len(ORDER)]

ORDER = [Operation.NONE, Operation.PLUS, Operation.MINUS]    
    
SUM_FOR_TASK = 200
ALL_DIGITS = [i for i in range(9,-1,-1)]

ZERO_STATE = ORDER[0].value.join(map(str, ALL_DIGITS)) # строка 9_8_7_6_5_4_3_2_1_0 в нашем случае
END_STATE = ORDER[-1].value.join(map(str, ALL_DIGITS)) # строка 9-8-7-6-5-4-3-2-1-0 в нашем случае

def sumOfState(state): # Возращает сумму состояния
    totalSum = 0
    currOperation = Operation.PLUS.value
    currStrNumber = ''
    for i in range(len(state)):
        if not (state[i] in ZERO_STATE):
            totalSum += int(currOperation + currStrNumber) # Оператор у нас меняет знак числа (Пока операторы это + и -, 
                                                           # при маштабировании операторов формула будет другая)
            currStrNumber = ''
            currOperation = state[i]
        else:
            if state[i] != Operation.NONE.value: # Таким образом мы пропускаем ненужный символ пустоты
                currStrNumber += state[i]
    totalSum += int(currOperation + currStrNumber) # Дополнительная обработкеа последнего числа 
    return totalSum

def incState(state): # Возвращается следующие состояние
    for i in range(1,len(state), 2):
        currOperation = Operation(state[i])
        nextOperation = currOperation.next()
        state = state[:i] + nextOperation.value + state[i+1:]
        if nextOperation != Operation.NONE:
            break
    return state

def main(): # Главная функция, которая выводит состояния, сумма которых SUM_FOR_TASK
    currState = incState(ZERO_STATE)
        
    while(currState != END_STATE):
        if (sumOfState(currState) == SUM_FOR_TASK):
            print(currState.replace(Operation.NONE.value, "")) # Убираем все знаки Operation.NONE
        currState = incState(currState)

if __name__ == "__main__":
    main()








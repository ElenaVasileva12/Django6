# семинар 4

# Доработаем задачу про броски монеты, игральной кости и
# случайного числа.
# Создайте форму, которая предлагает выбрать: монета, кости,
# числа.
# Второе поле предлагает указать количество попыток от 1 до 64.

# Доработаем задачу 1.
# Создайте представление, которое выводит форму выбора.
# В зависимости от переданных значений представление
# вызывает одно из трёх представлений, созданных на
# прошлом семинаре (если данные прошли проверку, конечно
# же).

from django import forms

class GameCoinForm(forms.Form):
    game=forms.ChoiceField(choices=(('coin','Монетка'),('dice','Кости'),('number','Случайное число')))
    size=forms.IntegerField(min_value=1, max_value=64)


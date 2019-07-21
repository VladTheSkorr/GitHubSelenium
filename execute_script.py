from selenium import webdriver
import  math

# Посчитать математическую функцию от x.
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

# Открыть страницу https://SunInJuly.github.io/execute_script.html
browser.get('https://SunInJuly.github.io/execute_script.html')

# Считать значение для переменной x
valueX = browser.find_element_by_id('input_value').text

# Ввести ответ в текстовое поле.
browser.find_element_by_id('answer').send_keys(calc(valueX))

# Проскроллить страницу вниз.
browser.execute_script('return arguments[0].scrollIntoView(true);', browser.find_element_by_tag_name('button'))

# Выбрать checkbox "Подтверждаю, что являюсь роботом". Переключить radiobutton "Роботы рулят!".Нажать на кнопку "Отправить".
for selector in ['#robotCheckbox', '#robotsRule', 'button.btn.btn-default']:
  browser.find_element_by_css_selector(selector).click()
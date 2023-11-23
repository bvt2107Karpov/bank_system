import code_confirm
import random

a = str(input('ваша почта - '))
b = random.randint(100, 999)

code_confirm.send_email_code(a, b)
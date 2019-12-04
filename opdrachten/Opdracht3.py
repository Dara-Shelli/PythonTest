recipients = ['b44 44 4rt  ', 'Wou uuT3R', '  4l 3x', ' K 3 n 4n', '54R4h']

for element in recipients:
    element_index = recipients.index(element)
    element = element.replace('0', 'o').replace('3', 'e').replace('5', 's').replace('4', 'a')
    element = element.replace(' ', '')
    element = element.capitalize()
    recipients[element_index] = element
print(recipients)

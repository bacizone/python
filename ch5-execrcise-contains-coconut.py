smoothies = [
    'coconut', 
    'strawberry', 
    'banana', 
    'tropical', 
    'acai berry']

has_coconut = [True,
                False,
                False,
                True,
                False]

#i = 0
#while i < len(has_coconut):
#    if has_coconut[i]:
#      print(smoothies[i],'contains coconut')
#    i = i + 1

# length = len(smoothies)
# for i in range(length):
#     print('Smoothie #', i, smoothies[i])

for smoothie in smoothies:
    output = 'We serve ' + smoothie
    print(output)


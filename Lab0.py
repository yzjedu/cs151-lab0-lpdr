import time

#prints texts with a slight delay
def print_text_animation(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.1)
    print()#new line

print('Donovan Raymond')
print('Donovan knows how to dance his fingers between violin strings and guitar cords.')
print('With a blistering mile time of 5:50, Donovan’s strides feel like a sprint even over long distances.')
print('Seven months ago, Donovan faced the challenge of a torn meniscus.')
print('While Donovan has explore parts of North America, a world of continents awaits his discovery.')
print("Donovan's father speaks the language of machines, he knows C++ and python.")

print('CS151 Lab 0')
print('Lucas Podowski')
print('Lucas carves through the winter wonderlands on his snowboard.')
print('Lucas embraces fitness and vitality through regular exercise.')
print('Lucas immerses himself in the world of circuits, where he struggles daily with the age old dilemma,\n'
      'do I calculate the current with calc or drop out like a voltage cause I cant handle my current work load.')
print('Lucas has yet to ever leave the continent')
print('Lucas loves to lay among the leaves that paint the outdoors')
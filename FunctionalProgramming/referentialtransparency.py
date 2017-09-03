# class Speaker():
#
#     def __init__(self,name):
#         self._name = name
#
#     def speak(self, text):
#         print('[%s] %s' %((self._name, text))
#
#
#
#
# Speaker('John')

# Stateless implementation

def speak(speaker,text):
    print('[%s] %s' % (speaker, text))


john = 'John'
speak(john, 'Stateless')
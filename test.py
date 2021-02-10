class bee(object):
    def __init__(self):
        def say_my_name (self, name):
            return name

        setattr(bee, f'Jim_name', property(lambda self: say_my_name(self, 'Jim')))
        setattr(bee, f'Jill_name', property(lambda self: say_my_name(self, 'Jill')))

for name in ['Jake', 'Jordan']:
    setattr(bee, f'{name}_name', property(lambda self, name=name: say_my_name(self, name)))


buzz = bee()

print(buzz.Jim_name)
# >Jim
print(buzz.Jill_name)
# >Jill
print(buzz.Jake_name)
# >Jordan
print(buzz.Jordan_name)
# >Jordan
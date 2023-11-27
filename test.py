class ClassA:
        def __init__(self):
                self.variable_in_class_a = "I am a variable in ClassA."

class ClassB:
        def __init__(self, object_of_class_a):
                self.object_of_class_a = object_of_class_a

        def use_variable_from_class_a(self):
                print(self.object_of_class_a.variable_in_class_a)









ClassB(ClassA()).use_variable_from_class_a()
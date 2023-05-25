init_code = """
if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car' class?")

Car = USER_GLOBAL['Car']

if not "my_car" in USER_GLOBAL:
    raise NotImplementedError("Dude, where is 'my_car'?")

my_car = USER_GLOBAL['my_car']

if not isinstance(my_car, Car):
    raise TypeError("'my_car' should be an instance of 'Car' class")


if not hasattr(Car, "wheels"):
    raise AttributeError("Where is 'wheels' attribute of 'Car' class?")

if not hasattr(Car, "doors"):
    raise AttributeError("Where is 'doors' attribute of 'Car' class?")

if Car.wheels != "four":
    raise ValueError("'wheels' attribute should be equal 'four'")
    
if Car.doors != 4:
    raise ValueError("'doors' attribute should be equal 4")


if not '__init__' in vars(Car):
    raise NotImplementedError("Where is '__init__' method of 'Car' class?")

from inspect import signature

params = signature(Car.__init__).parameters
if not all((len(params) ==  3, 'self' in params, 'brand' in params, 'model' in params)):
    raise NotImplementedError("Check the number and names of '__init__' arguments")

if my_car.brand != "" or my_car.model != "":
    raise Warning("'my_car' must have default values as 'brand' and 'model'")
    
if not "some_car1" in USER_GLOBAL:
    raise NotImplementedError("Where is 'some_car1'?")

some_car1 = USER_GLOBAL['some_car1']

if not isinstance(some_car1, Car):
    raise TypeError("'some_car1' should be an instance of 'Car' class")

if not hasattr(some_car1, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'some_car1'?")
    
if not isinstance(some_car1.brand, str):
    raise TypeError("'brand' attribute of 'some_car1' should be of type 'str'")

if not some_car1.brand:
    raise ValueError("Set distinct (!='') value of 'some_car1' 'brand'")

if not hasattr(some_car1, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'some_car1'?")

if not isinstance(some_car1.model, str):
    raise TypeError("'model' attribute of 'some_car1' should be of type 'str'")

if not some_car1.model:
    raise ValueError("Set distinct (!='') value of 'some_car1' 'model'")

if not "some_car2" in USER_GLOBAL:
    raise NotImplementedError("Where is 'some_car2'?")

some_car2 = USER_GLOBAL['some_car2']

if not isinstance(some_car2, Car):
    raise TypeError("'some_car2' should be an instance of 'Car' class")

if not hasattr(some_car2, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'some_car2'?")
    
if not isinstance(some_car2.brand, str):
    raise TypeError("'brand' attribute of 'some_car2' should be of type 'str'")

if not some_car2.brand:
    raise ValueError("Set distinct (!='') value of 'some_car2' 'brand'")

if not hasattr(some_car2, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'some_car2'?")

if not isinstance(some_car2.model, str):
    raise TypeError("'model' attribute of 'some_car2' should be of type 'str'")

if not some_car2.model:
    raise ValueError("Set distinct (!='') value of 'some_car2' 'model'")
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
        "Basics": [
        prepare_test(middle_code='''''',
                     test="Car.wheels",
                     answer="four"),
        prepare_test(middle_code='''''',
                     test="Car.doors",
                     answer=4)],
}
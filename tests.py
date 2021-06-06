from serializers.serializer_factory.serializer_factory import SerializerFactory
import pytest
from car import *

factory = SerializerFactory()

name = "Toyota"
arg2 = 4


def test_object(form: str):
    serializer = factory.get_serializer(form)
    car = Car()
    car.model = "Q8"
    obj = serializer.loads(serializer.dumps(car))
    assert obj.text == car.text
    assert obj.model == car.model
    assert obj.info(obj) == car.info()
    serializer.dump(car, "cars." + form)
    obj_file = serializer.load("cars." + form)
    assert obj_file.text == car.text
    assert obj_file.model == car.model
    assert obj_file.info(obj) == car.info()
    

def test_class(form: str):
    clas = Car
    serializer = factory.get_serializer(form)
    obj = serializer.loads(serializer.dumps(clas))
    car = Car()
    car.model = "Q8"
    carr = obj()
    carr.model = "Q8"
    assert carr.info() == car.info()
    assert carr.text == car.text


def test_list(form: str):
    serializer = factory.get_serializer(form)
    car = Car()
    car.model = "Q8"
    car.size = [4998, 2011, 1706]
    car.dictionary = {"Doors": 5, "Seats": 5}
    car.previous = Car()
    car.previous.text = "Audi"
    car.previous.model = "Q7"
    car2 = Car()
    car2.model = "Q3"
    car2.size = [4484, 2024, 1616]
    obj_list = serializer.loads(serializer.dumps([car, car2]))
    assert obj_list[0].text == car.text
    assert obj_list[0].model == car.model
    assert obj_list[0].size == car.size
    assert obj_list[0].dictionary == car.dictionary
    assert obj_list[0].previous.text == car.previous.text
    assert obj_list[0].previous.model == car.previous.model
    assert obj_list[0].info(obj_list[0]) == car.info()
    assert obj_list[1].text == car2.text
    assert obj_list[1].model == car2.model
    assert obj_list[1].size == car2.size
    assert obj_list[1].info(obj_list[1]) == car2.info()
    serializer.dump([car, car2], "cars." + form)
    obj_list_file = serializer.load("cars." + form)
    assert obj_list_file[0].text == car.text
    assert obj_list_file[0].model == car.model
    assert obj_list_file[0].size == car.size
    assert obj_list_file[0].dictionary == car.dictionary
    assert obj_list_file[0].previous.text == car.previous.text
    assert obj_list_file[0].previous.model == car.previous.model
    assert obj_list_file[0].info(obj_list_file[0]) == car.info()
    assert obj_list_file[1].text == car2.text
    assert obj_list_file[1].model == car2.model
    assert obj_list_file[1].size == car2.size
    assert obj_list_file[1].info(obj_list_file[1]) == car2.info()


def function(text):
    print(f"The car is {text} and {name}.")


def test_function(form: str):
    serializer = factory.get_serializer(form)
    obj = serializer.loads(serializer.dumps(function))
    assert function("Audi") == obj("Audi")
    serializer.dump(function, "cars." + form)
    obj = serializer.load("cars." + form)
    assert function("Audi") == obj("Audi")


def test_list_function(form: str):
    function2 = lambda arg1: arg1 ** arg2
    serializer = factory.get_serializer(form)
    obj = serializer.loads(serializer.dumps([function, function2]))
    assert obj[0]("Audi") == function("Audi")
    assert obj[1](3) == function2(3)


@pytest.mark.json
def test_json_object():
    test_object("json")
    
@pytest.mark.pickle
def test_pickle_object():
    test_object("pickle")
    
@pytest.mark.toml
def test_toml_object():
    test_object("toml")
    
@pytest.mark.yaml
def test_yaml_object():
    test_object("yaml")

@pytest.mark.json
def test_json_list():
    test_list("json")
    
@pytest.mark.pickle
def test_pickle_list():
    test_list("pickle")
    
@pytest.mark.toml
def test_toml_list():
    test_list("toml")

@pytest.mark.yaml
def test_yaml_list():
    test_list("yaml")
    
@pytest.mark.json
def test_json_function():
    test_function("json")
    
@pytest.mark.pickle
def test_pickle_function():
    test_function("pickle")

@pytest.mark.toml
def test_toml_function():
    test_function("toml")
    
@pytest.mark.yaml
def test_yaml_function():
    test_function("yaml")

@pytest.mark.json
def test_json_list_function():
    test_list_function("json")
    
@pytest.mark.pickle
def test_pickle_list_function():
    test_list_function("pickle")
    
@pytest.mark.toml
def test_toml_list_function():
    test_list_function("toml")
    
@pytest.mark.yaml
def test_yaml_list_function():
    test_list_function("yaml")

@pytest.mark.json
def test_json_class():
    test_class("json")
    
@pytest.mark.pickle
def test_pickle_class():
    test_class("pickle")
    
@pytest.mark.toml
def test_toml_class():
    test_class("toml")
    
@pytest.mark.yaml
def test_yaml_class():
    test_class("yaml")

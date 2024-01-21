import inspect
import pytest
import student

def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in dir(student), reason=f'Skipped because {class_name} has not been defined')

def has_property(cls, *, property_name):
    if not hasattr(cls, property_name):
        return False
    prop = getattr(cls, property_name)
    if type(prop) is not property:
        return False
    return True

def has_method(cls, *, method_name, parameter_names=None):
    if parameter_names is None:
        parameter_names = []
    method = getattr(cls, method_name)
    if not inspect.isfunction(method):
        return False
    specs = inspect.getfullargspec(method)
    if specs.args != parameter_names:
        return False
    return True

@pytest.mark.parametrize("kwargs", [
    {
        'method_name' : 'csom',
        'parameter_names' : ['n'],
    }
])
def test_csom(kwargs):
    assert has_method(
        student,
        **kwargs) , f"Method {kwargs['method_name']} is missing or incorrect."
    
@pytest.mark.parametrize("kwargs", [
    {
        'method_name' : 'isPalindrome',
        'parameter_names' : ['t'],
    }
])
def test_isPalindrome(kwargs):
    assert has_method(
        student,
        **kwargs) , f"Method {kwargs['method_name']} is missing or incorrect."

def test_class_Attraction_is_defined():
    assert 'Attraction' in dir(student), 'Class Attraction has not been defined'

@if_class_exists('Attraction')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name', 'height']
    },
    {
        'method_name': 'visit',
        'parameter_names': ['self', 'height'],
    },
])
def test_attraction_methods(kwargs):
    assert has_method(
        student.Attraction,
        **kwargs), f"Attraction's method {kwargs['method_name']} is missing or incorrect."

@if_class_exists('Attraction')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'name',
    },
    {
        "property_name": 'height',
    },
])
def test_attraction_properties(kwargs):
    assert has_property(student.Attraction, **kwargs), f"Attraction's property {kwargs['property_name']} is missing or incorrect"

def test_class_ThemePark_is_defined():
    assert 'ThemePark' in dir(student), 'Class ThemePark has not been defined'

@if_class_exists('ThemePark')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name']
    },
    {
        'method_name': 'addAttraction',
        'parameter_names': ['self', 'attraction'],
    },
    {
        'method_name': 'printOverview',
        'parameter_names': ['self'],
    },
])
def test_themepark_methods(kwargs):
    assert has_method(
        student.ThemePark,
        **kwargs), f"ThemePark's method {kwargs['method_name']} is missing or incorrect."

@if_class_exists('ThemePark')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'name',
    },
])
def test_pretpark_properties(kwargs):
    assert has_property(student.ThemePark, **kwargs), f"ThemePark's property {kwargs['property_name']} is missing or incorrect"

@if_class_exists('ThemePark')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': 'securityupdate',
        'parameter_names': ['self','file']
    },
])
def test_themepark_uitbreiding(kwargs):
    assert has_method(
        student.ThemePark,
        **kwargs), f"ThemePark's method {kwargs['method_name']} is missing or incorrect."
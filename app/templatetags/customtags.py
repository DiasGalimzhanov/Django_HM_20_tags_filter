from django import template

register = template.Library()

@register.filter
def rounded_value(value, args=2):
    return round(value, args)

@register.filter
def country(value: dict, args: None) -> str:
    if args == 'country':
        return f"Name: {value['name']} | Age: {value['age']} | City: {value['city']} | Country: {value.get('country', 'Country not found')}"
    else:
        return f"Name: {value['name']} | Age: {value['age']} | City: {value['city']} /n"
    
@register.simple_tag
def add(name, city):
    return name + city

@register.simple_tag
def name(name):
    return name.capitalize()

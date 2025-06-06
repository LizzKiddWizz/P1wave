from h2o_wave import ui
from types import SimpleNamespace

component_counter = {'count': 0}

def assign_names(obj, prefix='auto_item'):
    if isinstance(obj, list):
        for item in obj:
            assign_names(item, prefix)
    elif isinstance(obj, (dict, SimpleNamespace)):
        items = obj.values() if isinstance(obj, dict) else vars(obj).values()
        for val in items:
            assign_names(val, prefix)
    elif hasattr(obj, 'dict'):
        if hasattr(obj, 'name') and (not getattr(obj, 'name', None)):
            componentcounter['count'] += 1
            obj.name = f'{prefix}{component_counter["count"]}'
        for attr_name in dir(obj):
            if attr_name.startswith('__'):
                continue
            attr_val = getattr(obj, attr_name)
            assign_names(attr_val, prefix)
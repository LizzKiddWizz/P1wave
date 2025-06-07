
def assign_names(page):
    counter = [1]

    def assign(component):
        if isinstance(component, dict):
            if 'name' not in component and 'type' in component:
                component['name'] = f'auto_item_{counter[0]}'
                counter[0] += 1
            for value in component.values():
                assign(value)
        elif isinstance(component, list):
            for item in component:
                assign(item)

    assign(page)
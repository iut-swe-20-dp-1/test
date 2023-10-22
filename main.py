def add_value_to_stack(stack_list):
    if len(stack_list) > 10:
        raise ValueError("A maximum of 10 values can be added")
    return {"stack": stack_list}

print(add_value_to_stack([1,2,3])

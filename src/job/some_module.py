def convert_to_int(value):
    if isinstance(value,int):
        return value
    elif isinstance(value,float):
        return int(value)
    elif isinstance(value,str):
        value = value.replace(',',').replace('.','')
        return value
    else:
        print('No valid value to transform')


exception_mapping = {
    ValueError: 'UnsupportedValueError',
    KeyError: 'NonExistedKeyError'
}
exc=ValueError()
print( type(exc) in exception_mapping)
## Programming Challenge 3

def get_value(nested_object, nested_key):
    object_value = nested_object
    for key in nested_key:
        object_value = object_value.get(key, None)
        if object_value is None:
            return None
    return object_value


## To test enter object and key like below syntax
# print(get_value(anyobject,[key]))

##Valid Key Test case
print(get_value({"a": {"b": {"c": "d"}}}, ["a", "b", "c"]))
print(get_value({"x": {"y": {"z": "a"}}}, ["x", "y", "z"]))

print(get_value({
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}, ["glossary", "title"]))

##Invalid Key Test
print(get_value({"a": {"b": {"c": "d"}}}, ["a", "b", "d"]))
print(get_value({"x": {"y": {"z": "a"}}}, ["x", "d", "z"]))
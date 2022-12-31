print("dataclasses-dynamodb")

@dataclasses-dynaomdb
# @dataclasses-json
@fastclasese-json
@dataclasses
class Person():
    name: str

me = Person().from_dict({'name': 'Ian'})
me.put()

me_from_dynamodb = Person.get(me.index())
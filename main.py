print("dataclasses-dynamodb")

db = dataclasses-dynamodb.Dynamo(table='mytable')
db.create()

@dataclasses-dynaomdb(db)
@fastclaseses-json  # or @dataclasses-json
@dataclasses
class Person():
    name: str
    children: Optional[List[Person]] = None


me = Person.from_dict({'name': 'Ian'}).put()
me_from_dynamodb = Person.get(me.index())

people = Person.list()
person = {
    "name": "John Doe",
    "age": 17,
    "adress": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "postal_code": "12345"
    },
    "contact": [
        {
        "type": "email",
        "value": "johndoe@example.com"
        },
        {
            "type": "phone",
            "value": [
                {
                    "type": "phone",
                    "value": "13221321"
                }
            ]
        },

    ]
}

print(person["name"])
print(person["age"])
print(person["adress"]["city"])
print(person["contact"][1]["value"])

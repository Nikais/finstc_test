# JSON-SCHEMA
## GET /api/car/
This method return list of cars  
Parameters: None  
Return: List of Cars

```json
[
    {
        "id": 6,
        "vin": "1234567890qwertyu",
        "brand": 1,
        "mark": "Corolla",
        "year": 1999,
        "price": 100000,
        "dealer": 2
    },
    {
        "id": 7,
        "vin": "1234567890qwertya",
        "brand": 1,
        "mark": "Camry",
        "year": 2007,
        "price": 2000000,
        "dealer": null
    }
]
```

## POST /api/car/\<id\>/
This method for create Car object  
Parameters: fields of Car  
Return: Car object
```json
{
    "id": 6,
    "vin": "1234567890qwertyu",
    "brand": 1,
    "mark": "Corolla",
    "year": 1999,
    "price": 100000,
    "dealer": 2
}
```

## PUT /api/car/\<id\>/
Parameters: one or all fields of Car  
Return: Car object
```json
{
    "id": 6,
    "vin": "1234567890qwertyu",
    "brand": 1,
    "mark": "Camry",
    "year": 1999,
    "price": 100000,
    "dealer": 2
}
```

## DELETE /api/car/\<id\>/
Delete Car object by ID  
Parameters: None
Return: None

## GET /api/brand/
This method return list of brands  
Parameters: None  
Return: List of Brands

```json
[
    {
        "id": 6,
        "name": "Toyota"
    },
    {
        "id": 7,
        "name": "Lexus"
    }
]
```

## POST /api/brand/\<id\>/
This method for create Brand object  
Parameters: fields of Brand  
Return: Brand object
```json
{
    "id": 8,
    "vin": "Mercedes-Benz"
}
```

## PUT /api/brand/\<id\>/
Parameters: one or all fields of Brand  
Return: Brand object
```json
{
    "id": 8,
    "vin": "Toyota"
}
```

## DELETE /api/brand/\<id\>/
Delete Brand object by ID  
Parameters: None  
Return: None

## GET /api/dealer/
This method return list of dealers  
Parameters: None  
Return: List of Dealers

```json
[
    {
        "id": 6,
        "name": "Toyota Center Moscow"
    },
    {
        "id": 7,
        "name": "Lexus Official Dealer"
    }
]
```

## POST /api/dealer/\<id\>/
This method for create Dealer object  
Parameters: fields of Dealer  
Return: Dealer object
```json
{
    "id": 8,
    "vin": "Toyota Center in Saint-Petersburg"
}
```

## PUT /api/dealer/\<id\>/
Parameters: one or all fields of Dealer  
Return: Dealer object
```json
{
    "id": 8,
    "vin": "Toyota Center Ladojsky"
}
```

## DELETE /api/dealer/\<id\>/
Delete Dealer object by ID  
Parameters: None  
Return: None

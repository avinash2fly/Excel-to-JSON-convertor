# Excel-to-JSON-convertor

It can convert Excel to JSON with two level of header.

## Steps

### Change Varibles

#### Assign respective Value for the given two variable

>excelFile : Contains the Name of the Excel File to be Used

example : 

```python
excelFile = "abc.xls"
```

>worksheet : Contains the Name of the worksheet Excel File to be Used

example : 

```python
worksheet = "Sheet1"
```

### Example 

#### excel data, to see data open abc.xlsx

|     |                   |            |           | 
|-----|-------------------|------------|-----------| 
| N/A | N/A               | Name       | Name      | 
| id  | email             | first Name | last Name | 
| 123 | avinash2fly@gmail | Avinash    | Gupta     | 


1) N/A : if no master header or just one header
2) Put same master header, if the master header composed of multiple header

example : 
|	     |		 |
|------------|-----------| 
| Name       | Name      | 
| first Name | last Name | 
| Avinash    | Gupta     | 

#### run file
>python3 convertor.py

### ouput in element.json

```json
{
	"data": [
		{
			"id": 123,
			"email": "avinash2fly@gmail",
			"Name": {
				"first Name": "Avinash",
				"last Name": "Gupta"
			}
		}
	]
}
```




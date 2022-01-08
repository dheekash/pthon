product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}

new_list = []

for key, value in product_info.items():
	new_list.append([key, value])

print(new_list)

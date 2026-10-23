def parse_inventory_record(csv_line):
    fields = csv_line.split(",")

    if len(fields) != 3:
        print("Invalid Record")
    else:
        product = fields[0]
        sku = fields[1]
        quantity = fields[2]

        print(
            f"Product: {product} | SKU: {sku} | Qty: {quantity}"
        )


csv_line = input("Enter inventory record: ")
parse_inventory_record(csv_line)
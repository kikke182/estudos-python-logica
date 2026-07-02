# -------------------------------------------------------------------------
# PROJECT 02 - Receipt Generator
# -------------------------------------------------------------------------
client_name = "john"
service_description = "Home remodeling at 367, labor only!"
total_price = "500"

receipt_details = (
    f"Service: {service_description}\n"
    f"Provided by: {client_name.title()}\n"
    f"Total Amount: R${total_price}"
)

print(receipt_details)

name=input("customer name:")

product_1=input("product:")
price_1=float(input("price:"))
quantity_1=int(input("no_of_products:"))

product_2=input("product:")
price_2=float(input("price:"))
quantity_2=int(input("no_of_products:"))

product_3=input("product:")
price_3=float(input("price:"))
quantity_3=int(input("no_of_products:"))

cost_of_product_1=(price_1*quantity_1)
cost_of_product_2=(price_2*quantity_2)
cost_of_product_3=(price_3*quantity_3)

subtotal=cost_of_product_1+cost_of_product_2+cost_of_product_3

discount=int(input("enter dicount="))
discount_amount=(subtotal*discount)/100

amount_after_discount=subtotal-discount_amount
gst=(amount_after_discount*18)/100

bill=amount_after_discount+gst

print("====================shopping bill======================")

print(f"customer={name}")
print(f"{product_1} : {price_1} *{cost_of_product_1}={cost_of_product_1}")
print(f"{product_2} : {price_2} *{cost_of_product_2}={cost_of_product_2}")
print(f"{product_3} : {price_3} *{cost_of_product_3}={cost_of_product_3}")

print(f"subtoal={subtotal}")
print(f"discount amount={discount_amount}")
print(f"amount after discount={amount_after_discount}")
print(f"gst(18%)={gst}")
print(f"your bill with gst is {bill}")




"""
write a function called linear_search_product that takes the list of products and a target product
name is input. the function should perform a linear search to find the target product in the list and 
return a list of indices of all occurrences of the product if found, or an empty list if the product is not
found.
"""
  
def linearsearchproduct(product_list, target_product):
  
    indices = []
  
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index) 

    return indices 
  
# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = "apple"
result = linearsearchproduct(products, target)
print(result)

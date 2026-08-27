product_names=[]
product_prices=[]
product_qty=[]
while True:
       print("="*45)
       print("PRODUCT INVENTORY SYSTEM")
       print("="*45)
       print("1. Insert product")
       print("2. Delete product")
       print("3. Update product price")
       print("4. Traverse / Display All products")
       print("5. Search product(by name)")
       print("6. Sort products by price(ascending)")
       print("7. Sort products by price(descending)")
       print("8. Sort products by price(alphabetical))")
       print("9. Show costliest/Cheapest product")
       print("10.Exit")
       print("="*45)
       choice=input("Enter your choice(1-10): ").strip()
       if choice=='1':
              name=input("Enter product name:").strip()  
              if name in product_names:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                  print(f"product '{name}' already exists!Use update option instead.\n")
              else:
                price=float(input(f"Enter price  for {name}: "))
                qty=float(input(f"Enter qty for {name}: "))
                product_names.append(name)
                product_prices.append(price)
                product_qty.append(qty)
                print(f"Record for '{name}' inserted successfully.\n")
       elif choice== '2':
              name=input("Enter product name to delete: ").strip()
              if name in product_names :
                index=product_names.index(name)
                product_names.pop(index)
                product_prices.pop(index)
                product_qty.pop(index)
              if name in product_names :
                print(f"product'{name}'deleted successfully.\n")
              else:
                print(f"product'{name}'not found")

       elif choice=='3':
              name=input("Enter product name to update: ").strip()
              if name in product_names:
                     index=product_names.index(name)
                     new_price=float(input(f"enter new price for {name}:"))
                     product_prices[index] = new_price
                     print(f"pricess for'{name}'updated successfully.\n")
              else:
                print(f"product'{name}' not found.\n")
       elif choice== '4':
              if len (product_names)==0:
                     print("No records to display.\n")
              else:
                     print("\n {:<5} {:<20} {:<10} {:<10}".format("No.","Name","price","qty"))
                     print("-"*45)
                     for i in range(len(product_names)):
                            print(" {:<5} {:<20} {:<10} {:<10}".format(i+1,product_names[i],product_prices[i],product_qty[i]))
                            print()
       elif choice== '5':
              name=input("Enter product name to search: ").strip()
              if name in product_names:
                     index=product_names.index(name)
                     print(f"{name} -> name:{product_names[index]}, price:{product_prices[index]},qty:{product_qty[index]}")
              else:
                     print(f"product'{name}' not found.\n")
       elif choice== '6':
              if len (product_names)==0:
                            print("No products to sort.\n")
              else:
                     combined=list(zip(product_names,product_prices,product_qty))
                     combined.sort()
                     product_prices=[item [0] for item in combined]
                     product_names=[item [1] for item in combined]
                     product_qty=[item [2] for item in combined]
                     print("Product sorted by price(ascending).\n")
       elif choice== '7':
                     if len (product_names)==0:
                            print("No products to sort.\n")
                     else:
                            combined=list(zip(product_names,product_prices,product_qty))
                            combined.sort()
                            product_prices=[item [0] for item in combined]
                            product_names=[item [1] for item in combined]
                            product_qty=[item [2] for item in combined]
                            print("Product sorted by price(descending).\n")
       elif choice== '8':
                     if len (product_names)==0:
                            print("No products to sort.\n")
                     else:
                            combined=list(zip(product_names,product_prices,product_qty))
                            combined.sort()
                            product_prices=[item [0] for item in combined]
                            product_names=[item [1] for item in combined]
                            product_qty=[item [2] for item in combined]
                            print("Product sorted alphabetically by name.\n")
       elif choice== '9':
                     if len (product_prices)==0:
                            print("No products available.\n")
                     else:
                            highest=max(product_prices)
                            lowest=min(product_prices)

                            costilest_index=product_prices.index(highest)
                                  
                            print("\n-----------price summary--------------")
                                                               
                            print(f"Costilest product:{product_names[costilest_index]} (price:{highest})")
                            print(f"Cheapest product:{product_names[cheapest_index]} (price:{lowest})")
                            print()               
                            cheapest_index=product_prices.index(lowest)
       elif choice =='10':
                     print("Exiting program.Thank you!")
                     break
       else:
              print("Invalid choice.Please enter a number between 1 and 10.\n")
                        
       
       
       
       











                     



        








       
       
       
       
       
          


 


                       
       



                    


                                        
       
       
       


                 
                                                                            
                       
                                                                            
                                                                            
                                                                      
             
             

                                                        
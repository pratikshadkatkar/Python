Student_names=[]
Student_marks=[]
while True:
       print("="*40)
       print("STUDENT MARKS MANAGEMENT SYSTEM")
       print("="*40)
       print("1. Insert Student Record")
       print("2. Delete Student Record")
       print("3. Update Student Marks")
       print("4. Traverse / Display All Records")
       print("5. Search Student")
       print("6. Show Statistics")
       print("7. Exit")
       print("="*40)
       choice=input("Enter your choice(1-7): ").strip()
       if choice=='1':
              name=input("Enter Student name:").strip()  
              if name in Student_names:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                  print(f"Student '{name}' already exists!Use update option instead.\n")
              else:
                marks=float(input(f"Enter marks for {name}: "))
                Student_names.append(name)
                Student_marks.append(marks)
                print(f"Record for '{name}' inserted successfully.\n")
       elif choice== '2':
              name=input("Enter Student name to delete: ").strip()
              if name in Student_names:
                index=Student_names.index(name)
                Student_names.pop(index)
                Student_marks.pop(index)
                print(f"Record for'{name}'deleted successfully.\n")
              else:
                print(f"Student '{name}' not found.\n")
       elif choice=='3':
              name=input("Enter Student name to update: ").strip()
              if name in Student_names:
                            index=Student_names.index(name)
                            new_marks=float(input(f"enter new marks for {name}:"))
                            Student_marks[index] = new_marks
                            print(f"marks for'{name}'updated successfully.\n")
              else:
                            print(f"Student '{name}' not found.\n")
       elif choice== '4':
              if len (Student_names)==0:
                       print("No records to display.\n")
              else:
                       print("\n {:<5} {:<20} {:<10}".format("No.","Name","Marks"))
                       print("-"*35)
                       for i in range(len(Student_names)):
                        print(" {:<5} {:<20} {:<10}".format(i+1,Student_names[i],Student_marks[i]))
                        print()
       elif choice== '5':
              name=input("Enter Student name to search: ").strip()
              if name in Student_names:
                     index=Student_names.index(name)
                     print(f"{name} -> Marks:{Student_marks[index]}\n")
              else:
                     print(f"Student '{name}' not found.\n")
       elif choice== '6':
              if len (Student_names)==0:
                            print("No records available for statistics.\n")
              else:
                     total=sum(Student_marks)
                     average=total/len(Student_marks)
                     highest=max(Student_marks)
                     lowest=min(Student_marks)
                     topper_index=Student_marks.index(highest)
                     weakest_index=Student_marks.index(lowest)
       elif choice =='7':
              print("Exiting program.Thank you!")
              break
       else:
              print("Invalid choice.Please enter a number between 1 and 7.\n")

















        





                     


                       
                                        
       
       
       


                 
                                                                            
                       
                                                                            
                                                                            
                                                                      
             
             

                                                              
                     
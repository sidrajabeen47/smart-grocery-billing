                                                 # Smart grocery billing


"""products = {
    "apple": 50,
    "milk": 30,
    "bread": 40,
    "eggs": 60,
    "rice": 70
}
# step 1 :cleaning using split,strip,lower

user_input=" apple, MILK , bread, chocolate, eggs "
raw_list= user_input.split(',')
clean_item=[item.strip().lower() for item in raw_list]
print(clean_item)

# step 2: using in and append

cart=[]
invalid_list=[]
for item in clean_item :
    if item in products.keys():
        cart.append(item)
    else:
        invalid_list.append(item)
print(cart)
print(invalid_list)

# step 3: using get ,sum

total_sum=[]
for item in cart:
    price=products.get(item)
    total_sum.append(price)
total_bill=sum(total_sum)
print(total_bill)

print("------ INVOICE ------")
for item in cart:
    price = products.get(item)
    print(f"{item.title():<8} : ₹{price}")
print(f"{'Total':<8} : ₹{total_bill}")
print("Unavailable Items:" )
# join() takes the list and turns it into a string separated by a comma
print(", ".join(invalid_list).title())

# Use set(cart) to ensure "Apple" only prints once
for item in set(cart):
    # Use count()
    quantity = cart.count(item)
    price = products.get(item)
    subtotal = price * quantity
    
    # Updated print statement for the bonus requirement
    print(f"{item.title():<8} x{quantity} = ₹{subtotal}")

print("-" * 20)
print(f"{'Total':<11} = ₹{total_bill}")
print("-" * 20)

print("Unavailable Items:")
print(", ".join(invalid_list).title())"""
                                                    # Employee attendace

records = [
    " Ellie - Present ",
    "john-Present",
    "MAYA - Absent",
    "ellie-present",
    "John-Late",
    "Maya-Present"
]

normalized_data = []
attendance_dict = {}

for record in records:
    parts = record.split('-')
    name = parts[0].strip().title()
    status = parts[1].strip().capitalize()
    
    # 1. Add to the list
    clean_record = f"{name}: {status}"
    normalized_data.append(clean_record)
    
    # 2. Add to the dictionary 
    current_history = attendance_dict.get(name, [])
    current_history.append(status)
    attendance_dict[name] = current_history

# Now print everything AFTER the loop is totally done
print("--- Normalized Records ---")
for entry in normalized_data:
    print(entry)

print("\n--- Attendance Dictionary ---")
print(attendance_dict)

# Assuming attendance_dict is already created from Step 2
print("--- Final Attendance Report ---")

# .items() gives us both the name (key) and the list of statuses (value)
for name, statuses in attendance_dict.items():
   
    print(f"\n{name}")
    
    # Use .count() 
    present_count = statuses.count("Present")
    absent_count  = statuses.count("Absent")
    late_count    = statuses.count("Late")
    
    # Print the formatted counts
    print(f" Present Days: {present_count}")
    print(f" Absent Days : {absent_count}")
    print(f" Late Days   : {late_count}")
    
# STEP 4: Find Best Employee
best_employee = max(attendance_dict, key=lambda name: attendance_dict[name].count("Present"))

print(f"\nBest Attendance: {best_employee}")

# --- Search Feature ---
print("\n--- Employee Search ---")
search_name = input("Enter name to search: ").strip().title()

# .get() looks for the name. If not found, it returns None
result = attendance_dict.get(search_name)

if result:
    print(f"\nReport for {search_name}:")
    print(f"Status History: {result}")
    print(f"Total Present: {result.count('Present')}")
else:
    print(f"Record for '{search_name}' not found.")
# --- Sorted Report ---
print("\n------ SORTED ATTENDANCE REPORT ------")

# sorted() 
for name in sorted(attendance_dict.keys()):
    statuses = attendance_dict[name]
    print(f"\n{name}")
    print(f"Present: {statuses.count('Present')}")
    print(f"Absent : {statuses.count('Absent')}")
    print(f"Late   : {statuses.count('Late')}")
                    

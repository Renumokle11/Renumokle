import csv
import re
class UserDetails:
    def __init__(self, filename='user_data.csv'):
        self.filename = filename
        self.users = self.Insert_data()


    def Insert_data(self):
        users = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    address_data = {
                        'House_no': row.get('address.House_no', row.get('House_no', '')),
                        'House_name': row.get('address.House_name', row.get('House_name', '')),
                        'Colony': row.get('address.Colony', row.get('Colony', '')),
                        'Landmark': row.get('address.Landmark', row.get('Landmark', '')),
                        'City': row.get('address.City', row.get('City', '')),
                        'Pincode': row.get('address.Pincode', row.get('Pincode', '')),
                        'State': row.get('address.State', row.get('State', ''))
                    }
                    user = {
                        'Name':row['Name'],
                        'Last_name': row['Last_name'],
                        'address': address_data,
                        'Pan_no': row['Pan_no'],
                        'Mobile_number': row['Mobile_number'],
                        'Aadhar_number': row['Aadhar_number']
                    }
                    users.append(user)
        except FileNotFoundError as e:
            print("The error is", e)
        return users
   
    
    def save_data(self, output_file1, output_file2):
        personal_details = ['Name', 'Last_name', 'Pan_no', 'Mobile_number', 'Aadhar_number']
        address_details = ['Name', 'Last_name', 'House_no', 'House_name', 'Colony',
                           'Landmark', 'City', 'State']
        self.existing_data1 = self.read_existing_data(output_file1)
        self.existing_data2 = self.read_existing_data(output_file2)
        if self.existing_data1 or self.existing_data2:
            confirm_overwrite = input(
                "Warning: Output files already contain this data. Do you want to overwrite? (yes/no): ").lower()
            if confirm_overwrite != 'yes':
                print("Data not saved. Exiting.")
                return
            
        with open(output_file1, 'w', newline='') as file1, open(output_file2, 'w', newline='') as file2:
            writer1 = csv.DictWriter(file1, fieldnames=personal_details)
            writer2 = csv.DictWriter(file2, fieldnames=address_details)

            if file1.tell() == 0 or confirm_overwrite == 'yes':
                writer1.writeheader()
            if file2.tell() == 0 or confirm_overwrite == 'yes':
                writer2.writeheader()

            for user in self.users:
                # Save personal details to file1
                writer1.writerow({
                    'Name': user['Name'],
                    'Last_name': user['Last_name'],
                    'Pan_no': user['Pan_no'],
                    'Mobile_number': user['Mobile_number'],
                    'Aadhar_number': user['Aadhar_number']
                })
                # Save address details to file2
                writer2.writerow({
                    'Name': user['Name'],
                    'Last_name': user['Last_name'],
                    'House_no': user['address']['House_no'],
                    'House_name': user['address']['House_name'],
                    'Colony': user['address']['Colony'],
                    'Landmark': user['address']['Landmark'],
                    'City': user['address']['City'],
                    'State': user['address']['State']
                })
            print("Data saved successfully.")

    def read_existing_data(self, filename):
        try:
            with open(filename, 'r') as file:
                return file.read().strip()  # Assuming the file contains plain text data
        except FileNotFoundError:
            return None
        
    def get_existing_user(self,Pan_no,Aadhar_number):
        for user in self.users:
            if user['Pan_no'] == Pan_no or user['Aadhar_number'] == Aadhar_number:
                return user
        return False
        
    def display_user_details(self, user):
        print("\nUser Details:")
        print(f"Name: {user['Name']} {user['Last_name']}")
        print(f"Pan_no: {user['Pan_no']}")
        print(f"Mobile number: {user['Mobile_number']}")
        print(f"Aadhar_number: {user['Aadhar_number']}")
        print(f"Address: {user['address']['House_no']} {user['address']['House_name']}, "
          f"{user['address']['Colony']}, "
          f"{user['address']['Landmark']}, "
          f"{user['address']['City']}, {user['address']['State']}")
    

    def Update_existing_user(self, existing_user):
        print("\nUpdating existing user:")
        print("Existing User Details:")
        self.display_user_details(existing_user)

 
        action = input("Do you want to Update (U) or Fetch (F) Existing data? (Enter 'U' or 'F'): ")
        print(f"Entered the action is '{action}'")
        if action == 'U':
           existing_user['Aadhar_number'] = input("Enter updated Aadhar_number: ")
           existing_user['Pan_no'] = input("Enter updated Pan_no: ")
           existing_user['Mobile_number'] = input("Enter updated Mobile number: ")
           print("User data updated successfully.")
        elif action == 'F':
            print("Fetching existing user data.")
            self.display_user_details(existing_user)
        else:
            print("Invalid action. Skipping update.")



    def get_valid_input(self, prompt, validator, skip_option=False):
        while True:
            user_input = input(prompt)
            if skip_option and (user_input.lower() == 's' or not user_input.strip()):
                return None
            elif validator(user_input):
                return user_input
            else:
                print("Invalid input. Please try again.")
    def validate_alpha(self, value):
        return value.isalpha()
    def validate_digit(self, value):
        return value.isdigit()
    def validate_pan_no(self, value):
        return re.match("[A-Z]{5}[0-9]{4}[A-Z]{1}", value) is not None
    def validate_aadhar_number(self, value):
        return re.match(r"^\d{12}$", value) is not None
    def validate_mobile_number(self, value):
        return value.isdigit() and len(value) == 10
    def validate_Fetch_choice(self, value):
        return value in ['1', '2', '3', '4', '5', '6', '7']
    def get_basis_from_choice(self, choice):
        basis_mapping = {
            '1': 'Name',
            '2': 'Last_name',
            '3': 'Aadhar_number',
            '4': 'Mobile_number',
            '5': 'House_no',
            '6': 'House_name'
        }
        return basis_mapping.get(choice, 'Name')
    
    def Insert_user(self):
        # Mandatory fields
        Name = self.get_valid_input("Enter Your Name: ", self.validate_alpha)
        Last_name = self.get_valid_input("Enter Your Last name: ", self.validate_alpha)
        Pan_no = self.get_valid_input("Enter your 10 digit(CAPATIAL) PAN Number: ", self.validate_pan_no)
        Aadhar_number = self.get_valid_input("Enter your 12 digit Aadhar_number: ", self.validate_aadhar_number)
        
        existing_user = self.get_existing_user(Pan_no, Aadhar_number)
        if existing_user:
               print("Duplicate entry found.")
               print("Existing User Details:")
               self.display_user_details(existing_user)
               
               while True:
                action = input("Do you want to Update (U) or Fetch (F) existing data? (Enter 'U', 'F', or 'any other key to skip): ")
                print(f"Entered  the action is '{action}'")
                if action == 'U':
                    if existing_user:
                        self.Update_existing_user(existing_user)
                        print("User data updated successfully.")
                        break
                    else:
                        print("Existing User not found")
                elif action == 'F':
                    if existing_user:
                        print("Fetching existing user data.")
                        self.display_user_details(existing_user)
                    else:
                        print("Existing User not found")

                else:
                    print("Skipping duplicate entry.")
                    return

        # Optional fields without skip option
        House_no = self.get_valid_input("Enter your House_Number: ", self.validate_digit)
        House_name = self.get_valid_input("Enter Your House name: ", self.validate_alpha)
        Colony = self.get_valid_input("Enter Your colony: ", self.validate_alpha)
        Landmark = self.get_valid_input("Enter Landmark: ", self.validate_alpha)
        City = self.get_valid_input("Enter City: ", self.validate_alpha)
        State = self.get_valid_input("Enter State: ", self.validate_alpha)
        Mobile_number = self.get_valid_input("Enter 10-digit Mobile_number: ", self.validate_mobile_number)
    
        new_user = {
            'Name': Name,
            'Last_name': Last_name,
            'address': {
                'House_no': int(House_no) if House_no else None,
                'House_name': House_name,
                'Colony': Colony,
                'Landmark': Landmark,
                'City': City,
                'State': State
            },
            'Pan_no': Pan_no,
            'Mobile_number': Mobile_number,
            'Aadhar_number': Aadhar_number
           }
        self.users.append(new_user)
        self.save_data("output_file1.csv", "output_file2.csv")
        print("User data added successfully.")
        
    def Fetch_user_data(self):
        print("Choose the basis for Fetching data:")
        print("1. Name")
        print("2. Last name")
        print("3. Aadhar number")
        print("4. Mobile number")
        print("5. House_number")
        print("6. House_name")
        print("7. All")
        choice = self.get_valid_input("Enter your choice (1-7): ", self.validate_Fetch_choice)
        if choice == '7':
            basis = 'all'
            value = ''
        else:
            basis = self.get_basis_from_choice(choice)
            value = input(f"Enter the value to search for based on {basis} (leave empty for 'all'): ")
        matching_users = []
          
        for user in self.users:   
            if basis == 'all':
                matching_users.append(user)

            else:
                for user in self.users:
                    if choice=='5' or choice=='6':
                        user_value=str(user.get("address",{}).get(basis,{}))
                        if not value or user_value.strip()== value.strip():
                            matching_users.append(user)
                    else:
                        user_value = str(user.get(basis, ''))
                        if not value or user_value.strip() == value.strip():
                            matching_users.append(user)   


        if matching_users:
            for user in matching_users:
                print("\nUser Details:")
                print(f"Name: {user['Name']} {user['Last_name']}")
                print(f"Pan_no: {user['Pan_no']}")
                print(f"Mobile number: {user['Mobile_number']}")
                print(f"Aadhar_number: {user['Aadhar_number']}")
                print(f"Address: {user['address']['House_no']} {user['address']['House_name']}, "
                      f"{user['address']['Colony']}, "
                      f"{user['address']['Landmark']}, "
                      f"{user['address']['City']}, {user['address']['State']}")
                print("-" * 30)
        else:
            print("No matching users found.")

    def run_program(self):
        while True:
            print("\n1. Insert User Data")
            print("2. Fetch User Data")
            print("3. Exit")
            
            self.existing_data1 = self.read_existing_data("output_file1.csv")
            self.existing_data2 = self.read_existing_data("output_file2.csv")
            choice = self.get_valid_input("Enter your choice (1/2/3): ", self.validate_choice)
            if choice == '1':
                self.Insert_user()
            elif choice == '2':
                self.Fetch_user_data()
            elif choice == '3':
                self.save_data("output_file1.csv", "output_file2.csv")
                print("Exiting program. Data saved to output_file1.csv and output_file2.csv.")
                
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def validate_choice(self, value):
        return value in ['1', '2', '3']
if __name__ == "__main__":
    user_details = UserDetails()
    user_details.run_program()
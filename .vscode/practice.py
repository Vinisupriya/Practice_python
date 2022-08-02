""""
# using randint function

import random
a_number = 0
while a_number <= 20:
    a_number = random.randint(1, 25)
    print(f"This is the random number: {a_number}")
print("You have found one larger than 20")

import random
a = random.randint(1, 20)
b = random.randint(1, 20)
if a > 10:
    print("a is a big number, it seems")
if b > 10:
    print("Whoa, both a and b are in double digits!") 

# Storing data in list using append 

list_of_names = ['Amelia', 'Olivia', 'Emily', 'Alexey', 'Poppy', 'Ava', 'Isabella', 'Jessica', 'Marcus', 'Lily', 'Sophie', 'Grace', 'Vsevolod', 'Sophia', 'Mia', 'Evie', 'Ruby', 'Celim', 'Sumir', 'Ella', 'Scarlett', 'Ruben', 'Isabelle', 'Chloe', 'Cherlin', 'Sienna', 'Masha', 'Freya', 'Phoebe', 'Charlotte', 'Daisy', 'Alice', 'Florence', 'Eva', 'Sofia', 'Millie', 'Lucy', 'Evelyn', 'Elsie', 'Rosie', 'Imogen', 'Lola', 'Matilda', 'Elizabeth', 'Layla', 'Alasdair','Holly', 'Lilly', 'Molly', 'Erin', 'Ellie', 'Maisie', 'Maya', 'Abigail', 'Eliza', 'Georgia', 'Jasmine', 'Esme', 'Willow', 'Leanne', 'Bella', 'Annabelle', 'Keemiya', 'Ivy', 'Amber', 'Emilia', 'Emma', 'Summer', 'Hannah', 'Eleanor', 'Harriet', 'Rose', 'Amelie', 'Lexi', 'Megan', 'Gracie', 'Zara', 'Nuha', 'John', 'Lacey', 'Martha', 'Anna', 'Violet', 'Darcey', 'Maria', 'Maryam', 'Brooke', 'Aisha', 'Katie', 'Leah', 'Heinrich', 'Nour', 'Thea', 'Darcie', 'Hollie', 'Amy', 'Alexandra', 'Stephen', 'Jonathan', 'Penny', 'Mollie', 'Heidi', 'Lottie', 'Bethany', 'Francesca', 'Faith', 'Harper', 'Nancy', 'Beatrice', 'Isabel', 'Juliette', 'Darcy', 'Lydia', 'Sarah', 'Sara', 'Julia', 'Victoria', 'Zoe', 'Robyn', 'Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'Annabel', 'George', 'Oscar', 'James', 'Ian', 'William', 'Noah', 'Alfie', 'Joshua', 'Yuvraj', 'Muhammad', 'Leo', 'Archie', 'Ethan', 'Joseph', 'Arushi', 'Freddie', 'Samuel', 'Alexander', 'Logan', 'Daniel', 'Isaac', 'Max', 'Mohammed', 'Benjamin', 'Hugo', 'Mason', 'Lucas', 'Edward', 'Harrison', 'Jake', 'Neil', 'Dylan', 'Asher', 'Riley', 'Akash', 'Finley', 'Catherine', 'Theo', 'Muktarsi', 'Sebastian', 'Adam', 'Zachary', 'Arthur', 'Thomas', 'Alberto', 'Toby', 'Jayden', 'Luke', 'Harley', 'Lewis', 'Tyler', 'Harvey', 'Anusha', 'Matthew', 'David', 'Reuben', 'Alok', 'Michael', 'Elijah', 'Kian', 'Tom', 'Mohammad', 'Blake', 'Jean', 'Luca', 'Theodore', 'Stanley', 'Derin', 'Jenson', 'Nathan', 'Nicholas', 'Charles', 'Frankie', 'Constantin', 'Jude', 'Teddy', 'Eric', 'Viren', 'Louie', 'Louis', 'Ryan', 'Hugo', 'Bobby', 'Niamh', 'Anya', 'Elliott', 'Dexter', 'Khai', 'Hariesh', 'Henry', 'Ollie', 'Aron', 'Alex', 'Liam', 'Kai', 'Gabriel', 'Connor', 'Aaron', 'Afrah', 'Frederick', 'Callum', 'Lorcan', 'Elliot', 'Albert', 'Leon', 'Ronnie', 'Rory', 'Jamie', 'Austin', 'Seth', 'Ibrahim', 'Mei', 'Owen', 'Caleb', 'Yousuf', 'Ellis', 'Sonny', 'Devyn', 'Robert', 'Joey', 'Felix', 'Finlay', 'Rossa', 'Ekraj', 'Jackson', 'Jimi', 'Meera', 'Rafi', 'Salahdeen', 'Guido', 'Tanya', 'Karlis']
result = []  #creating an Empty list
for name in list_of_names:
#name = list_of_names[0]
    if name[0] == "P":
        result.append(name)
print(result)

#Without using it

list_of_names = ['Amelia', 'Olivia', 'Emily', 'Alexey', 'Poppy', 'Ava', 'Isabella', 'Jessica', 'Marcus', 'Lily', 'Sophie', 'Grace', 'Vsevolod', 'Sophia', 'Mia', 'Evie', 'Ruby', 'Celim', 'Sumir', 'Ella', 'Scarlett', 'Ruben', 'Isabelle', 'Chloe', 'Cherlin', 'Sienna', 'Masha', 'Freya', 'Phoebe', 'Charlotte', 'Daisy', 'Alice', 'Florence', 'Eva', 'Sofia', 'Millie', 'Lucy', 'Evelyn', 'Elsie', 'Rosie', 'Imogen', 'Lola', 'Matilda', 'Elizabeth', 'Layla', 'Alasdair','Holly', 'Lilly', 'Molly', 'Erin', 'Ellie', 'Maisie', 'Maya', 'Abigail', 'Eliza', 'Georgia', 'Jasmine', 'Esme', 'Willow', 'Leanne', 'Bella', 'Annabelle', 'Keemiya', 'Ivy', 'Amber', 'Emilia', 'Emma', 'Summer', 'Hannah', 'Eleanor', 'Harriet', 'Rose', 'Amelie', 'Lexi', 'Megan', 'Gracie', 'Zara', 'Nuha', 'John', 'Lacey', 'Martha', 'Anna', 'Violet', 'Darcey', 'Maria', 'Maryam', 'Brooke', 'Aisha', 'Katie', 'Leah', 'Heinrich', 'Nour', 'Thea', 'Darcie', 'Hollie', 'Amy', 'Alexandra', 'Stephen', 'Jonathan', 'Penny', 'Mollie', 'Heidi', 'Lottie', 'Bethany', 'Francesca', 'Faith', 'Harper', 'Nancy', 'Beatrice', 'Isabel', 'Juliette', 'Darcy', 'Lydia', 'Sarah', 'Sara', 'Julia', 'Victoria', 'Zoe', 'Robyn', 'Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'Annabel', 'George', 'Oscar', 'James', 'Ian', 'William', 'Noah', 'Alfie', 'Joshua', 'Yuvraj', 'Muhammad', 'Leo', 'Archie', 'Ethan', 'Joseph', 'Arushi', 'Freddie', 'Samuel', 'Alexander', 'Logan', 'Daniel', 'Isaac', 'Max', 'Mohammed', 'Benjamin', 'Hugo', 'Mason', 'Lucas', 'Edward', 'Harrison', 'Jake', 'Neil', 'Dylan', 'Asher', 'Riley', 'Akash', 'Finley', 'Catherine', 'Theo', 'Muktarsi', 'Sebastian', 'Adam', 'Zachary', 'Arthur', 'Thomas', 'Alberto', 'Toby', 'Jayden', 'Luke', 'Harley', 'Lewis', 'Tyler', 'Harvey', 'Anusha', 'Matthew', 'David', 'Reuben', 'Alok', 'Michael', 'Elijah', 'Kian', 'Tom', 'Mohammad', 'Blake', 'Jean', 'Luca', 'Theodore', 'Stanley', 'Derin', 'Jenson', 'Nathan', 'Nicholas', 'Charles', 'Frankie', 'Constantin', 'Jude', 'Teddy', 'Eric', 'Viren', 'Louie', 'Louis', 'Ryan', 'Hugo', 'Bobby', 'Niamh', 'Anya', 'Elliott', 'Dexter', 'Khai', 'Hariesh', 'Henry', 'Ollie', 'Aron', 'Alex', 'Liam', 'Kai', 'Gabriel', 'Connor', 'Aaron', 'Afrah', 'Frederick', 'Callum', 'Lorcan', 'Elliot', 'Albert', 'Leon', 'Ronnie', 'Rory', 'Jamie', 'Austin', 'Seth', 'Ibrahim', 'Mei', 'Owen', 'Caleb', 'Yousuf', 'Ellis', 'Sonny', 'Devyn', 'Robert', 'Joey', 'Felix', 'Finlay', 'Rossa', 'Ekraj', 'Jackson', 'Jimi', 'Meera', 'Rafi', 'Salahdeen', 'Guido', 'Tanya', 'Karlis']
for name in list_of_names:
#name = list_of_names[0]
    if name[0] == "P":
        print ( name )
        

# define function and return the data to main function
list_of_names = ['Amelia', 'Olivia', 'Emily', 'Alexey', 'Poppy', 'Ava', 'Isabella', 'Jessica', 'Marcus', 'Lily', 'Sophie', 'Grace', 'Vsevolod', 'Sophia', 'Mia', 'Evie', 'Ruby', 'Celim', 'Sumir', 'Ella', 'Scarlett', 'Ruben', 'Isabelle', 'Chloe', 'Cherlin', 'Sienna', 'Masha', 'Freya', 'Phoebe', 'Charlotte', 'Daisy', 'Alice', 'Florence', 'Eva', 'Sofia', 'Millie', 'Lucy', 'Evelyn', 'Elsie', 'Rosie', 'Imogen', 'Lola', 'Matilda', 'Elizabeth', 'Layla', 'Alasdair','Holly', 'Lilly', 'Molly', 'Erin', 'Ellie', 'Maisie', 'Maya', 'Abigail', 'Eliza', 'Georgia', 'Jasmine', 'Esme', 'Willow', 'Leanne', 'Bella', 'Annabelle', 'Keemiya', 'Ivy', 'Amber', 'Emilia', 'Emma', 'Summer', 'Hannah', 'Eleanor', 'Harriet', 'Rose', 'Amelie', 'Lexi', 'Megan', 'Gracie', 'Zara', 'Nuha', 'John', 'Lacey', 'Martha', 'Anna', 'Violet', 'Darcey', 'Maria', 'Maryam', 'Brooke', 'Aisha', 'Katie', 'Leah', 'Heinrich', 'Nour', 'Thea', 'Darcie', 'Hollie', 'Amy', 'Alexandra', 'Stephen', 'Jonathan', 'Penny', 'Mollie', 'Heidi', 'Lottie', 'Bethany', 'Francesca', 'Faith', 'Harper', 'Nancy', 'Beatrice', 'Isabel', 'Juliette', 'Darcy', 'Lydia', 'Sarah', 'Sara', 'Julia', 'Victoria', 'Zoe', 'Robyn', 'Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'Annabel', 'George', 'Oscar', 'James', 'Ian', 'William', 'Noah', 'Alfie', 'Joshua', 'Yuvraj', 'Muhammad', 'Leo', 'Archie', 'Ethan', 'Joseph', 'Arushi', 'Freddie', 'Samuel', 'Alexander', 'Logan', 'Daniel', 'Isaac', 'Max', 'Mohammed', 'Benjamin', 'Hugo', 'Mason', 'Lucas', 'Edward', 'Harrison', 'Jake', 'Neil', 'Dylan', 'Asher', 'Riley', 'Akash', 'Finley', 'Catherine', 'Theo', 'Muktarsi', 'Sebastian', 'Adam', 'Zachary', 'Arthur', 'Thomas', 'Alberto', 'Toby', 'Jayden', 'Luke', 'Harley', 'Lewis', 'Tyler', 'Harvey', 'Anusha', 'Matthew', 'David', 'Reuben', 'Alok', 'Michael', 'Elijah', 'Kian', 'Tom', 'Mohammad', 'Blake', 'Jean', 'Luca', 'Theodore', 'Stanley', 'Derin', 'Jenson', 'Nathan', 'Nicholas', 'Charles', 'Frankie', 'Constantin', 'Jude', 'Teddy', 'Eric', 'Viren', 'Louie', 'Louis', 'Ryan', 'Hugo', 'Bobby', 'Niamh', 'Anya', 'Elliott', 'Dexter', 'Khai', 'Hariesh', 'Henry', 'Ollie', 'Aron', 'Alex', 'Liam', 'Kai', 'Gabriel', 'Connor', 'Aaron', 'Afrah', 'Frederick', 'Callum', 'Lorcan', 'Elliot', 'Albert', 'Leon', 'Ronnie', 'Rory', 'Jamie', 'Austin', 'Seth', 'Ibrahim', 'Mei', 'Owen', 'Caleb', 'Yousuf', 'Ellis', 'Sonny', 'Devyn', 'Robert', 'Joey', 'Felix', 'Finlay', 'Rossa', 'Ekraj', 'Jackson', 'Jimi', 'Meera', 'Rafi', 'Salahdeen', 'Guido', 'Tanya', 'Karlis']
def find_names_starting_with():
    result = []
    for name in list_of_names:
        #name = list_of_names[0]
        if name[0] == "A":
            result.append(name)
            
    return result #Note indentation level for the return statement. It’s part of the def block but not part of the for or if blocks. Therefore it only needs one indent.

result = find_names_starting_with()
print(result)

"""











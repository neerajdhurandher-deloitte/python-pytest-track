from main_assignment.customExceptions.invalidCredential import InvalidCredential
from main_assignment.utils import movie, user
from main_assignment.pages import homePage
from main_assignment.utils.db import DB
from main_assignment.customExceptions.invalidInput import InputCheck
from main_assignment.utils.validations import emailvalidation, phonenumbervalidation, passwordvalidation

def welcome_page():
    print("Welcome")
    print("1. Login")
    print("2. Register new account")
    print("3. Exit")

    choice = InputCheck.int_input_check("Enter :- ")
    return choice


class UserPage(InvalidCredential, DB, InputCheck):

    def __init__(self):
        pass

    def user_page(self):
        choice = welcome_page()

        while choice != 3:
            if choice == 1:
                self.user_login()
                break
            elif choice == 2:
                self.register_user()

            else:
                print("Invalid choice , try again")
            choice = welcome_page()

        return

    def register_user(self):
        email = ""
        emailBool = False
        phone = ""
        phoneBool = False
        password = ""
        passwordBool = False

        print("****Create new Account***** ")
        while True:
            username = input("Enter your username :- ")

            if DB.user_dic.get(username) is None:
                break
            else:
                print("username already exits. Try another username.")

        name = input("Enter your name :- ")

        while not emailBool:
            email = input("Enter your email :- ")
            emailBool = emailvalidation(email)

        while not phoneBool:
            phone = input("Enter your phone number :- ")
            phoneBool = phonenumbervalidation(phone)

        age = InputCheck.int_input_check("Enter your age :- ")
        while not passwordBool:
            password = input("Enter your password :- ")
            passwordBool = passwordvalidation(password)

        new_user = user.User(username, name, email, phone, age, password)

        DB.user_dic[username] = new_user
        DB.user_list.append(DB.user_dic)
        print("User created")
        DB.print_users_details(self, new_user)

    def user_login(self):
        print("****** Welcome to Book MyShow ******* ")
        print("********** User Login **********")

        username = input("Enter username :- ")
        password = input("Enter password :- ")

        if DB.user_dic.get(username) is None:
            print("User not exits")
        else:
            user_temp = DB.user_dic.get(username)

            if user_temp.username == username and user_temp.password == password:
                print("***** welcome " + user_temp.name + " *****")
                self.after_login()

    def after_login(self):
        # show list of movies
        DB.show_movies_name(self)

        logoutcode = DB.movie_dict.__len__() + 1
        print(logoutcode, " Logout ")

        choice = InputCheck.int_input_check("Enter your choice :- ")

        if choice == logoutcode:
            self.user_page()
        else:
            self.sel_movie_actions(choice)

    def sel_movie_actions(self, choice):
        # shows movies details
        get_movie_index = choice - 1
        DB.show_movie_details(self, get_movie_index)
        self.action_on_movie(get_movie_index)

    def action_on_movie(self, get_movie_index):
        get_movie = DB.movie_list[get_movie_index]
        print("Selected movie :- ", get_movie.title)
        print("1. Book Tickets ")
        print("2. Cancel Tickets ")
        print("3. Give User Rating ")
        print("4. Back")

        choice = 0

        while choice != 4:
            choice = InputCheck.int_input_check("Enter your choice :- ")

            if choice == 1:
                self.book_ticket(get_movie_index)
            elif choice == 2:
                self.cancel_ticket(get_movie_index)
            elif choice == 3:
                self.user_rating(get_movie_index)
            elif choice == 4:
                self.after_login()

    def book_ticket(self, get_movie_index):
        get_movie = DB.movie_list[get_movie_index]
        print("*** Book tickets for ", get_movie.title, " movie")
        print("Timings")
        index = 1
        for time in get_movie.timings:
            print(str(index), " ", time)

        sel_timing = InputCheck.int_input_check("Select timing :- ")
        print("Timing ", get_movie.timings[sel_timing - 1])
        available_ticket = get_movie.available_seat
        print("Remaining seats :- ", available_ticket)
        ticket_count = InputCheck.int_input_check("Enter number of seats :- ")

        if ticket_count > available_ticket:
            print(ticket_count, " seats are not available.  try again")
            self.action_on_movie(get_movie_index)
        else:
            get_movie.available_seat = available_ticket - ticket_count
            print("Thanks for booking")
            self.after_login()

    def cancel_ticket(self, get_movie_index):
        get_movie = DB.movie_list[get_movie_index]
        print("*** Book tickets for ", get_movie.title, " movie")
        cancel_tickets = InputCheck.int_input_check("Number of seats you want to cancel :-  ")
        total_seats = get_movie.seat_capacity
        available_ticket = get_movie.available_seat

        if total_seats < cancel_tickets or total_seats - available_ticket < cancel_tickets:
            print("Invalid input !!  try again")
            self.action_on_movie(get_movie_index)
        else:
            get_movie.available_seat = available_ticket + cancel_tickets
            print("Ticket cancel successfully for ", get_movie.title)
            self.after_login()

    def user_rating(self, get_movie_index):
        get_movie = DB.movie_list[get_movie_index]
        print("*** Rate ", get_movie.title, " movie (max 10) :- ")
        rating = InputCheck.float_input_check("Enter your rating")
        if rating > 10:
            print("Invalid input !!  try again")
            self.user_rating(get_movie_index)
        else:
            get_movie.user_rating = rating
            print("Thankyou for rating ", get_movie.title)
            self.after_login()

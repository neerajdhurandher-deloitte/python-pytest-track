import random

from main_assignment.customExceptions.invalidCredential import InvalidCredential
from main_assignment.customExceptions.invalidInput import InputCheck
from main_assignment.utils import movie

from main_assignment.utils.db import DB

def str_val(val):
    if val < 10:
        return "0" + str(val)
    else:
        return str(val)


def time_formate(time):
    hours = int(time / 60)
    min = time - hours * 60
    if hours > 23:
        hours -= 24
    if min == 0:
        min = 00
    am_pm = " AM"
    if hours > 11:
        am_pm = " PM"
    if hours > 12:
        hours -= 12

    return "" + str_val(hours) + ":" + str_val(min) + am_pm


def get_show_timing(show_starting_time, total_length, gap_bt_show):
    show_start = time_formate(show_starting_time)
    show_end = time_formate(show_starting_time + total_length - gap_bt_show)

    return show_start + " to " + show_end


def cal_movie_show_timing(total_length, gap_bt_show, numShows, first_show):
    show_timing_list = []
    show_starting_time = first_show

    for show in range(numShows):
        show_time = get_show_timing(show_starting_time, total_length, gap_bt_show)
        show_timing_list.append(show_time)
        show_starting_time += total_length
    return show_timing_list


# 8  16*60 960


def show_count_validation(total_length, numShows, first_show):
    total_running_time = total_length * numShows
    available_time = 1440 - first_show * 60

    if total_running_time < available_time:
        return True
    elif total_running_time - available_time < total_length:
        return True
    else:
        # TODO remove this
        print("total_running_time ", total_running_time)
        print("available_time", available_time)
        return False


def show_timing_setup(length, interval_timing, gap_bt_show, numShows, first_show):
    total_length = length + interval_timing + gap_bt_show

    valid_show_setup = show_count_validation(total_length, numShows, first_show)

    while not valid_show_setup:
        print("Invalid shows setting !!")
        numShows = InputCheck.int_input_check("Enter movie's number of shows in a day :- ")
        valid_show_setup = show_count_validation(total_length, numShows, first_show)

    timings = cal_movie_show_timing(total_length, gap_bt_show, numShows, first_show * 60)

    return timings


def options_on_invalid_choice():
    print("1. Try again")
    print("2. Exit")
    op = InputCheck.int_input_check("choice :- ")
    return op

def check_data_for_input(param):

    if isinstance(param, int):
        new_input = InputCheck.int_input_check("Enter new " + param + " :- ")
    elif isinstance(param, float):
        new_input = InputCheck.float_input_check("Enter new " + param + " :- ")
    else:
        new_input = InputCheck.str_input_check("Enter new " + param + " :- ")

    return new_input


def get_id():
    valid = False
    generated_id = str(random.randint(1, 100000))

    while not valid:
        if generated_id in DB.movie_dict.keys():
            generated_id = random.randint(1, 100000)

        else:
            return generated_id




class Admin(InvalidCredential, DB, InputCheck):
    # TODO create valid admin credential
    admin_dict = {"username": "admin", "password": "admin"}

    print("****** Welcome to Admin Login Page *******")

    def delete_movie(self):
        print("Delete a movie")
        DB.show_movies_name(self)

        logoutcode = DB.movie_dict.__len__() + 1

        print(logoutcode, ". Back ")

        choice = InputCheck.int_input_check("Enter movie number for delete :- ")

        if choice == logoutcode:
            self.go_to_admin_options()

        else:
            selected_movie_index = choice - 1
            selected_movie = DB.movie_list[selected_movie_index]
            key = selected_movie.movie_id

            del DB.movie_dict[key]
            DB.movie_list.pop(selected_movie_index)

            print(selected_movie.title, " deleted")
            print("Available Movies ")
            DB.show_movies_name(self)

            self.go_to_admin_options()

    def logout(self):
        print("Logout")
        return

    def edit_movie(self):
        print("Edit movie's info")

        DB.show_movies_name(self)

        logoutcode = DB.movie_dict.__len__() + 1

        print(logoutcode, ". Back ")

        choice = InputCheck.int_input_check("Enter movie number for edit :- ")

        if choice == logoutcode:
            self.go_to_admin_options()

        else:
            selected_movie_index = choice - 1
            editing_movie = DB.movie_list[selected_movie_index]
            # DB.movie_dict.get(editing_movie.title)

            edit_choice = -1

            while edit_choice != 0:

                print("Which filed you want to edit")
                print("1. Title")
                print("2. genre")
                print("3. cast")
                print("4. director")
                print("5. admin rating")
                print("6. language")
                print("7. seat capacity")
                print("0. Exit")

                edit_choice = InputCheck.int_input_check("Enter choice :- ")

                if edit_choice == 0:
                    print(editing_movie.title + "'s  details edited successfully")
                    DB.movie_dict[editing_movie.movie_id] = editing_movie
                    print("Movie's edited details :- ")
                    DB.show_movie_details(self, selected_movie_index)
                    self.go_to_admin_options()

                elif edit_choice == 1:
                    param = editing_movie.title
                    new_val = check_data_for_input(param)
                    editing_movie.title = new_val

                elif edit_choice == 2:
                    param = editing_movie.genre
                    new_val = check_data_for_input(param)
                    editing_movie.genre = new_val

                elif edit_choice == 3:
                    param = editing_movie.cast
                    new_val = check_data_for_input(param)
                    editing_movie.cast = new_val

                elif edit_choice == 4:
                    param = editing_movie.director
                    new_val = check_data_for_input(param)
                    editing_movie.director = new_val

                elif edit_choice == 5:
                    param = editing_movie.admin_rating
                    new_val = check_data_for_input(param)
                    editing_movie.admin_rating = new_val

                elif edit_choice == 6:
                    param = editing_movie.language
                    new_val = check_data_for_input(param)
                    editing_movie.language = new_val

                elif edit_choice == 7:
                    param = editing_movie.seat_capacity
                    new_val = check_data_for_input(param)
                    editing_movie.seat_capacity = new_val

                else:
                    print("Invalid input !! try again")

    def add_new_movie(self):
        print("****** Add new movie info ******")
        title = input("Enter movie's title :- ")

        genre = input("Enter movie's Genre :- ")

        length = InputCheck.int_input_check("Enter movie's length (hours):- ")
        try:
            length *= 60
        except Exception as e:
            print(e)
            length = InputCheck.int_input_check("Enter movie's length (hours):- ")

        length += InputCheck.int_input_check("Enter movie's length (minutes):- ")

        cast = input("Enter movie's cast :- ")

        director = input("Enter movie's director :- ")

        admin_rating = InputCheck.float_input_check("Enter movie's admin rating (out of 10 ):- ")

        language = input("Enter movie's language :- ")

        numShows = InputCheck.int_input_check("Enter movie's number of shows in a day :- ")

        first_show = InputCheck.int_input_check("Enter timing of first shows of the day ( 24 hours formate ) :- ")

        interval_timing = InputCheck.int_input_check("Enter movie's interval timing  (int minutes) :- ")

        gap_bt_show = InputCheck.int_input_check("Enter the of gap timing between shows  (int minutes) :- ")

        seat_capacity = InputCheck.int_input_check("Enter seat capacity in theater :- ")

        timings = show_timing_setup(length, interval_timing, gap_bt_show, numShows, first_show)

        user_rating = 0.0
        available_seat = seat_capacity

        # random key generated for dict key
        generate_id = get_id()

        new_movie_obj = movie.Movie(generate_id, title, genre, length, cast, director, admin_rating, user_rating,
                                    language, timings,
                                    numShows,
                                    first_show, interval_timing, gap_bt_show, seat_capacity, available_seat)
        # add in dictionary
        DB.movie_dict[generate_id] = new_movie_obj

        # add in list
        DB.movie_list.append(new_movie_obj)

        # DB.show_movie_details(self, new_movie_obj)

        print(title, " Movie add successfully ")

        # print("Available timings are ", timings)

        self.go_to_admin_options()

    def go_to_admin_options(self):

        print("****** Welcome Admin *******")

        print("1. Add New Movie Info")
        print("2. Edit Movie Info ")
        print("3. Delete Movies ")
        print("4. Logout")
        sel_option = 0

        while sel_option != 4:
            sel_option = InputCheck.int_input_check("Enter your choice :- ")

            if sel_option == 1:
                self.add_new_movie()
            elif sel_option == 2:
                self.edit_movie()
            elif sel_option == 3:
                self.delete_movie()
            elif sel_option == 4:
                self.logout()

    def log_in_credential(self):

        print("****** Welcome Admin *******")

        username = input("Enter admin username :- ")
        password = input("Enter password :- ")

        try:
            get_username = self.admin_dict.get('username')
            get_password = self.admin_dict.get('password')

            # on successfully login
            if get_username.__eq__(username) and get_password.__eq__(password):
                self.go_to_admin_options()
            else:
                raise InvalidCredential

        except InvalidCredential as e:
            e.print_msg("Invalid admin credentials !!")

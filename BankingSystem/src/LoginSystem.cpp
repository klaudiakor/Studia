#include "LoginSystem.hpp"

#include <iostream>
#include <string>

#include "DataBase.hpp"
#include "Tools.hpp"
#include "User/Employee.hpp"

// REJESTRACJA
Client LogingSystem::registration_site() {
    std::string name;
    std::string surname;
    std::string login;
    std::string password;

    std::cout << "Name: ";
    std::cin >> name;
    std::cout << "Surname: ";
    std::cin >> surname;

    while (true) {
        std::cout << "Login: ";
        std::cin >> login;
        if (!LogingSystem::IsLoginExist(login)) {
            std::cout << "Password: ";
            std::cin >> password;
            auto& json = DataBase::GetInstance().getJson();
            long long int account_num;

            // generowanie nr konta
            do {
                // losuje liczbe 12-cyfrowa
                account_num = tools::RandomNumber();

            } while (json["Accounts"].contains(std::to_string(account_num)));
            // dopoki nie znajdzie unikalnego

            // zapis do bazy danych
            tools::WriteUserDataToJson(login, "name", name);
            tools::WriteUserDataToJson(login, "surname", surname);
            tools::WriteUserDataToJson(login, "password", password);
            tools::WriteUserDataToJson(login, "number", account_num);
            tools::WriteUserDataToJson(login, "client", true);
            tools::WriteBalanceToJson(account_num, 0);

            break;
        } else {
            std::cout << "This login exist! Please try again.\n";
        }
    }

    return Client(name, surname, login, password);
}

bool LogingSystem::IsLoginExist(const std::string& login) {
    auto& json = DataBase::GetInstance().getJson();

    if (json["Users"].contains(login)) {
        return true;
    }
    return false;
}

bool LogingSystem::IsCorrectPassword(
    const std::string& login, const std::string& password) {
    auto& json = DataBase::GetInstance().getJson();

    std::string pass = json["Users"][login]["password"];
    if (pass == password) {
        return true;
    } else {
        return false;
    }
}

// szablon
template <typename T>
std::unique_ptr<T> get_user_from_json_helper(
    const Json& json, const std::string& login) {
    return std::make_unique<T>(
        json["name"], json["surname"], login, json["password"]);
}

std::unique_ptr<User> LogingSystem::get_user_from_json(
    const std::string& login) {
    const auto& json = DataBase::GetInstance().getJson()["Users"][login];

    if (json["client"]) {
        return get_user_from_json_helper<Client>(json, login);
    } else {
        return get_user_from_json_helper<Employee>(json, login);
    }
}

//  LOGOWANIE
std::unique_ptr<User> LogingSystem::login_site() {
    std::string login, password;
    while (true) {
        std::cout << "Login: ";
        std::cin >> login;
        std::cout << "Password: ";
        std::cin >> password;
        if (LogingSystem::IsLoginExist(login)) {
            if (LogingSystem::IsCorrectPassword(login, password)) {
                std::cout << "Logged in.\n";

                return LogingSystem::get_user_from_json(login);
            }
        }
        std::cout << "Wrong login or password.\n";
    }
}

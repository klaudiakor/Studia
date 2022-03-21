#include "Employee.hpp"

#include <DataBase.hpp>
#include <Money.hpp>
#include <Tools.hpp>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>

using Json = nlohmann::json;

Employee::Employee(const std::string& name, const std::string& surname,
    const std::string& log, const std::string& pass)
    : User(name, surname, log), password(pass) {}

void Employee::show_menu() { UserMenu(this); }

void Employee::SearchRecord() {
    std::string login;
    std::cout << "Enter login: ";
    std::cin >> login;

    auto& json = DataBase::GetInstance().getJson();

    if (json["Users"].contains(login) && json["Users"][login]["client"]) {
        try {
            long long int num = tools::ReadAccountNumFromJson(login);
            std::cout << "Name: "
                      << tools::ReadUserDataFromJson(login, "name").value()
                      << '\n';
            std::cout << "Surname: "
                      << tools::ReadUserDataFromJson(login, "surname").value()
                      << '\n';
            std::cout << "Account number: " << num << '\n';
            Money balance = tools::ReadBalanceFromJson(num);
            std::cout << "Balance: " << balance << '\n';
        } catch (...) {
            std::cout << "[ERROR]: Read user data from json error\n";
        }
    } else {
        std::cout << "Client doesn't exist.\n";
    }
}
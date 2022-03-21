#include "Client.hpp"

#include <DataBase.hpp>
#include <Tools.hpp>
#include <iostream>
#include <nlohmann/json.hpp>

using Json = nlohmann::json;

Client::Client(const std::string& name, const std::string& surname,
    const std::string& log, const std::string& pass)
    : User(name, surname, log), password(pass) {
    auto& json = DataBase::GetInstance().getJson();
    data.account_num = tools::ReadAccountNumFromJson(data.login);
    balance = tools::ReadBalanceFromJson(data.account_num.value());
}

void Client::show_menu() { UserMenu(this); }

void Client::ShowAccount() {
    std::cout << "Account number: " << data.account_num.value() << '\n';
    std::cout << "Name: " << data.first_name << '\n';
    std::cout << "Last Name: " << data.last_name << '\n';
    std::cout << "Balance: " << balance << '\n';
}

void Client::Deposit() {
    Money temp_amount;
    std::cout << "Enter amount you want to deposit: ";
    std::cin >> temp_amount;
    balance += temp_amount;
    tools::WriteBalanceToJson(data.account_num.value(), balance);
}

void Client::Withdrawal() {
    balance = tools::ReadBalanceFromJson(data.account_num.value());
    std::cout << "Enter amount you want to withdraw: ";
    Money temp_amount;
    std::cin >> temp_amount;
    if (temp_amount <= balance) {
        balance -= temp_amount;
        tools::WriteBalanceToJson(data.account_num.value(), balance);
    } else {
        std::cout << "You don't have enough money\n";
    }
}

void Client::Transfer() {
    auto& json = DataBase::GetInstance().getJson();
    long long int receiver_number;
    do {
        std::cout << "Enter account number: ";
        std::cin >> receiver_number;
        if (!json["Accounts"].contains(std::to_string(receiver_number))) {
            std::cout << "Number doesn't exist. Try again.\n";
        }
    } while (!json["Accounts"].contains(std::to_string(receiver_number)));

    Money temp_amount;

    balance = tools::ReadBalanceFromJson(data.account_num.value());
    do {
        std::cout << "Enter the amount you want to transfer: ";
        std::cin >> temp_amount;
        if (balance < temp_amount) {
            std::cout << "You don't have enough money.\n";
        } else {
            std::cout << "Balance after transfer: ";
            std::cout << balance - temp_amount << '\n';
        }
    } while (balance < temp_amount);

    char option;
    std::cout << "Confirm [Y/N]\n";
    std::cin >> option;
    if (option == 'Y') {
        Money money_of_reciever = tools::ReadBalanceFromJson(receiver_number);
        money_of_reciever += temp_amount;
        tools::WriteBalanceToJson(receiver_number, money_of_reciever);

        Money money_of_sender =
            tools::ReadBalanceFromJson(data.account_num.value());
        money_of_sender -= temp_amount;
        tools::WriteBalanceToJson(data.account_num.value(), money_of_sender);
        balance = money_of_sender;

        std::cout << "The transfer was successful.\n";
    } else if (option == 'N') {
        std::cout << "Transfer canceled.\n";
    } else {
        std::cout << "Please enter Y if you confirm.\n";
    }
}
#include "UserMenu.hpp"

#include <iostream>

#include "User/Client.hpp"
#include "User/Employee.hpp"

void UserMenu(Client* client) {
    int option;

    do {  // while not logout
        std::cout << "\n\t█▀▄▀█ █▀▀ █▄░█ █░█\n";
        std::cout << "\t█░▀░█ ██▄ █░▀█ █▄█\n";
        std::cout << '\n';
        std::cout << "\t 1. Show Account \n";
        std::cout << "\t 2. Deposit      \n";
        std::cout << "\t 3. Withdrawal   \n";
        std::cout << "\t 4. Transfer     \n";
        std::cout << "\t 5. Logout       \n\n";
        std::cout << "Please enter number: ";

        std::cin >> option;
        switch (option) {
            case 1:
                client->ShowAccount();
                break;
            case 2:
                client->Deposit();
                break;
            case 3:
                client->Withdrawal();
                break;
            case 4:
                client->Transfer();
                break;
            case 5:
                break;
            default:
                std::cout << "Please enter a number from 1 to 5.\n";
                break;
        }
    } while (option != 5);
    std::cout << "Logged out.\n";
}
void UserMenu(Employee* employee) {
    int option;

    do {  // while not logout
        std::cout << "\n\t█▀▄▀█ █▀▀ █▄░█ █░█\n";
        std::cout << "\t█░▀░█ ██▄ █░▀█ █▄█\n";
        std::cout << '\n';
        std::cout << "\t 1. Search Record \n";
        std::cout << "\t 2. Logout \n";
        std::cout << "Please enter number: ";

        std::cin >> option;
        switch (option) {
            case 1:
                employee->SearchRecord();
                break;
            case 2:
                break;
            default:
                std::cout << "Please enter a number 1 or 2.\n";
                break;
        }

    } while (option != 2);
    std::cout << "Logged out.\n";
}

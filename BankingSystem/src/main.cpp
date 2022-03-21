#include <iostream>
#include <string>

#include "DataBase.hpp"
#include "LoginSystem.hpp"
#include "UserMenu.hpp"

int StartSite();

int main() {
    int option;
    do {
        option = StartSite();
        if (option == 1) {
            // login
            auto user = LogingSystem::login_site();
            user->show_menu();
        } else if (option == 2) {
            // register
            auto client = LogingSystem::registration_site();
            client.show_menu();
        } else if (option != 3) {
            std::cout << "Option doesn't exist.\n";
        }
    } while (option != 3);
}
int StartSite() {
    std::cout
        << "\n\t█▄▄ ▄▀█ █▄░█ █▄▀ █ █▄░█ █▀▀   █▀ █▄█ █▀ ▀█▀ █▀▀ █▀▄▀█\n"
        << "  \t█▄█ █▀█ █░▀█ █░█ █ █░▀█ █▄█   ▄█ ░█░ ▄█ ░█░ ██▄ █░▀░█\n\n";

    int option;
    std::cout << "1. Login\n"
              << "2. Register\n"
              << "3. Quit\n"
              << "Please enter number: ";
    std::cin >> option;
    return option;
}

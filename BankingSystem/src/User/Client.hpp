#pragma once

#include <Money.hpp>
#include <UserMenu.hpp>
#include <string>

#include "User.hpp"

class Client : public User {
   public:
    Client(const std::string& name, const std::string& surname,
        const std::string& log, const std::string& pass);

    void show_menu();
    void ShowAccount();
    void Deposit();
    void Withdrawal();
    void Transfer();

   private:
    std::string password;
    Money balance;  // saldo
};

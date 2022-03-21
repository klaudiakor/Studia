#pragma once
#include <UserMenu.hpp>
#include <string>

#include "User.hpp"

class Employee : public User {
   public:
    Employee(const std::string& name, const std::string& surname,
        const std::string& log, const std::string& pass);
    void SearchRecord();
    void show_menu();

   private:
    std::string password;
};
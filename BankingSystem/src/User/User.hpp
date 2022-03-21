#pragma once

#include <string>

#include "UserData.hpp"

class User {
   public:
    virtual void show_menu() = 0;

   protected:
    User(const std::string& name, const std::string& surname,
        const std::string& log);

    UserData data;
};

// polimorfizm
#pragma once

#include <memory>

#include "User/Client.hpp"

enum class UserType { Client, Employee };

class LogingSystem {
   public:
    static Client registration_site();
    static std::unique_ptr<User> login_site();

   private:
    static bool IsLoginExist(const std::string& login);
    static bool IsCorrectPassword(
        const std::string& login, const std::string& password);
    static std::unique_ptr<User> get_user_from_json(const std::string& login);
};
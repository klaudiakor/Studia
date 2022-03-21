#include "User.hpp"

User::User(
    const std::string& name, const std::string& surname, const std::string& log)
    : data{ .first_name{ name }, .last_name{ surname }, .login{ log } } {}
// lista inicjalizujaca konstruktora
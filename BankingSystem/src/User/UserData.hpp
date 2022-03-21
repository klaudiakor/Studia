#pragma once

#include <optional>
#include <string>

struct UserData {
    std::string first_name;
    std::string last_name;
    std::string login;
    std::optional<long> account_num{ std::nullopt };
};

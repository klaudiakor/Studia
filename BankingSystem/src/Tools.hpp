#pragma once
#include <iostream>
#include <optional>
#include <random>
#include <string>

#include "DataBase.hpp"

class Money;

namespace tools {

template <typename T>
void WriteUserDataToJson(
    const std::string& login, const std::string& item, const T& value_of_item) {
    auto& json = DataBase::GetInstance().getJson();
    if (item == "name" || item == "surname" || item == "password" ||
        item == "number" || item == "client") {
        json["Users"][login][item] = value_of_item;

        DataBase::GetInstance().save();
    } else {
        std::cout << "[ERROR]: Write user data to json error\n";
    }
}

void WriteBalanceToJson(long long int account_num, const Money& value);

std::optional<std::string> ReadUserDataFromJson(
    const std::string& login, const std::string& item);

long long int ReadAccountNumFromJson(const std::string& login);

Money ReadBalanceFromJson(long long int account_num);

long long int RandomNumber();

}  // namespace tools

// szablon
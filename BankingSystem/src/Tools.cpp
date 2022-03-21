#include "Tools.hpp"

#include "Money.hpp"

namespace tools {

void WriteBalanceToJson(long long int account_num, const Money& value) {
    auto& json = DataBase::GetInstance().getJson();
    json["Accounts"][std::to_string(account_num)]["balance"] =
        (static_cast<double>(value.get_amount()) / 100.0);
    DataBase::GetInstance().save();
}

std::optional<std::string> ReadUserDataFromJson(
    const std::string& login, const std::string& item) {
    if (item == "name" || item == "surname") {
        auto& json = DataBase::GetInstance().getJson();
        return json["Users"][login][item];
    }
    return std::nullopt;
}

Money ReadBalanceFromJson(long long int account_num) {
    auto& json = DataBase::GetInstance().getJson();

    long double balance_formatted =
        json["Accounts"][std::to_string(account_num)]["balance"];

    return Money(balance_formatted * 100);
}

long long int ReadAccountNumFromJson(const std::string& login) {
    auto& json = DataBase::GetInstance().getJson();
    long long int account_num =
        static_cast<long>(json["Users"][login]["number"]);
    return account_num;
}

long long int RandomNumber() {
    // losuje liczbe 12-cyfrowa
    std::random_device random_device;
    std::mt19937 random_engine(random_device());
    std::uniform_int_distribution<long long int> distribution_10_10(
        10e10, 10e11 - 1);
    return distribution_10_10(random_engine);
}

}  // namespace tools

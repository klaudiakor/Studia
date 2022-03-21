#pragma once

#include <exception>
#include <iostream>

struct NegativeMoneyException : public std::exception {
    const char* what() const noexcept { return "Money can't be negative!"; }
};

class Money {
    using MoneyType = long int;

   public:
    Money(MoneyType amt)
        : amount{ amt } {}  // lista inicjalizujaca konstruktora
    Money() = default;      // konstruktor domyslny

    friend std::ostream& operator<<(std::ostream& stream, const Money& money) {
        stream << (money.get_amount() / 100) << '.'
               << (money.get_amount() % 100);

        return stream;
    }

    friend std::istream& operator>>(std::istream& stream, Money& money) {
        long double input;

        try {
            stream >> input;
            if (input < 0.0) {
                throw NegativeMoneyException();
            }
        } catch (std::exception& e) {
            std::cout << "EXCEPTION: " << e.what() << '\n';
            input = 0;
        }

        money.amount = input * 100;

        return stream;
    }

    Money& operator+=(const Money& rhs) {
        amount += rhs.amount;
        return *this;
    }

    Money& operator-=(const Money& rhs) {
        amount -= rhs.amount;
        return *this;
    }

    // https://en.cppreference.com/w/cpp/language/operators
    friend Money operator+(Money lhs, const Money& rhs) {
        lhs += rhs;
        return lhs;
    }

    friend Money operator-(Money lhs, const Money& rhs) {
        lhs -= rhs;
        return lhs;
    }

    // (c++20) <, <=, >= , >, ==
    auto operator<=>(const Money& other) const {
        return amount <=> other.amount;
    };

    MoneyType get_amount() const { return amount; }
    void set_amount(MoneyType new_amount) { amount = new_amount; }

   private:
    MoneyType amount{ 0 };
};

// deklaracja przyjaciela
// wyjatek
// przeciazanie operatorow
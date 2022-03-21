#pragma once
#include <iostream>
#include <nlohmann/json.hpp>

using Json = nlohmann::json;

class DataBase {
   private:
    DataBase() { load(); }

   public:
    ~DataBase() { save(); }  // destruktor
    static DataBase& GetInstance();
    Json& getJson();
    void load();
    void save();

   private:
    Json json;
};

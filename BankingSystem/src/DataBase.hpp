#pragma once
#include <iostream>
#include <nlohmann/json.hpp>

using Json = nlohmann::json;

// singleton - 1 globalny obiekt
class DataBase {
   private:
    DataBase() { load(); }
    // prywatny konstruktor
    //-> jedyna mozliwosc utworzenia obiektu przez get instance

   public:
    ~DataBase() { save(); }  // destruktor
    static DataBase& GetInstance();
    Json& getJson();
    void load();
    void save();

   private:
    Json json;
};

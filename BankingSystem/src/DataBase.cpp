#include "DataBase.hpp"

#include <fstream>
#include <iostream>
#include <memory>

#include "config.hpp"

DataBase& DataBase::GetInstance() {
    static const std::unique_ptr<DataBase> db{ new DataBase{} };
    return *db;
}

Json& DataBase::getJson() { return json; }

void DataBase::load() {
    std::ifstream ifile(PATH);
    if (ifile.fail()) {
        std::cout << "file open error\n";
    }
    json = Json::parse(ifile);
}

void DataBase::save() {
    std::ofstream ofile(PATH);
    if (ofile.fail()) {
        std::cout << "file open error\n";
    }
    ofile << json;
}

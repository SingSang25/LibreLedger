// Currency.h
#ifndef CURRENCY_H
#define CURRENCY_H

#include <string>
#include <list>

class Currency
{
public:
    // Konstruktor
    Currency(std::string name, std::string symbol, std::string code, std::string country, int decimal);

    // Getter
    std::string getName() const;
    std::string getSymbol() const;
    std::string getCode() const;
    std::string getCountry() const;
    int getDecimal() const;

    // Setters
    void setName(const std::string &name);
    void setSymbol(const std::string &symbol);
    void setCode(const std::string &code);
    void setCountry(const std::string &country);
    void setDecimal(const int decimal);

private:
    std::string name;
    std::string symbol;
    std::string code;
    std::string country;
    int decimal;
};

#endif
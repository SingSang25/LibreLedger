#include <Currency.h>

Currency::Currency(std::string name, std::string symbol, std::string code, std::string country, int decimal)
    : name(name), symbol(symbol), code(code), country(country), decimal(decimal) {}

std::string Currency::getName() const { return name; }
void Currency::setName(const std::string &name) { this->name = name; }
std::string Currency::getSymbol() const { return symbol; }
void Currency::setSymbol(const std::string &symbol) { this->symbol = symbol; }
std::string Currency::getCode() const { return code; }
void Currency::setCode(const std::string &code) { this->code = code; }
std::string Currency::getCountry() const { return country; }
void Currency::setCountry(const std::string &country) { this->country = country; }
int Currency::getDecimal() const { return decimal; }
void Currency::setDecimal(const int decimal) { this->decimal = decimal; }
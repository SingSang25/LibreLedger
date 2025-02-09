#include "model/Account.h"
#include "model/Currency.h"

Account::Account(int id, const std::string &name, const std::string &type, double balance, const Currency &currency)
    : id(id), name(name), type(type), balance(balance), currency(currency) {}

int Account::getId() const { return id; }
void Account::setId(const int id) { this->id = id; }
std::string Account::getName() const { return name; }
void Account::setName(const std::string &name) { this->name = name; }
std::string Account::getType() const { return type; }
void Account::setType(const std::string &type) { this->type = type; }
double Account::getBalance() const { return balance; }
void Account::setBalance(const double balance) { this->balance = balance; }
Currency Account::getCurrency() const { return currency; }
void Account::setCurrency(const Currency &currency) { this->currency = currency; }
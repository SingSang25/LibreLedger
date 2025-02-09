// Account.h (Konto)
#ifndef ACCOUNT_H
#define ACCOUNT_H

#include <string>
#include "model/Currency.h"

class Account
{
public:
    // Konstruktor
    Account(int id, const std::string &name, const std::string &type, double balance, const Currency &currency);

    // Getter
    int getId() const;
    std::string getName() const;
    std::string getType() const;
    double getBalance() const;
    Currency getCurrency() const;

    // Setters
    void setId(const int id);
    void setName(const std::string &name);
    void setType(const std::string &type);
    void setBalance(const double balance);
    void setCurrency(const Currency &currency);

private:
    int id;
    std::string name;
    std::string type;
    double balance;
    Currency currency;
};

#endif // ACCOUNT_H
// Transaction.h
#ifndef TRANSACTION_H
#define TRANSACTION_H

#include <string>
#include <ctime>
#include <Currency.h>
#include <Account.h>

class Transaction
{
public:
    // Konstruktor
    Transaction(int id, const std::string &description, double amount, const Currency &currency, const Account &debitAccount, const Account &creditAccount, const std::string &date, const std::string &category, const User &createdBy);

    // Getter
    int getId() const;
    std::string getDescription() const;
    double getAmount() const;
    Currency getCurrency() const;
    Account getDebitAccount() const;
    Account getCreditAccount() const;
    std::string getDate() const;
    std::string getCategory() const;
    User getCreatedBy() const;

    // Setter
    void setId(const int id);
    void setDescription(const std::string &description);
    void setAmount(const double amount);
    void setCurrency(const Currency &currency);
    void setDebitAccount(const Account &debitAccount);
    void setCreditAccount(const Account &creditAccount);
    void setDate(const std::string &date);
    void setCategory(const std::string &category);
    void setCreatedBy(const User &createdBy);

private:
    int id;
    std::string description;
    double amount;
    Currency currency;
    Account debitAccount;  // Soll-Konto
    Account creditAccount; // Haben-Konto
    std::string date;
    std::string category;
    User createdBy;
};

#endif
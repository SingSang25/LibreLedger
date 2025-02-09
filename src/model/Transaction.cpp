#include "model/Transaction.h"
#include "model/Currency.h"
#include "model/Account.h"
#include "model/User.h"

Transaction::Transaction(int id, const std::string &description, double amount, const Currency &currency, const Account &debitAccount, const Account &creditAccount, const std::string &date, const std::string &category, const User &createdBy)
    : id(id), description(description), amount(amount), currency(currency), debitAccount(debitAccount), creditAccount(creditAccount), date(date), category(category), createdBy(createdBy) {}

int Transaction::getId() const { return id; }
void Transaction::setId(const int id) { this->id = id; }
std::string Transaction::getDescription() const { return description; }
void Transaction::setDescription(const std::string &description) { this->description = description; }
double Transaction::getAmount() const { return amount; }
void Transaction::setAmount(const double amount) { this->amount = amount; }
Currency Transaction::getCurrency() const { return currency; }
void Transaction::setCurrency(const Currency &currency) { this->currency = currency; }
Account Transaction::getDebitAccount() const { return debitAccount; }
void Transaction::setDebitAccount(const Account &debitAccount) { this->debitAccount = debitAccount; }
Account Transaction::getCreditAccount() const { return creditAccount; }
void Transaction::setCreditAccount(const Account &creditAccount) { this->creditAccount = creditAccount; }
std::string Transaction::getDate() const { return date; }
void Transaction::setDate(const std::string &date) { this->date = date; }
std::string Transaction::getCategory() const { return category; }
void Transaction::setCategory(const std::string &category) { this->category = category; }
User Transaction::getCreatedBy() const { return createdBy; }
void Transaction::setCreatedBy(const User &createdBy) { this->createdBy = createdBy; }
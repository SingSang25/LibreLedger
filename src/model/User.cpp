#include "model/User.h"
#include "model/Role.h"
#include "model/Groupe.h"
#include "model/Address.h"

User::User(std::string username, std::string password, std::string role)
    : username(username), password(password), role(role) {}

int User::getId() const { return id; }
void User::setId(const int id) { this->id = id; }
std::string User::getUsername() const { return username; }
void User::setUsername(const std::string &username) { this->username = username; }
std::string User::getTitel() const { return titel; }
void User::setTitel(const std::string &titel) { this->titel = titel; }
std::string User::getFirstname() const { return firstname; }
void User::setFirstname(const std::string &firstname) { this->firstname = firstname; }
std::string User::getLastname() const { return lastname; }
void User::setLastname(const std::string &lastname) { this->lastname = lastname; }
std::string User::getPassword() const { return password; }
void User::setPassword(const std::string &password) { this->password = password; }
std::string User::getMail() const { return mail; }
void User::setMail(const std::string &mail) { this->mail = mail; }
std::string User::getPhone() const { return phone; }
void User::setPhone(const std::string &phone) { this->phone = phone; }
Role User::getRole() const { return role; }
void User::setRole(const Role &role) { this->role = role; }
Groupe User::getGroupe() const { return groupe; }
void User::setGroupe(const Groupe &groupe) { this->groupe = groupe; }
Address User::getAddress() const { return address; }
void User::setAddress(const Address &address) { this->address = address; }
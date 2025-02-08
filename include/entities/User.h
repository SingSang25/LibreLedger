#ifndef USER_H
#define USER_H

#include <string>
#include <Role.h>
#include <Groupe.h>
#include <Address.h>

class User
{
public:
    // Konstruktor
    User(std::string username, std::string password, std::string role);

    // Getter
    int getId() const;
    std::string getUsername() const;
    std::string getTitel() const;
    std::string getFirstname() const;
    std::string getLastname() const;
    std::string getPassword() const;
    std::string getMail() const;
    std::string getPhone() const;
    Role getRole() const;
    Groupe getGroupe() const;
    Address getAddress() const;

    // Setters
    void setId(const int id);
    void setUsername(const std::string &username);
    void setTitel(const std::string &titel);
    void setFirstname(const std::string &firstname);
    void setLastname(const std::string &lastname);
    void setPassword(const std::string &password);
    void setMail(const std::string &mail);
    void setPhone(const std::string &phone);
    void setRole(const Role &role);
    void setGroupe(const Groupe &groupe);
    void setAddress(const Address &address);

private:
    int id;
    std::string username;
    std::string titel;
    std::string firstname;
    std::string lastname;
    std::string password;
    std::string mail;
    std::string phone;
    Role role;
    Groupe groupe;
    Address address;
};

#endif // USER_H
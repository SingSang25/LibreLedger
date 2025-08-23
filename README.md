# 📘 LibreLedger

**LibreLedger** ist eine modulare, skalierbare SaaS-Webplattform zur modernen Buchhaltung – entwickelt für Privatpersonen, Freelancer und KMU.  
Das System vereint **Finanzübersicht**, **Automatisierung**, **Sicherheit** und **Multiplattform-Zugriff** in einer durchdachten Fullstack-Architektur.

---

## 🚀 Ziel des Projekts

Entwicklung eines offenen, erweiterbaren Buchhaltungssystems mit:

- intelligenter Finanzanalyse
- Belegmanagement & OCR
- PDF-Import für Bankdokumente
- geplanter Open-Banking-Anbindung (PSD2/bLink)
- SaaS-fähiger Struktur mit Abomodellen und Mehrbenutzerzugang

---

## 🏗 Architekturüberblick

**Technologie-Stack:**

- **Backend:** FastAPI (Python), async SQLAlchemy, PostgreSQL
- **Frontend:** Vue 3 + Vite, Tailwind CSS
- **Mobile:** Flutter (in Planung)
- **DevOps:** GitHub Actions, Docker, CI/CD, Testabdeckung

**Architekturprinzipien:**

- Clean Architecture (modular, testbar, erweiterbar)
- Monorepo mit klarer Trennung von Applikationen

**Monorepo-Struktur:**
LibreLedger/
├── apps/
│ ├── backend/ # FastAPI-Backend mit OAuth2 & PostgreSQL
│ ├── frontend/ # Vue 3 Frontend (Vite + Tailwind)
│ └── mobile/ # Flutter-App (optional)
├── docker/ # Dockerfiles & Container-Setups
├── tools/ # CLI-Tools & Scripts
├── package.json # npm workspaces (Frontend/Tooling)
├── pyproject.toml # Poetry-Konfiguration (Backend)
└── README.md # Dieses Dokument

---

## 🔐 Authentifizierung & Sicherheit

**Mehrstufiges Login-System:**

1. E-Mail + Passwort (OAuth2 Password Flow)
2. TOTP-basierte Zwei-Faktor-Authentifizierung (verpflichtend)
3. _Optional:_ Push-Login via Mobile App
4. _Optional:_ WebAuthn (Passkey, Face ID, Fingerabdruck)

**Weitere Sicherheitsfeatures:**

- End-to-End-Verschlüsselung
- DSGVO-konformer Export & Account-Löschung
- 2FA, rollenbasierte Zugriffsverwaltung

---

## ✨ Kernfunktionen (geplant & umgesetzt)

### 1. Finanzübersicht & Budgetierung

- Dashboard mit Einnahmen, Ausgaben, Saldenverlauf
- Kategorisierung: manuell & automatisch
- Budgets & Warnungen bei Überschreitung
- Wiederkehrende Zahlungen erkennen

### 2. Analysen & Prognosen

- Jahresprognose & Liquiditätsentwicklung
- Steueranalyse (CH) inkl. Kantonsaufteilung
- Säule 3a Empfehlungen & Sparpotenziale

### 3. PDF-Import & OCR

- Kontoauszüge per PDF/Foto importieren
- OCR-Text-Extraktion
- Automatisches Transaktions-Matching

### 4. Planung & Simulation

- Liquiditätsvorschau (Kalenderansicht)
- Was-wäre-wenn-Rechnungen
- Vertragsverwaltung & Erinnerungen

### 5. Mehrbenutzer & Rollen

- Gemeinsame Konten (z. B. Familien)
- Benutzerrechte & Rollen (Admin, Nur-Lesen, Steuerberater)

### 6. Belegmanagement

- Upload per PDF oder Mobile App
- OCR, Matching mit Transaktionen
- Steuerrelevanz markieren

### 7. Export & API

- CSV, Excel, DATEV (geplant)
- SaaS-ready API-Struktur für spätere Integrationen (z. B. Bexio)

---

## 📦 SaaS & Erweiterungen

**Zukünftige Features:**

- Abo-Modelle: Free / Basic / Pro
- Feature-Gating je nach Tarif
- Open-Banking Anbindung (PSD2, bLink)
- Automatisierte Regeln & Workflows

**Regel-Engine (z. B.):**

> "Wenn Amazon-Ausgabe > 200 CHF → Warnung senden"

---

## 🧪 Testing & Qualität

- **Backend:** Pytest + Coverage
- **Frontend:** Vitest + ggf. Playwright
- **CI/CD:** GitHub Actions + Docker Build Pipelines

---

## 📄 Lizenz

**MIT License**  
Frei nutzbar, anpassbar und erweiterbar.

---

## 🛠 Beitrag & Entwicklung

Mitwirken ist willkommen!  
Konventionen:

- Clean Code & Tests
- Commit-Stil: Conventional Commits (`feat:`, `fix:`, `chore:` etc.)
- Docker-Setup & Devcontainer verfügbar

---

## 📞 Kontakt & Community

- 📧 Kontakt: _coming soon_
- 💬 Diskussion: _coming soon_
- 📝 Roadmap: [TO BE ADDED]

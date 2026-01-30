# Environment Book – E-Store

---

## E.1 – Glossary

### Actors

**E1.1 – Client**: A person who owns a customer account on the e-store and is able to browse products and make online purchases.  
**E1.2 – Administrator**: A person responsible for managing the e-store, including product catalog, stock levels, orders, and system configuration.

---

### Business Objects (Products and Documents)

**E1.3 – Product**: A generic item offered for sale on the e-store.  
**E1.4 – Sports equipment**: A specific type of product intended for practicing or assisting a sports activity.  
**E1.5 – Order**: A set of products selected by a client with the intention of purchasing.  
**E1.6 – Invoice**: An electronic document summarizing the details of a completed sale, including products, prices, date, and client information.

---

### Business Processes

**E1.7 – Sale**: A commercial process corresponding to the validation and successful payment of an order.  
**E1.8 – Payment**: A process allowing the client to pay for an order using secure payment methods.  
**E1.9 – Delivery**: A process by which ordered products are delivered to a location chosen by the client.  
**E1.10 – Order cancellation**: An action allowing the client to remove all or part of the products from an order before final validation.

---

### System Elements

**E1.11 – E-store**: A virtual store allowing the online sale of goods or services via the Internet.  
**E1.12 – Customer account**: A personal system space allowing a client to authenticate, place orders, and consult order and invoice history.  
**E1.13 – Login**: The action allowing a client to access their customer account using identifiers.  
**E1.14 – Authentication**: The system process of verifying the client’s identity during login.

---

## E.2 – Components

### Internal Components

**E2.1 – User Interface (UI)**: Graphical interface allowing the client to interact with the e-store (navigation, ordering, payment).  
**E2.2 – Application server**: Component hosting the backend code and handling user requests.  
**E2.3 – Database**: Centralized storage system for data related to clients, products, orders, and invoices.

---

### External Components

**E2.4 – External payment service**: Third-party system (bank or payment provider) responsible for validating and securing transactions.  
**E2.5 – Email service**: External system used to send confirmation, notification, and invoice emails.  
**E2.6 – SMS service**: External system used to send validation codes during payment.  
**E2.7 – Web browser**: Software used by the client to access the e-store.  
**E2.8 – Internet network**: Infrastructure enabling communication between users, external services, and the e-store system.

---

## E.3 – Constraints

### Functional Constraints

**E3.1** – An order payment can only be performed after a customer account has been created.  
**E3.2** – A customer account must be created using a valid email address, a password, and a phone number.  
**E3.3** – Out-of-stock products must be clearly indicated to the user.  
**E3.4** – Each invoice must be accessible in the customer’s personal space.

---

### Security Constraints

**E3.5** – Customer passwords must contain at least eight characters, one uppercase letter, one lowercase letter, one digit, and one special character.  
**E3.6** – Any payment validation must be confirmed using a confidential code sent to the customer’s phone number.

---

### Notification Constraints

**E3.7** – A confirmation message must be displayed on the user interface after account creation.  
**E3.8** – A confirmation email must be sent to the customer after account creation.  
**E3.9** – An error message must be displayed in case of account creation or payment failure.  
**E3.10** – Any site unavailability must be notified to customers by email.

---

### Technical Constraints

**E3.11** – The user interface must be developed using AngularJS.  
**E3.12** – The backend must be developed using Spring Boot.

---

## E.4 – Assumptions

**E4.1** – The Internet network is available and allows access to the e-store.  
**E4.2** – External services (payment, email, SMS) are operational when required.  
**E4.3** – Customers provide accurate and correctly formatted information.  
**E4.4** – Customers use a web browser compatible with the application.  
**E4.5** – Users comply with the usage rules of the e-store.

---

## E.5 – Effects on the Environment

**E5.1** – Creation, modification, and deletion of customer data in the database.  
**E5.2** – Stock updates following orders and order cancellations.  
**E5.3** – Generation and storage of electronic invoices.  
**E5.4** – Sending emails and notifications to customers.  
**E5.5** – Impact on sales and commercial management processes.

---

## E.6 – Invariants

**E6.1** – Each customer account is uniquely identified.  
**E6.2** – A validated order corresponds to a confirmed payment.  
**E6.3** – Product stock levels must never be negative.  
**E6.4** – An issued invoice cannot be modified.  
**E6.5** – Customer personal data must remain protected.  
**E6.6** – Deleting a customer account results in the deletion or anonymization of personal data, except for information retained for legal purposes (invoices and sales history).
**E6.1** – Each customer account is uniquely identified.

**E6.2** – A validated order corresponds to a confirmed payment.

**E6.3** – Product stock levels must never be negative.

**E6.4** – An issued invoice cannot be modified.

**E6.5** – Customer personal data must remain protected.

---

## E.7 – Customer account deletion

**E7.1** – Deleting a customer account results in the deletion or anonymization of personal data, except for information retained for legal purposes (invoices and sales history).

### G.1 Overall Context
The E-store project aims to design a robust software solution for online sports equipment sales. The goal is to capture a market of demanding athletes by offering a platform capable of supporting high traffic and heavy loads.

### G.2 Current Situation
Currently, customers must visit physical stores. There is a lack of centralized online platforms for specialized sports equipment with reliable real-time inventory tracking.

### G.3 Expected Benefits
* **Inventory Range:** Showcase over 500 technical product references.
* **Concurrency:** Support hundreds of simultaneous orders.
* **Automation:** Reduce human errors in order entry.
* **Speed:** Instant payment processing and notifications.

### G.4 Functionality Overview
The system shall ensure a seamless user experience through:
* Navigation by sports discipline (Bodybuilding, Fitness, Football, etc.).
* Advanced search (weight, brand, size).
* Cart management (Add/Edit/Remove) including guest mode.
* Secure checkout funnel (Registration/Login mandatory for payment).
* Profile management and order history tracking.



### G.5 High-level Usage Scenarios
* **G.5.1 Targeted Purchase:** A user searches for "10kg Dumbbells", filters by brand, and completes the purchase immediately.
* **G.5.2 Account Management:** A customer updates their shipping address following a relocation.
* **G.5.3 Product Consultation:** A user compares the technical specifications of two treadmills.
* **G.5.4 Admin Tracking:** The Director (PO) reviews weekly sales statistics.

### G.6 Limitations and Exclusions
* **G.6.1:** No second-hand or used product sales.
* **G.6.2:** Delivery is restricted to Mainland France and Belgium only.
* **G.6.3:** No integrated video coaching programs (V1).
* **G.6.4:** No payments via check or cryptocurrency.
* **G.6.5:** Product returns are not handled automatically via the UI (Manual Customer Support).

### G.7 Stakeholders and Requirements Sources
* **G.7.1 Customers:** Amateur and pro athletes (Usability requirements).
* **G.7.2 Product Owner:** Store Manager (Profitability requirements).
* **G.7.3 Luce (Fullstack):** Source of Java/Angular technical constraints.
* **G.7.4 Abdel (DevOps):** Source of deployment and CI/CD requirements.
* **G.7.5 Payment Provider:** Source of banking security constraints.
* **G.7.6 GDPR:** Source of legal constraints regarding data privacy.


### P.1 Roles and Personnel
* **Luce:** Angular (Frontend) and Java Spring Boot (Backend) development.
* **Abdel:** AWS Architecture, CI/CD Pipeline, and Validation Testing.
* **Product Owner:** Store Director (Deliverable validation).

### P.2 Imposed Technical Choices
* **Stacks:** Angular (Frontend), Java (Backend), PostgreSQL (Database).
* **Professional Tools:** Jira (Ticketing), GitHub (Code), AWS (Cloud).


### P.3 Schedule, Milestones, and Key Objectives
| Date (D+) | Mission | Phase | Key Objective |
| :--- | :--- | :--- | :--- |
| **D+7** | M1: Design | UI/UX Mockups | Validation of the graphic charter and checkout funnel. |
| **D+10** | M2: Catalog | Backend Development | SQL Database import and functional search API. |
| **D+14** | M3: Checkout | Payment & Security | Payment gateway integration and "Sandbox" testing. |
| **D+25** | M4: CI/CD | Cloud Deployment | Production Go-Live on AWS with GitHub Actions pipeline. |


### P.4 Tasks and Deliverables
* **Task:** Catalog Module (Filters/Search). -> **Deliverable:** Frontend source code.
* **Task:** Shipping calculation system. -> **Deliverable:** Tested Java API.
* **Task:** Doc generation pipeline. -> **Deliverable:** GitHub Actions workflow.

### P.5 Required Technology Elements
* Java 17, Maven, Angular CLI, AWS EC2 Instance.

### P.6 Risk and Mitigation Analysis
* **Risk:** Server downtime. -> **Mitigation:** AWS Load Balancing implementation.
* **Risk:** Data breach. -> **Mitigation:** SSL encryption and BCrypt hashing.

### P.7 Requirements Process and Report
* **P.7.1:** Project requirements are specified using the PEGS approach.
* **P.7.1:** Each created tag triggers a new project version in ZIP format and generates a PDF version of the requirements.
* **P.7.2:** The specification PDF is automatically generated.

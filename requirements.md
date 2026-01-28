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

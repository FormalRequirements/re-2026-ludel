# Environment Book – E‑Store

## E.1 – Glossary

**E1.1 – E‑store**: Virtual store allowing the online sale of goods or services via the Internet.

**E1.2 – Client**: A person who owns an account on the e‑store and is able to make online purchases.

**E1.3 – Product / Sports equipment**: Equipment intended for practicing or assisting a sports activity.

**E1.4 – Order**: A set of products selected by a client with the intention of purchasing.

**E1.5 – Sale**: Commercial act corresponding to the validation and payment of an order.

**E1.6 – Payment**: Process allowing the client to pay for an order using secure payment methods.

**E1.7 – Delivery**: Process by which ordered products are delivered to a location chosen by the client.

**E1.8 – Order cancellation**: Action allowing the client to remove all or part of the products from an order before final validation.

**E1.9 – Customer account**: Personal space allowing the client to authenticate, place orders and consult order history.

**E1.10 – Login**: Action allowing a client to access their account using identifiers.

**E1.11 – Authentication**: Process of verifying the client’s identity during login.

**E1.12 – Invoice**: Electronic document summarizing the details of a sale (products, prices, date, client).

---

## E.2 – Components

### Internal components

**E2.1 – User Interface (UI)**: Graphical interface allowing the client to interact with the e‑store (navigation, ordering, payment).

**E2.2 – Application server**: Component hosting the backend code and handling user requests.

**E2.3 – Database**: Centralized storage system for data related to clients, products, orders and invoices.

### External components

**E2.4 – External payment service**: Third‑party system (bank or payment provider) responsible for validating and securing transactions.

**E2.5 – Email service**: External system used to send confirmation, notification and invoice emails.

**E2.6 – SMS service**: External system used to send validation codes during payment.

**E2.7 – Web browser**: Software used by the client to access the e‑store.

**E2.8 – Internet network**: Infrastructure enabling communication between users, external services and the e‑store system.

---

## E.3 – Constraints

### Functional constraints

**E3.1** – An order payment can only be performed after a customer account has been created.

**E3.2** – A customer account must be created using a valid email address, a password and a phone number.

**E3.3** – Out‑of‑stock products must be clearly indicated to the user.

**E3.4** – Each invoice must be accessible in the customer’s personal space.

### Security constraints

**E3.5** – Customer passwords must contain at least:

- 8 characters
- one uppercase letter
- one lowercase letter
- one digit
- one special character

**E3.6** – Any payment validation must be confirmed using a confidential code sent to the customer’s phone number.

### Notification constraints

**E3.7** – A confirmation message must be displayed on the user interface after account creation.

**E3.8** – A confirmation email must be sent to the customer after account creation.

**E3.9** – An error message must be displayed in case of account creation or payment failure.

**E3.10** – Any site unavailability must be notified to customers by email.

### Technical constraints

**E3.11** – The user interface must be developed using AngularJS.

**E3.12** – The backend must be developed using Spring Boot.

---

## E.4 – Assumptions

**E4.1** – The Internet network is available and allows access to the e‑store.

**E4.2** – External services (payment, email, SMS) are operational when required.

**E4.3** – Customers provide accurate and correctly formatted information.

**E4.4** – Customers use a web browser compatible with the application.

**E4.5** – Users comply with the usage rules of the e‑store.

---

## E.5 – Effects on the environment

**E5.1** – Creation, modification and deletion of customer data in the database.

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

---

## E.7 – Customer account deletion

**E7.1** – Deleting a customer account results in the deletion or anonymization of personal data, except for information retained for legal purposes (invoices and sales history).

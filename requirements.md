# Environment Book – E-Store

---

## E.1 – Glossary

### E.1.1 Actors

- **E.1.1.1 – Client**: A person who owns a customer account on the e-store and is able to browse products and make online purchases.
- **E.1.1.2 – Administrator**: A person responsible for managing the e-store, including product catalog, stock levels, orders, and system configuration.

---

### E.1.2 Business Objects (Products and Documents)

- **E.1.2.1 – Product**: A generic item offered for sale on the e-store.
- **E.1.2.2 – Sports equipment**: A specific type of product intended for practicing or assisting a sports activity.
- **E.1.2.3 – Order**: A set of products selected by a client with the intention of purchasing.
- **E.1.2.4 – Invoice**: An electronic document summarizing the details of a completed sale.

---

### E.1.3 Business Processes

- **E.1.3.1 – Sale**: Commercial process corresponding to order validation and successful payment.
- **E.1.3.2 – Payment**: Process allowing the client to pay for an order using secure payment methods.
- **E.1.3.3 – Delivery**: Process by which ordered products are delivered to a location chosen by the client.
- **E.1.3.4 – Order cancellation**: Action allowing the client to remove all or part of the products from an order before final validation.

---

### E.1.4 System Elements

- **E.1.4.1 – E-store**: A virtual store allowing the online sale of goods or services via the Internet.
- **E.1.4.2 – Customer account**: A personal system space allowing a client to authenticate, place orders, and consult order and invoice history.
- **E.1.4.3 – Login**: The action allowing a client to access their customer account using identifiers.
- **E.1.4.4 – Authentication**: The system process of verifying the client’s identity during login.

---

## E.2 – Components

### E.2.1 Internal Components

- **E.2.1.1 – User Interface (UI)**: Graphical interface allowing the client to interact with the e-store.
- **E.2.1.2 – Application server**: Component hosting backend code and handling user requests.
- **E.2.1.3 – Database**: Centralized storage system for clients, products, orders, and invoices.

---

### E.2.2 External Components

- **E.2.2.1 – External payment service**: Third-party system responsible for validating and securing transactions.
- **E.2.2.2 – Email service**: External system used to send confirmation and notification emails.
- **E.2.2.3 – SMS service**: External system used to send payment validation codes.
- **E.2.2.4 – Web browser**: Software used by the client to access the e-store.
- **E.2.2.5 – Internet network**: Infrastructure enabling communication between all systems.

---

## E.3 – Constraints

### E.3.1 Functional Constraints

- **E.3.1.1** – Order payment can only be performed after a customer account has been created.
- **E.3.1.2** – A customer account must be created using a valid email address, a password, and a phone number.
- **E.3.1.3** – Out-of-stock products must be clearly indicated to the user.
- **E.3.1.4** – Each invoice must be accessible in the customer’s personal space.

---

### E.3.2 Security Constraints

- **E.3.2.1** – Customer passwords must follow defined complexity rules.
- **E.3.2.2** – Any payment validation must be confirmed using a confidential code sent to the customer’s phone number.

---

### E.3.3 Notification Constraints

- **E.3.3.1** – A confirmation message must be displayed after account creation.
- **E.3.3.2** – A confirmation email must be sent after account creation.
- **E.3.3.3** – An error message must be displayed in case of failure.
- **E.3.3.4** – Any site unavailability must be notified by email.

---

### E.3.4 Technical Constraints

- **E.3.4.1** – The user interface must be developed using Angular.
- **E.3.4.2** – The backend must be developed using Spring Boot.

---

## E.4 – Assumptions

- **E.4.1** – The Internet network is available.
- **E.4.2** – External services are operational.
- **E.4.3** – Customers provide accurate information.
- **E.4.4** – Customers use a compatible web browser.
- **E.4.5** – Users comply with e-store usage rules.

---

## E.5 – Effects on the Environment

- **E.5.1** – Creation, modification, and deletion of customer data.
- **E.5.2** – Stock updates following orders and cancellations.
- **E.5.3** – Generation and storage of electronic invoices.
- **E.5.4** – Sending notifications to customers.
- **E.5.5** – Impact on commercial management processes.

---

## E.6 – Invariants

- **E.6.1** – Each customer account is uniquely identified.
- **E.6.2** – A validated order corresponds to a confirmed payment.
- **E.6.3** – Product stock levels must never be negative.
- **E.6.4** – An issued invoice cannot be modified.
- **E.6.5** – Customer personal data must remain protected.
- **E.6.6** – Deleting a customer account results in data deletion or anonymization, except for legal retention.

---

# Goals Book – E-Store

## G.1 – Context

- **G.1.1** – Design an online sports equipment sales platform.

## G.2 – Current Situation

- **G.2.1** – Customers rely on physical stores.
- **G.2.2** – No specialized centralized online platform.

## G.3 – Expected Benefits

- **G.3.1** – Large product inventory.
- **G.3.2** – High concurrency support.
- **G.3.3** – Process automation.
- **G.3.4** – Fast payments and notifications.

## G.4 – Functional Overview

- **G.4.1** – Navigation by sports discipline.
- **G.4.2** – Advanced search and filtering.
- **G.4.3** – Cart management.
- **G.4.4** – Secure checkout.
- **G.4.5** – Profile and order history management.

## G.5 – Usage Scenarios

- **G.5.1** – Targeted purchase.
- **G.5.2** – Account update.
- **G.5.3** – Product comparison.
- **G.5.4** – Sales monitoring by admin.

## G.6 – Limitations

- **G.6.1** – No second-hand products.
- **G.6.2** – Limited delivery area.
- **G.6.3** – No video coaching (V1).
- **G.6.4** – Restricted payment methods.
- **G.6.5** – Manual product returns.

## G.7 – Stakeholders

- **G.7.1** – Customers.
- **G.7.2** – Product Owner.
- **G.7.3** – Development team.
- **G.7.4** – DevOps.
- **G.7.5** – Payment provider.
- **G.7.6** – GDPR authority.

---

# Project Book – E-Store

## P.1 – Roles

- **P.1.1** – Fullstack Developer.
- **P.1.2** – DevOps Engineer.
- **P.1.3** – Product Owner.

## P.2 – Technical Choices

- **P.2.1** – Angular, Java Spring Boot, PostgreSQL.
- **P.2.2** – Jira, GitHub, AWS.

## P.3 – Planning

- **P.3.1** – Defined milestones and objectives.

## P.4 – Tasks and Deliverables

- **P.4.1** – Catalog module.
- **P.4.2** – Shipping calculation system.
- **P.4.3** – Documentation pipeline.

## P.5 – Required Technologies

- **P.5.1** – Java 17, Angular CLI, AWS EC2.

## P.6 – Risks and Mitigation

- **P.6.1** – Downtime → Load balancing.
- **P.6.2** – Data breach → Encryption and hashing.

## P.7 – Requirements Process

- **P.7.1** – PEGS methodology.
- **P.7.2** – Automated versioning and PDF generation.

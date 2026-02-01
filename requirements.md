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



# Goals Book – E‑Store

## G.1 – Overall Context

**G1.1** – The E-store project aims to design a robust software solution for online sports equipment sales.

**G1.2** – The primary objective is to capture a market of demanding athletes by offering a platform capable of supporting high traffic and heavy loads.

---

## G.2 – Current Situation

**G2.1** – Currently, customers are required to visit physical stores to purchase specialized sports equipment.

**G2.2** – There is a significant lack of centralized online platforms offering technical sports gear with reliable real-time inventory tracking.

---

## G.3 – Expected Benefits

**G3.1 – Inventory Range**: Showcase a catalog of over 500 technical product references.

**G3.2 – Concurrency**: Support hundreds of simultaneous orders without performance degradation.

**G3.3 – Automation**: Reduce human errors in order entry and processing.

**G3.4 – Speed**: Ensure instant payment processing and immediate automated notifications.

---

## G.4 – Functionality Overview

**G4.1 – Navigation**: Allow users to browse products categorized by sports discipline (Bodybuilding, Fitness, Football, etc.).

**G4.2 – Advanced Search**: Provide a search engine with filters for weight, brand, and size.

**G4.3 – Cart Management**: Enable users to add, modify, or remove items in a cart, including a guest mode for non-authenticated users.

**G4.4 – Secure Checkout**: Implement a secure funnel where registration or login is mandatory for final payment.

**G4.5 – Profile & History**: Allow registered users to manage their profiles and track their order history.

---

## G.5 – High-level Usage Scenarios

**G5.1 – Targeted Purchase**: A user searches for "10kg Dumbbells", filters by brand, and completes the purchase immediately.

**G5.2 – Account Management**: A customer updates their shipping address in their profile following a relocation.

**G5.3 – Product Consultation**: A user compares the technical specifications of two different treadmills before deciding.

**G5.4 – Admin Tracking**: The Store Director (PO) reviews weekly sales statistics via the administration dashboard.

---

## G.6 – Limitations and Exclusions

**G6.1** – The platform does not support the sale of second-hand or used products.

**G6.2** – Delivery services are strictly restricted to Mainland France and Belgium.

**G6.3** – Integrated video coaching programs are excluded from this version (V1).

**G6.4** – Payments via check or cryptocurrency are not supported.

**G6.5** – Product returns are handled manually via Customer Support and are not automated in the UI.

---

## G.7 – Stakeholders and Requirements Sources

**G7.1 – Customers**: Amateur and professional athletes (Source for usability and performance requirements).

**G7.2 – Product Owner**: Store Manager (Source for profitability and business rules).

**G7.3 – Luce (Fullstack)**: Developer responsible for Java/Angular technical constraints.

**G7.4 – Abdel (DevOps)**: Engineer responsible for deployment and CI/CD requirements.

**G7.5 – Payment Provider**: External entity setting banking security constraints.

**G7.6 – GDPR**: Regulatory framework for legal constraints regarding data privacy.

---
---

# Project Book – E‑Store

## P.1 – Roles and Personnel

**P1.1 – Luce**: Lead developer in charge of Angular (Frontend) and Java Spring Boot (Backend) development.

**P1.2 – Abdel**: DevOps engineer in charge of AWS Architecture, CI/CD Pipeline, and Validation Testing.

**P1.3 – Product Owner**: Store Director responsible for business requirements and deliverable validation.

---

## P.2 – Imposed Technical Choices

**P2.1 – Frontend Stacks**: Development must use AngularJS.

**P2.2 – Backend Stacks**: Development must use Java Spring Boot.

**P2.3 – Database**: Centralized storage using PostgreSQL.

**P2.4 – Management Tools**: Jira for ticketing and project tracking.

**P2.5 – Version Control**: GitHub for code hosting and versioning.

**P2.6 – Infrastructure**: Cloud hosting provided by AWS (Amazon Web Services).

---

## P.3 – Schedule, Milestones, and Key Objectives

| Date (D+) | Mission | Phase | Key Objective |
| :--- | :--- | :--- | :--- |
| **D+7** | M1: Design | UI/UX Mockups | Validation of the graphic charter and checkout funnel. |
| **D+10** | M2: Catalog | Backend Dev | SQL Database import and functional search API. |
| **D+14** | M3: Checkout | Security | Payment gateway integration and "Sandbox" testing. |
| **D+25** | M4: CI/CD | Cloud Deployment | Production Go-Live on AWS with GitHub Actions. |

---

## P.4 – Tasks and Deliverables

**P4.1 – Catalog Module**: Development of filters and search functionality. **Deliverable**: Frontend source code.

**P4.2 – Shipping System**: Development of the delivery cost calculation logic. **Deliverable**: Tested Java API.

**P4.3 – Doc Pipeline**: Implementation of the requirements generation workflow. **Deliverable**: GitHub Actions `.yml` workflow.

---

## P.5 – Required Technology Elements

**P5.1 – Runtimes**: Java 17 and Maven for backend builds.

**P5.2 – CLI**: Angular CLI for frontend management.

**P5.3 – Compute**: AWS EC2 Instance for application hosting.

---

## P.6 – Risk and Mitigation Analysis

**P6.1 – Server Downtime**: Risk of service interruption. **Mitigation**: Implementation of AWS Load Balancing.

**P6.2 – Data Breach**: Risk of unauthorized access to sensitive data. **Mitigation**: Systematic SSL encryption and BCrypt password hashing.

---

## P.7 – Requirements Process and Report

**P7.1 – Methodology**: Project requirements are specified and maintained using the PEGS approach.

**P7.2 – Versioning**: Every Git "tag" triggers a new project version in ZIP format and generates a PDF version of the requirements.

**P7.3 – Automation**: The requirements specification PDF is automatically generated at each push via the CI/CD pipeline.


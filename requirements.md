---
title: "PEGS Requirements – E-Store"
subtitle: "Sports Equipment Online Store"
date: "2026-02-01"
toc-title: "Table des matières"
---

# Project Book – E-Store

## P.1 – Roles

- **P.1.1** – Fullstack Developer.
- **P.1.2** – DevOps Engineer.
- **P.1.3** – Product Owner.

## P.2 – Technical Choices

- **P2.1 – Frontend Stacks**: Development must use AngularJS.
- **P2.2 – Backend Stacks**: Development must use Java Spring Boot.
- **P2.3 – Database**: Centralized storage using PostgreSQL.
- **P2.4 – Management Tools**: Jira for ticketing and project tracking.
- **P2.5 – Version Control**: GitHub for code hosting and versioning.
- **P2.6 – Infrastructure**: Cloud hosting provided by AWS (Amazon Web Services).

## P.3 – Schedule, Milestones, and Key Objectives

| Date (D+) | Mission | Phase | Key Objective |
| :--- | :--- | :--- | :--- |
| **D+7** | M1: Design | UI/UX Mockups | Validation of the graphic charter and checkout funnel. |
| **D+10** | M2: Catalog | Backend Dev | SQL Database import and functional search API. |
| **D+14** | M3: Checkout | Security | Payment gateway integration and "Sandbox" testing. |
| **D+25** | M4: CI/CD | Cloud Deployment | Production Go-Live on AWS with GitHub Actions. |

## P.4 – Tasks and Deliverables

- **P4.1 – Catalog Module**: Development of filters and search functionality. **Deliverable**: Frontend source code.
- **P4.2 – Shipping System**: Development of the delivery cost calculation logic. **Deliverable**: Tested Java API.
- **P4.3 – Doc Pipeline**: Implementation of the requirements generation workflow. **Deliverable**: GitHub Actions `.yml` workflow.

## P.5 – Required Technologies

- **P5.1 – Runtimes**: Java 17 and Maven for backend builds.
- **P5.2 – CLI**: Angular CLI for frontend management.
- **P5.3 – Compute**: AWS EC2 Instance for application hosting.

## P.6 – Risks and Mitigation

- **P.6.1** – Downtime mitigated by load balancing.
- **P.6.2** – Data breach mitigated by encryption and hashing.

## P.7 – Requirements Process

- **P.7.1** – PEGS methodology.
- **P.7.2** – using Elisa.
- **P.7.3** – A Continuous Integration (CI) pipeline is configured via GitHub Actions to trigger automatically on every push or pull request to the main branch.
- **P.7.4** – The system utilizes the Pandoc tool to automatically convert the requirements.md source file into professional PDF and HTML formats.
- **P.7.5** – The generation process automatically includes a table of contents (--toc) and hierarchical section numbering (--number-sections) to ensure consistency with the Meyer Standard Plan.
- **P.7.6** – Upon completion of each workflow run, the generated files (requirements-E-store.pdf and .html) are archived as downloadable artifacts on GitHub, ensuring the most up-to-date version is always available for stakeholders.


---

# Environment Book – E-Store

## E.1 – Glossary

### E.1.1 – Actors

- **E.1.1.1 – Client**: A person who owns a customer account on the e-store and is able to browse products and make online purchases.
- **E.1.1.2 – Administrator**: A person responsible for managing the e-store, including product catalog, stock levels, orders, and system configuration.

### E.1.2 – Business Objects (Products and Documents)

- **E.1.2.1 – Product**: A generic item offered for sale on the e-store.
- **E.1.2.2 – Sports equipment**: A specific type of product intended for practicing or assisting a sports activity.
- **E.1.2.3 – Order**: A set of products selected by a client with the intention of purchasing.
- **E.1.2.4 – Invoice**: An electronic document summarizing the details of a completed sale.

### E.1.3 – Business Processes

- **E.1.3.1 – Sale**: Commercial process corresponding to order validation and successful payment.
- **E.1.3.2 – Payment**: Process allowing the client to pay for an order using secure payment methods.
- **E.1.3.3 – Delivery**: Process by which ordered products are delivered to a location chosen by the client.
- **E.1.3.4 – Order cancellation**: Action allowing the client to remove all or part of the products from an order before final validation.

### E.1.4 – System Elements

- **E.1.4.1 – E-store**: A virtual store allowing the online sale of goods or services via the Internet.
- **E.1.4.2 – Customer account**: A personal system space allowing a client to authenticate, place orders, and consult order and invoice history.
- **E.1.4.3 – Login**: The action allowing a client to access their customer account using identifiers.
- **E.1.4.4 – Authentication**: The system process of verifying the client’s identity during login.

## E.2 – Components

### E.2.1 – Internal Components

- **E.2.1.1 – User Interface (UI)**: Graphical interface allowing the client to interact with the e-store.
- **E.2.1.2 – Application server**: Component hosting backend code and handling user requests.
- **E.2.1.3 – Database**: Centralized storage system for clients, products, orders, and invoices.

### E.2.2 – External Components

- **E.2.2.1 – External payment service**: Third-party system responsible for validating and securing transactions.
- **E.2.2.2 – Email service**: External system used to send confirmation and notification emails.
- **E.2.2.3 – SMS service**: External system used to send payment validation codes.
- **E.2.2.4 – Web browser**: Software used by the client to access the e-store.
- **E.2.2.5 – Internet network**: Infrastructure enabling communication between all systems.

## E.3 – Constraints

### E.3.1 – Functional Constraints

- **E.3.1.1** – Order payment can only be performed after a customer account has been created.
- **E.3.1.2** – A customer account must be created using a valid email address, a password, and a phone number.
- **E.3.1.3** – Out-of-stock products must be clearly indicated to the user.
- **E.3.1.4** – Each invoice must be accessible in the customer’s personal space.

### E.3.2 – Security Constraints

- **E.3.2.1** – Customer passwords must follow defined complexity rules.
- **E.3.2.2** – Any payment validation must be confirmed using a confidential code sent to the customer’s phone number.

### E.3.3 – Notification Constraints

- **E.3.3.1** – A confirmation message must be displayed after account creation.
- **E.3.3.2** – A confirmation email must be sent after account creation.
- **E.3.3.3** – An error message must be displayed in case of failure.
- **E.3.3.4** – Any site unavailability must be notified by email.

### E.3.4 – Technical Constraints

- **E.3.4.1** – The user interface must be developed using Angular.
- **E.3.4.2** – The backend must be developed using Spring Boot.

## E.4 – Assumptions

- **E.4.1** – The Internet network is available.
- **E.4.2** – External services are operational.
- **E.4.3** – Customers provide accurate information.
- **E.4.4** – Customers use a compatible web browser.
- **E.4.5** – Users comply with e-store usage rules.

## E.5 – Effects on the Environment

- **E.5.1** – Creation, modification, and deletion of customer data.
- **E.5.2** – Stock updates following orders and cancellations.
- **E.5.3** – Generation and storage of electronic invoices.
- **E.5.4** – Sending notifications to customers.
- **E.5.5** – Impact on commercial management processes.

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

- **G1.1** – The E-store project aims to design a robust software solution for online sports equipment sales.
- **G1.2** – The primary objective is to capture a market of demanding athletes by offering a platform capable of supporting high traffic and heavy loads.

## G.2 – Current Situation

- **G2.1** – Currently, customers are required to visit physical stores to purchase specialized sports equipment.
- **G2.2** – There is a significant lack of centralized online platforms offering technical sports gear with reliable real-time inventory tracking.

## G.3 – Expected Benefits

- **G.3.1** – Large product inventory.
- **G.3.2** – High concurrency support.
- **G.3.3** – Process automation.
- **G.3.4** – Fast payments and notifications.

## G.4 – Functional Overview

- **G4.1 – Navigation**: Allow users to browse products categorized by sports discipline (Bodybuilding, Fitness, Football, etc.).
- **G4.2 – Advanced Search**: Provide a search engine with filters for weight, brand, and size.
- **G4.3 – Cart Management**: Enable users to add, modify, or remove items in a cart, including a guest mode for non-authenticated users.
- **G4.4 – Secure Checkout**: Implement a secure funnel where registration or login is mandatory for final payment.
- **G4.5 – Profile & History**: Allow registered users to manage their profiles and track their order history.

## G.5 – Usage Scenarios

- **G5.1 – Achat ciblé** : Un utilisateur recherche "Haltères 10kg", filtre par marque et finalise l'achat immédiatement.
- **G5.2 – Gestion de compte** : Un client met à jour son adresse de livraison dans son profil suite à un déménagement.
- **G5.3 – Consultation de produit** : Un utilisateur compare les spécifications techniques de deux tapis de course différents avant de se décider.
- **G5.4 – Suivi Administrateur** : Le directeur du magasin (PO) consulte les statistiques de ventes hebdomadaires via le tableau de bord d'administration.

## G.6 – Limitations

- **G6.1** – The platform does not support the sale of second-hand or used products.
- **G6.2** – Delivery services are strictly restricted to Mainland France and Belgium.
- **G6.3** – Integrated video coaching programs are excluded from this version (V1).
- **G6.4** – Payments via check or cryptocurrency are not supported.
- **G6.5** – Product returns are handled manually via Customer Support and are not automated in the UI.


## G.7 – Stakeholders

- **G7.1 – Customers**: Amateur and professional athletes (Source for usability and performance requirements).
- **G7.2 – Product Owner**: Store Manager (Source for profitability and business rules).
- **G7.3 – Fullstack**: Developer responsible for Java/Angular technical constraints.
- **G7.4 – DevOps**: Engineer responsible for deployment and CI/CD requirements.
- **G7.5 – Payment Provider**: External entity setting banking security constraints.
 - **G7.6 – GDPR**: Regulatory framework for legal constraints regarding data privacy.

---

# System Book – E-Store

## S.1 – Components

### S.1.1 – Frontend Web

Web user interface allowing customers to browse products, manage their account, place orders and perform payments through a web browser.

### S.1.2 – Backend Application

Central application layer implementing the business logic of the e-store and coordinating interactions between internal modules, the database and external services.

### S.1.3 – Authentication Module

Module responsible for user authentication, credential verification, session management and access control.

### S.1.4 – Order Management Module

Module responsible for creating, updating, validating and cancelling customer orders.

### S.1.5 – Payment Management Module

Module responsible for initiating payment requests, validating payments and handling payment failures through interaction with external payment services.

### S.1.6 – Inventory Management Module

Module responsible for managing product stock levels and determining product availability.

### S.1.7 – Invoicing Module

Module responsible for generating, storing and providing access to electronic invoices.

### S.1.8 – Database

Persistent SQL database ensuring data integrity, consistency and transactional safety for customer, product, order, payment and invoice data.

## S.2 – Functionality

### S.2.1 – Frontend Web

- **S.2.1.1** - The system shall display the product catalog with availability information.
- **S.2.1.2** - The system shall allow customers to create an account and authenticate.
- **S.2.1.3** - The system shall allow customers to create orders and initiate payments.
- **S.2.1.4** - The system shall allow customers to consult order history and invoices.

### S.2.2 – Authentication Module

- **S.2.2.1** - The system shall verify customer credentials during login.
- **S.2.2.2** - The system shall create and manage authenticated user sessions.
- **S.2.2.3** - The system shall reject invalid authentication attempts.
- **S.2.2.4** - The system shall deny access to protected resources for unauthenticated users.

### S.2.3 – Order Management Module

- **S.2.3.1** - The system shall create an order for an authenticated customer.
- **S.2.3.2** - The system shall allow products to be added to or removed from an order.
- **S.2.3.3** - The system shall validate an order only if all products are available.
- **S.2.3.4** - The system shall allow an order to be cancelled before payment validation.
- **S.2.3.5** - The system shall mark an order as confirmed only after successful payment.

### S.2.4 – Payment Management Module

- **S.2.4.1** - The system shall initiate a payment request for a validated order.
- **S.2.4.2** - The system shall require a confirmation code to validate a payment.
- **S.2.4.3** - The system shall reject any payment attempt without a valid confirmation code.
- **S.2.4.4** - The system shall handle payment failures by marking the order as unpaid.
- **S.2.4.5** - The system shall notify the customer in case of payment failure.

### S.2.5 – Inventory Management Module

- **S.2.5.1** - The system shall check product availability before order validation.
- **S.2.5.2** - The system shall decrease stock levels after successful order validation.
- **S.2.5.3** - The system shall restore stock levels after order cancellation.
- **S.2.5.4** - The system shall prevent stock levels from becoming negative.

### S.2.6 – Invoicing Module

- **S.2.6.1** - The system shall generate an invoice after successful payment.
- **S.2.6.2** - The system shall store the invoice in the database.
- **S.2.6.3** - The system shall make invoices accessible in the customer’s personal space.
- **S.2.6.4** - The system shall prevent modification of issued invoices.

## S.3 – Interfaces

### S.3.1 – User Interface

Web interface allowing customers to interact with the e-store.

### S.3.2 – Payment Interface

Interface used to communicate with external payment services for payment initiation and validation.

### S.3.3 – Notification Interfaces

Interfaces used to send email and SMS notifications to customers.

### S.3.4 – Administration Interface

Interface allowing administrators to manage products, stock levels, orders and invoices, and to monitor system activity.

## S.4 – Detailed Usage Scenarios

### S.4.1 – Create a customer account

A user enters personal information. The system validates the data and creates a customer account.

### S.4.2 – Place an order

A customer selects products. The system checks availability and creates an order.

### S.4.3 – Pay an order

The customer initiates payment. The system validates the confirmation code and confirms the order.

### S.4.4 – Cancel an order

The customer cancels an unpaid order. The system updates stock levels accordingly.

### S.4.5 – Payment failure

If payment validation fails, the system marks the order as unpaid and notifies the customer.

### S.4.6 – Stock unavailable during validation

If stock becomes unavailable during order validation, the system prevents confirmation and informs the customer.

## S.5 – Prioritization

- **S.5.1 - Critical** – Required for production release  
  Authentication, order validation, payment processing

- **S.5.2 - High** – Required for normal commercial operation  
  Inventory management, invoicing, administration interface

- **S.5.3 - Medium** – Improves user experience  
  Order history consultation

- **S.5.4 - Low** – Optional enhancements  
  Interface customization

## S.6 – Verification and Acceptance Criteria

- **S.6.1** – A customer can create an account and authenticate successfully.
- **S.6.2** – An authenticated customer can create, validate and pay for an order.
- **S.6.3** – Any payment attempt without a valid confirmation code is rejected.
- **S.6.4** – Stock levels are updated after each order validation or cancellation.
- **S.6.5** – An invoice is generated and accessible after successful payment.
- **S.6.6** – The system prevents access to customer data by unauthorized users.
- **S.6.7** – The system rejects invalid authentication attempts within an acceptable response time.

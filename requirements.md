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

- **P.6.1** – Downtime mitigated by load balancing.
- **P.6.2** – Data breach mitigated by encryption and hashing.

## P.7 – Requirements Process

- **P.7.1** – PEGS methodology.
- **P.7.2** – Automated versioning and PDF generation.

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
- **G.5.4** – Sales monitoring by administrator.

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

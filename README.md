# SILC Application Models Documentation

This document outlines the models used in the SILC application, detailing their purpose, relationships, and key fields.

## Models Overview

### `SILCGroup`
- Represents a SILC group.
- Fields include `name`, `location`, `date_started`, `email`, and `contact_number`.
- Links to `Member` via ForeignKey in the `Member` model.

### `Member`
- Represents a member of a SILC group.
- Fields include `name`, `id_number`, `phone_number`, `email`, `role`, `date_of_joining`, `status`, and `gender`.
- Linked to `SILCGroup` through a ForeignKey relationship.
- Serves as a foreign key target for `Saving`, `Loan`, `SocialFund`, and `Fine` models.

### `Role`
- Defines roles within the SILC group, such as Chairperson or Treasurer.
- Contains a `name` and `permissions` field.

### `GroupRole`
- Associates `User` with a `Role` in a `SILCGroup`.
- Uses ForeignKey relationships to link `User`, `Role`, and `SILCGroup`.

### `Saving`
- Tracks savings contributions by members.
- Linked to `Member` through a ForeignKey.
- Includes `amount`, `date_contributed`, and `notes`.

### `Loan`
- Records loans issued to members.
- Fields include `amount`, `interest_rate`, `date_issued`, `repayment_due_date`, and `status`.
- `Member` is linked via ForeignKey.

### `SocialFund`
- Manages contributions to a social fund.
- Linked to `Member` and includes `contribution_amount`, `date_contributed`, and `purpose`.

### `Fine`
- Tracks fines imposed on members.
- Includes `amount`, `reason`, `date_issued`, and `status`.
- Linked to `Member`.

### `Cycle`
- Represents operational cycles of the SILC group, typically lasting a year.
- Contains `start_date`, `end_date`, and `active` status.

### `Guarantor`
- Details guarantors for loans.
- Fields include `id_number`, `name`, `email`, `loan`, and `relationship_with_loanee`.
- Linked to `Loan` via ForeignKey.

## Relationships

- **SILCGroup to Member**: One-to-Many. A group has many members.
- **Member to Savings/Loans/SocialFund/Fines**: One-to-Many. A member can have multiple records in each of these models.
- **Loan to Guarantor**: One-to-Many. A loan can have multiple guarantors.

## Functionality

- The application tracks all financial activities of a SILC group, including savings, loans, social fund contributions, fines, and operational cycles.
- Guarantors are associated with loans to manage risk.
- Group roles allow for role-based access and functionalities within the application.

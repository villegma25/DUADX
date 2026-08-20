# SQL Normalization Exercises

=========================================================
EXERCISE 1 - ORDERS
=========================================================

## Original Table (UNF)

| Order ID | Customer Name | Customer Phone | Address | Item ID | Item Name | Price | Quantity | Special Request | Delivery Time |
|----------|---------------|----------------|---------|---------|-----------|-------|----------|-----------------|--------------|
|001|Alice|123-456-7890|123 Main St|101|Cheeseburger|8|2|No onions|6:00 PM|
|001|Alice|123-456-7890|123 Main St|102|Fries|3|1|Extra ketchup|6:00 PM|
|002|Bob|987-654-3210|456 Elm St|103|Pizza|12|1|Extra cheese|7:30 PM|
|002|Bob|987-654-3210|4th Avenue|102|Fries|3|2|None|7:30 PM|
|003|Claire|555-123-4567|789 Oak St|105|Salad|6|1|No croutons|12:00 PM|
|004|Claire|555-123-4567|464 Georgia St|106|Water|1|1|None|5:00 PM|

---------------------------------------------------------
FIRST NORMAL FORM (1NF)
---------------------------------------------------------

Primary Key: (OrderID, ItemID)

All values are atomic and there are no repeating groups.

Problems:
- Customer information is repeated.
- Product information is repeated.
- Delivery time is repeated.
- Update anomalies.
- Insert anomalies.
- Delete anomalies.

---------------------------------------------------------
SECOND NORMAL FORM (2NF)
---------------------------------------------------------

Customers

| CustomerID | CustomerName | Phone |
|------------|--------------|-------|
|1|Alice|123-456-7890|
|2|Bob|987-654-3210|
|3|Claire|555-123-4567|

Products

| ItemID | ItemName | Price |
|--------|----------|------|
|101|Cheeseburger|8|
|102|Fries|3|
|103|Pizza|12|
|105|Salad|6|
|106|Water|1|

Orders

| OrderID | CustomerID | Address | DeliveryTime |
|---------|------------|---------|-------------|
|001|1|123 Main St|6:00 PM|
|002|2|456 Elm St|7:30 PM|
|003|3|789 Oak St|12:00 PM|
|004|3|464 Georgia St|5:00 PM|

OrderDetails

| OrderID | ItemID | Quantity | SpecialRequest |
|---------|--------|----------|----------------|
|001|101|2|No onions|
|001|102|1|Extra ketchup|
|002|103|1|Extra cheese|
|002|102|2|None|
|003|105|1|No croutons|
|004|106|1|None|

---------------------------------------------------------
THIRD NORMAL FORM (3NF)
---------------------------------------------------------

Customers

| CustomerID | CustomerName | Phone |
|------------|--------------|-------|
|1|Alice|123-456-7890|
|2|Bob|987-654-3210|
|3|Claire|555-123-4567|

Addresses

| AddressID | Address |
|-----------|----------------|
|1|123 Main St|
|2|456 Elm St|
|3|4th Avenue|
|4|789 Oak St|
|5|464 Georgia St|

Products

| ItemID | ItemName | Price |
|--------|----------|------|
|101|Cheeseburger|8|
|102|Fries|3|
|103|Pizza|12|
|105|Salad|6|
|106|Water|1|

Orders

| OrderID | CustomerID | AddressID | DeliveryTime |
|---------|------------|-----------|-------------|
|001|1|1|6:00 PM|
|002|2|2|7:30 PM|
|003|3|4|12:00 PM|
|004|3|5|5:00 PM|

OrderDetails

| OrderID | ItemID | Quantity | SpecialRequest |
|---------|--------|----------|----------------|
|001|101|2|No onions|
|001|102|1|Extra ketchup|
|002|103|1|Extra cheese|
|002|102|2|None|
|003|105|1|No croutons|
|004|106|1|None|

Justification

1NF
- Eliminated repeating groups.
- Every field contains a single value.

2NF
- Customer data moved to Customers.
- Product data moved to Products.
- Order details separated.

3NF
- Addresses moved to their own table.
- Every non-key attribute depends only on the primary key.
- Eliminates update, insertion, and deletion anomalies.

# EXERCISE 2 - CARS NORMALIZATION

=========================================================
ORIGINAL TABLE
=========================================================

| VIN | Make | Model | Year | Color | Owner ID | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|-----|------|-------|------|-------|----------|------------|-------------|-------------------|------------------|
|1HGCM82633A|Honda|Accord|2003|Silver|101|Alice|123-456-7890|ABC Insurance|Fire & Theft|
|1HGCM82633A|Honda|Accord|2003|Silver|102|Bob|987-654-3210|XYZ Insurance|Full Cover|
|5J6RM4H79EL|Honda|CR-V|2014|Blue|103|Claire|555-123-4567|DEF Insurance|Collision|
|1G1RA6EH1FU|Chevrolet|Volt|2015|Red|104|Dave|111-222-3333|GHI Insurance|Basic Legal|

=========================================================
FIRST NORMAL FORM (1NF)
=========================================================

The first step is to verify that all attributes contain atomic
values and that there are no repeating groups.

The original table contains atomic values, so it satisfies 1NF.

However, there is a problem with repeated information:

- Make and Model information can be repeated for many vehicles.
- Owner information can be repeated if an owner has multiple cars.
- Insurance company information can be repeated for multiple policies.

For the original data, a possible composite key is:

(VIN, Owner ID)

This is because the same VIN can appear with different owners.

At this stage, the table is:

Cars

| VIN | Make | Model | Year | Color | OwnerID | OwnerName | OwnerPhone | InsuranceCompany | InsurancePolicy |
|-----|------|-------|------|-------|---------|-----------|------------|------------------|-----------------|
|1HGCM82633A|Honda|Accord|2003|Silver|101|Alice|123-456-7890|ABC Insurance|Fire & Theft|
|1HGCM82633A|Honda|Accord|2003|Silver|102|Bob|987-654-3210|XYZ Insurance|Full Cover|
|5J6RM4H79EL|Honda|CR-V|2014|Blue|103|Claire|555-123-4567|DEF Insurance|Collision|
|1G1RA6EH1FU|Chevrolet|Volt|2015|Red|104|Dave|111-222-3333|GHI Insurance|Basic Legal|

=========================================================
SECOND NORMAL FORM (2NF)
=========================================================

2NF requires that every non-key attribute depends on the whole
primary key and not only on part of a composite key.

The original table has a composite key:

(VIN, OwnerID)

Some information depends only on VIN:

- Make
- Model
- Year
- Color

Other information depends only on OwnerID:

- OwnerName
- OwnerPhone

Therefore, the table contains partial dependencies.

To eliminate these dependencies, the information is separated
into different tables.

---------------------------------------------------------
CARS
---------------------------------------------------------

| VIN | Make | Model | Year | Color |
|-----|------|-------|------|-------|
|1HGCM82633A|Honda|Accord|2003|Silver|
|5J6RM4H79EL|Honda|CR-V|2014|Blue|
|1G1RA6EH1FU|Chevrolet|Volt|2015|Red|

---------------------------------------------------------
OWNERS
---------------------------------------------------------

| OwnerID | OwnerName | OwnerPhone |
|---------|-----------|-------------|
|101|Alice|123-456-7890|
|102|Bob|987-654-3210|
|103|Claire|555-123-4567|
|104|Dave|111-222-3333|

---------------------------------------------------------
CAR OWNERSHIP
---------------------------------------------------------

| VIN | OwnerID | InsuranceCompany | InsurancePolicy |
|-----|---------|------------------|-----------------|
|1HGCM82633A|101|ABC Insurance|Fire & Theft|
|1HGCM82633A|102|XYZ Insurance|Full Cover|
|5J6RM4H79EL|103|DEF Insurance|Collision|
|1G1RA6EH1FU|104|GHI Insurance|Basic Legal|

At this point, partial dependencies have been removed.

=========================================================
THIRD NORMAL FORM (3NF)
=========================================================

3NF requires that there are no transitive dependencies.

The previous Cars table still has the following dependency:

Make → Model

For example, Honda can have many models:

Honda → Accord
Honda → CR-V
Honda → Civic
Honda → Pilot

If there are 1,000 Toyota Corolla vehicles, storing Toyota and
Corolla in every vehicle record would create unnecessary
duplication.

Therefore, Make and Model must be separated.

The Insurance information also contains a dependency:

InsuranceCompany → InsurancePolicy

An insurance company can have many different policies.

For example:

ABC Insurance → Policy 1
ABC Insurance → Policy 2
ABC Insurance → Policy 3

Therefore, insurance companies and insurance policies should also
be separated.

---------------------------------------------------------
MAKES
---------------------------------------------------------

| MakeID | Make |
|--------|------|
|1|Honda|
|2|Chevrolet|

---------------------------------------------------------
MODELS
---------------------------------------------------------

| ModelID | Model | MakeID |
|---------|-------|--------|
|1|Accord|1|
|2|CR-V|1|
|3|Volt|2|

---------------------------------------------------------
CARS
---------------------------------------------------------

| VIN | ModelID | Year | Color |
|-----|---------|------|-------|
|1HGCM82633A|1|2003|Silver|
|5J6RM4H79EL|2|2014|Blue|
|1G1RA6EH1FU|3|2015|Red|

---------------------------------------------------------
OWNERS
---------------------------------------------------------

| OwnerID | OwnerName | OwnerPhone |
|---------|-----------|-------------|
|101|Alice|123-456-7890|
|102|Bob|987-654-3210|
|103|Claire|555-123-4567|
|104|Dave|111-222-3333|

---------------------------------------------------------
INSURANCE COMPANIES
---------------------------------------------------------

| CompanyID | CompanyName |
|-----------|-------------|
|1|ABC Insurance|
|2|XYZ Insurance|
|3|DEF Insurance|
|4|GHI Insurance|

---------------------------------------------------------
INSURANCE POLICIES
---------------------------------------------------------

| PolicyID | PolicyName | CompanyID |
|----------|------------|-----------|
|1|Fire & Theft|1|
|2|Full Cover|2|
|3|Collision|3|
|4|Basic Legal|4|

---------------------------------------------------------
CAR OWNERSHIP
---------------------------------------------------------

| VIN | OwnerID | PolicyID |
|-----|---------|----------|
|1HGCM82633A|101|1|
|1HGCM82633A|102|2|
|5J6RM4H79EL|103|3|
|1G1RA6EH1FU|104|4|

=========================================================
FINAL 3NF STRUCTURE
=========================================================

Makes
    |
    | 1:N
    ↓
Models
    |
    | 1:N
    ↓
Cars
    |
    | 1:N
    ↓
CarOwnership
    |
    | N:1
    ↓
Owners


InsuranceCompanies
    |
    | 1:N
    ↓
InsurancePolicies
    |
    | 1:N
    ↓
CarOwnership

=========================================================
JUSTIFICATION
=========================================================

1NF

The table was already in 1NF because all values are atomic and
there are no repeating groups.

2NF

The original table used a composite key (VIN, OwnerID).

Vehicle information depended only on VIN, while owner information
depended only on OwnerID.

Therefore, Cars and Owners were separated, and the relationship
between them was placed in CarOwnership.

3NF

The previous Cars table still contained the dependency:

Make → Model

Model depends on Make rather than directly on VIN.

To eliminate this transitive dependency, Makes and Models were
separated.

The insurance information also contained the dependency:

InsuranceCompany → InsurancePolicy

A single insurance company can have many policies.

Therefore, InsuranceCompanies and InsurancePolicies were
separated.

The final design has no unnecessary repetition and each
non-key attribute depends only on the primary key of its table.

The final structure therefore satisfies Third Normal Form (3NF).
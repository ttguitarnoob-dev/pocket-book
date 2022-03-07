# pocket-book
PocketBook (working name) Will be an app designed to help you plan your monthly finances in the simplest way possible. Create monthly budgets, list all expenses and calculate totals, update income for each month, and keep track of debt.

## Your tech stack (frontend, backend, database)
React front end with basic route navigation
Django Rest framework backend with postgresql database
## List of backend models and their properties
### BudgetList
- Retrieve every created budget per user
### CreateBudget
- fields > name, date_range, base_income, additional_income
- Success url > details page of that budget, where user can add expenses
### BudgetUpdate
- only used for updating fields used in create budget
### AddExpense
- fields > name, amount, date_due
- success url? Same budget details page
### DeleteBudget
- success url > budget list page
### NewUser
- Username
- Password
- Email
## React component hierarchy (if applicable)
- Ever-present nav bar
- Login Homepage
- Daily financial tips (if applicable api is available)
- Budget List
- Create/Edit budget forms
- Expense create interface
- budget detail display(total expenses, remaining budget amount)
## User stories
- As a user, I would like to enter the home page and either login, create an account or click on a link for financial tips
- As a user, I would like to create a budget for a pay period or month, and add my total income for that period
- As as user, I would like to add expenses to the budget and see the total amount added every time I add an expense
## Wireframes
![Screen Shot 2022-03-06 at 8 52 56 PM](https://media.git.generalassemb.ly/user/40858/files/12a0f580-9d91-11ec-8ca8-b02040c1dbf4)
![Screen Shot 2022-03-06 at 8 54 31 PM](https://media.git.generalassemb.ly/user/40858/files/16cd1300-9d91-11ec-8223-b6f1d335a9cb)
![Screen Shot 2022-03-06 at 8 58 51 PM](https://media.git.generalassemb.ly/user/40858/files/1a609a00-9d91-11ec-962a-0bdff02e4bc3)
![Screen Shot 2022-03-06 at 8 59 35 PM](https://media.git.generalassemb.ly/user/40858/files/1b91c700-9d91-11ec-8f01-25ef589f21e3)
![Screen Shot 2022-03-06 at 9 03 50 PM](https://media.git.generalassemb.ly/user/40858/files/1df42100-9d91-11ec-8ffb-3515002850fc)

## Anything else your squad lead should know
### Stretch Goals
- Calendar view with due dates
- Random user avatar on account creation
- Debt calculation/management/tracking
- Daily financial tips
- Mobile first design
- Choose between monthly(will then allow you to choose which month/year) or "other" budget periods

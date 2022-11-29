About the Dataset
Dataset used: Churn_modelling

Abstract

The model was fed with data that enabled it to give an outcome that predicted  if a customer remained using the service or exited from using the service.

Introduction to the problem

When customers or subscribers stop doing business with a company or service, it is known as customer churn. Customers in the telecom sector can choose from a wide range of service providers and actively swap between them. The telecommunications industry has a 15 to 25% yearly turnover rate in this fiercely competitive market. One of the biggest threats to revenue loss in the telecom sector is customer churn. Fostering customer loyalty is essential since the cost of recruiting new customers can be up to 25 times higher than the cost of keeping existing ones.
in our case a bank. Some studies show that acquiring new customers can cost 5 times more than that of satisfying and retaining existing customers. Thus tracking of bank customer churn rate through prediction will help in reducing marketing costs, lead to increase in capital ,expanding total customers and a lot more.
 For the dataset  we are going to work with it will enable us to predict a customer's churn.
The  dataset contains the following columns : RowNumber,CustomerId,Surname,CreditScore,Georaphy,Gender,Age,Tenure,Balance,NumOfProdcuts,HasCrCard,IsActiveMember,EstimatedSalary,Exited.
Variables:
RowNumber — corresponds to the record (row) number and has no effect on the output. This column will be removed.
CustomerId — contains random values and has no effect on customers leaving the bank. This column will be removed.
Surname — the surname of a customer has no impact on their decision to leave the bank. This column will be removed.
CreditScore — can have an effect on customer churn, since a customer with a higher credit score is less likely to leave the bank.
Geography — a customer’s location can affect their decision to leave the bank. We’ll keep this column.
Gender — it’s interesting to explore whether gender plays a role in a customer leaving the bank. We’ll include this column, too.
Age — this is certainly relevant, since older customers are less likely to leave their bank than younger ones.
Tenure — refers to the number of years that the customer has been a client of the bank. Normally, older clients are more loyal and less likely to leave a bank.
Balance — also a very good indicator of customer churn, as people with a higher balance in their accounts are less likely to leave the bank compared to those with lower balances.
NumOfProducts — refers to the number of products that a customer has purchased through the bank.
HasCrCard — denotes whether or not a customer has a credit card. This column is also relevant, since people with a credit card are less likely to leave the bank. (0=No,1=Yes)
IsActiveMember — active customers are less likely to leave the bank, so we’ll keep this. (0=No,1=Yes)
EstimatedSalary — as with balance, people with lower salaries are more likely to leave the bank compared to those with higher salaries.
Exited — whether or not the customer left the bank. This is what we have to predict. (0=No,1=Yes)

#variables for the insurance calculation
business_scale = input("size of the business (Small,Medium,Large): ")#Size of the business 

risk_exposure = input("Enter the risk factor (Low, Medium, High): ") # Low, Medium, or High

data_type = input("Enter the type of data (sensitive/non-sensitive): ")# Sensitive or Non-sensitive

potential_loss = int(input("Enter the expected loss: "))# Potential financial loss in case of a cyber-attack

annual_revenue = int(input("Enter the annual revenue: "))# Annual revenue of the business

compliance_requirements = input("is the business in complient with requirements(yes/no): ")# Whether the business has compliance requirements

#business size
if business_scale == "Small":
    base_premium = 5000
elif business_scale == "Medium":
    base_premium = 10000
else:
    base_premium = 20000

#risk exposure
if risk_exposure == "Low":
    risk_factor = 0.5
elif risk_exposure == "Medium":
    risk_factor = 1
else:
    risk_factor = 2

#data sensitivity
if data_type == "Sensitive":
    data_factor = 1.5
else:
    data_factor = 1

#potential loss
if potential_loss <= 1000000:
    loss_factor = 1
elif potential_loss <= 5000000:
    loss_factor = 1.5
else:
    loss_factor = 2

#business revenue
if annual_revenue <= 1000000:
    revenue_factor = 1
elif annual_revenue <= 10000000:
    revenue_factor = 1.5
else:
    revenue_factor = 2

#compliance requirements
if compliance_requirements == "yes":
    compliance_factor = 2
else:
    compliance_factor = 1

# Calculating the final insurance premium based on all factors
insurance_premium = base_premium * risk_factor * data_factor * loss_factor * revenue_factor *compliance_factor


print("The insurance for this company is " + str(insurance_premium))

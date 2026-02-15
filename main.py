import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
customers = pd.read_csv(r'D:\Python project 1\Data tables\Customers.csv')
orders = pd.read_csv(r'D:\Python project 1\Data tables\Orders.csv')
order_items = pd.read_csv(r'D:\Python project 1\Data tables\Order items.csv')

state_map = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapa',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceara',
    'DF': 'Distrito Federal',
    'ES': 'Espirito Santo',
    'GO': 'Goias',
    'MA': 'Maranhao',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Para',
    'PB': 'Paraiba',
    'PR': 'Parana',
    'PE': 'Pernambuco',
    'PI': 'Piaui',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondonia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'Sao Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

# Data cleaning for customer table

customers.columns
# print(customers.drop(columns = ['Unnamed: 5', 'Unnamed: 6']))
customers.head()
customers.dtypes
customers.duplicated().sum()
customers.isnull().sum()

# Data cleaning for orders table

orders.head()
orders.dtypes
# print(orders.isnull().sum ())
orders[orders['order_delivered_customer_date'].isnull()]['order_status'].value_counts()
# Not dropping null values because the nulls have business logic
orders.duplicated().sum()

# Data cleaning for order items table

order_items.head()
orders.dtypes
order_items.isna().sum()
order_items.duplicated().sum()

orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'], dayfirst=True, errors='coerce')

# Analytics and insights

df = orders.merge(order_items, on = 'order_id', how = 'left')
revenue_per_order = ( df.assign(total_revenue = df['price'] + df['freight_value']).groupby('order_id')['total_revenue'].sum()).reset_index(name = 'revenue_per_order')
df = orders.merge(order_items, on = 'order_id', how = 'left')
total_revenue = ( df.assign(total_revenue = df['price'] + df['freight_value'])['total_revenue'].sum()) 
print(total_revenue)

# Question 1: What is the monthly revenue trend?
df = orders.merge(order_items, on = 'order_id', how = 'left')
df['monthly_revenue'] = df['price'] + df['freight_value']
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['month'] = df['order_purchase_timestamp'].dt.to_period('M')
monthly_revenue = (df.groupby('month')['monthly_revenue'].sum().reset_index().sort_values('month'))
monthly_revenue['MOM_growth%'] = (monthly_revenue['monthly_revenue'].pct_change().mul(100).round(2))
# print(monthly_revenue) 

# Visualization:

# Revenue by months
monthly_revenue['month'] = monthly_revenue['month'].dt.to_timestamp()
plt.figure(figsize=(10,5))
plt.plot(monthly_revenue['month'], monthly_revenue['monthly_revenue'], marker = 'o')
plt.ticklabel_format(style = 'plain', axis = 'y')
plt.xticks(rotation = 45)
plt.title("Monthly Revenue Trend")
plt.xlabel("Months")
plt.ylabel("Revenue (BRL")
plt.tight_layout()
# plt.savefig('Revenue by months.png')
# plt.show()

# Monthly revenue vs MOM growth
# fig, ax1 = plt.subplots(figsize=(10,5))
# ax1.plot(monthly_revenue['month'].dt.to_timestamp(),
# monthly_revenue['monthly_revenue'], marker = 'o', linewidth = 2)
# ax1.set_xlabel("Month")
# ax1.set_ylabel("Revenue (BRL)")
# ax1.ticklabel_format(style = 'plain', axis = 'y')
# ax1.tick_params(axis = 'x', rotation = 45)
# ax2 = ax1.twinx()
# ax2.plot(monthly_revenue['month'].dt.to_timestamp(),
# monthly_revenue['MOM_growth%'], linestyle = '--', marker = 'x')
# ax2.set_ylabel("MOM Growth (%)")
# plt.title("Monthly Revenue & MOM Growth")
# plt.tight_layout()
# plt.savefig('Monthly revenue vs MOM growth.png')
# plt.show()

# Question 2: What is the average order value (AOV)?

df = orders.merge(order_items, on = 'order_id', how = 'left')
df['total_revenue'] = df['price'] + df['freight_value']
average_order_value = (df.groupby('order_id')['total_revenue'].sum().mean().round(2))
# print(average_order_value)

# Question 3: What percentage of revenue comes from top 10% customers? (Pareto 80/20 rule)

df = customers.merge(orders, on = 'customer_id', how = 'left')
df = df.merge(order_items, on = 'order_id', how = 'left')
df['total_revenue'] = df['price'] + df['freight_value']
revenue_per_customer = df.groupby('customer_unique_id')['total_revenue'].sum().reset_index().sort_values('total_revenue', ascending = False)
top_20_count = int(len(revenue_per_customer) * 0.20)
percentage_contribution = ( revenue_per_customer.head(top_20_count)['total_revenue'].sum() / revenue_per_customer['total_revenue'].sum())*100
# print(round(percentage_contribution, 2))

# # Visualization of the Pareto Effect:

revenue_per_customer = revenue_per_customer.sort_values('total_revenue', ascending = False).reset_index(drop = True)
revenue_per_customer['cumulative_revenue_%'] = (revenue_per_customer['total_revenue'].cumsum() / 
                                                revenue_per_customer['total_revenue'].sum()) *100
customer_percent = np.arange(1, len(revenue_per_customer) + 1) / len(revenue_per_customer) * 100
plt.figure(figsize = (10, 6))
plt.plot(customer_percent, revenue_per_customer['cumulative_revenue_%'], linewidth = 2)
plt.axvline(x = 20, linestyle = '--')
plt.axhline(y = 80, linestyle = '--')
plt.xlabel("Percentage of Customers (%)")
plt.ylabel("Cumulative Revenue (%)")
plt.title("Pareto Analysis: Revenue Concentration")
plt.grid(True)
plt.tight_layout()
# plt.savefig('Pareto Effect.png')
# plt.show()

# Question 4: What is the repeat purchase rate (%)?

df = customers.merge(orders, on = 'customer_id', how = 'left')
order_count = df.groupby('customer_unique_id')['order_id'].nunique()
repeat_customers = order_count[order_count > 1].count()
total_customers = order_count.count()
repeat_purchase_rate = (repeat_customers / total_customers) * 100
# print(round(repeat_purchase_rate, 2))

# Question 5: What is the average delivery time?

df = customers.merge(orders, on = 'customer_id', how = 'left')
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
delivered_orders = df[df['order_status'] == 'delivered']
delivered_orders['delivery_time_days'] = (delivered_orders['order_delivered_customer_date'] - delivered_orders['order_purchase_timestamp']).dt.days
average_delivery_time = delivered_orders['delivery_time_days'].mean()
# print(round(average_delivery_time, 2))

# Question 6: What is the percentage of orders that were delivered late?

delivered_orders = orders[orders['order_status'] == 'delivered'].copy()
delivered_orders['order_delivered_customer_date'] = pd.to_datetime(delivered_orders['order_delivered_customer_date'], format='%d-%m-%Y %H:%M')
delivered_orders['order_estimated_delivery_date'] = pd.to_datetime(delivered_orders['order_estimated_delivery_date'], format='%d-%m-%Y %H:%M')
delivered_orders['is late'] = (delivered_orders['order_delivered_customer_date'] > 
delivered_orders['order_estimated_delivery_date'])
late_percentage = delivered_orders['is late'].mean() * 100
# print(round(late_percentage, 2))

# Verification:
# print("Total orders: ", len(orders))
# print("Delivered orders: ", len(orders[orders['order_status'] == 'delivered']))
# print("Rows used for late calculation: ", len(delivered_orders))
# print(delivered_orders['is late'].sum())
# print(round(delivered_orders['is late'].mean() * 100, 2))
# print(delivered_orders['order_delivered_customer_date'].dtype)
# print(delivered_orders['order_estimated_delivery_date'].dtype)
# print((delivered_orders['order_delivered_customer_date'] > delivered_orders['order_estimated_delivery_date']).sum())
# print((delivered_orders['order_delivered_customer_date'] > delivered_orders['order_estimated_delivery_date']).value_counts())
# print((delivered_orders['order_delivered_customer_date'] - delivered_orders['order_estimated_delivery_date']).describe())

# Question 7: Which states generate highest revenue?

df1 = order_items.merge(orders, on = 'order_id', how = 'left')
df2 = df1.merge(customers, on = 'customer_id', how = 'left')
df2['total_revenue'] = df2['price'] + df2['freight_value']
revenue_by_states = df2.groupby('customer_state')['total_revenue'].sum().sort_values(ascending = False).head(10)
revenue_by_states = revenue_by_states.reset_index()
revenue_by_states['state_full'] = revenue_by_states['customer_state'].map(state_map)
# print(revenue_by_states)

# Visualization:

revenue_by_states['revenue_million'] = revenue_by_states['total_revenue'] / 100000
plt.figure(figsize = (10, 6))
plt.barh(revenue_by_states['state_full'], revenue_by_states['revenue_million'])
plt.xlabel("Total Revenue in millions (BRL)")
plt.ylabel("States")
plt.title("Top 10 states by revenue")
plt.ticklabel_format(style = 'plain', axis = 'x')
plt.tight_layout()
# plt.savefig('Revenue by states.png')
# plt.show()

# Question 8: Which states have highest late delivery rates?

df = orders.merge(customers, on = 'customer_id', how = 'left')
df = df[df['order_status']=='delivered'].copy()
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'], format='%d-%m-%Y %H:%M')
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'], format='%d-%m-%Y %H:%M')
df['is late'] = (df['order_delivered_customer_date'] > df['order_estimated_delivery_date'])
late_by_state = df.groupby('customer_state')['is late'].mean().mul(100).round(2).sort_values(ascending = False)
late_by_state.index = late_by_state.index.map(state_map)
# print(late_by_state)

# Visualization:

plt.figure(figsize = (12, 6))
late_by_state.head(10).plot(kind = 'bar')
plt.title("Late delivery percentage by states")
plt.xlabel("States")
plt.ylabel("Late Delivery (%)")
plt.xticks(rotation = 90)
plt.tight_layout()
# plt.savefig("Late delivery by states")
# plt.show()

# Question 9: How much revenue is derived from delivered order?

df = order_items.merge(orders, on = 'order_id', how = 'left')
df = df[df['order_status'] == 'delivered'].copy()
df['total_revenue'] = df['price'] + df['freight_value']
Revenue_by_delivered = df['total_revenue'].sum()
# print(Revenue_by_delivered)



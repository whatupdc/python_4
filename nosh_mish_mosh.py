import nosh_mish_mosh_1
import numpy as np 

all_visitors = nosh_mish_mosh_1.customer_visits
paying_visitors = nosh_mish_mosh_1.purchasing_customers

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)
baseline_percent = 100.0 * paying_visitor_count / total_visitor_count
payment_history = nosh_mish_mosh_1.money_spent
average_payment = np.mean(payment_history)
new_customers_needed = np.ceil(1240 / average_payment)
percentage_point_increase = 100.0 * new_customers_needed / total_visitor_count
minimum_detectable_effect = 100.0 * percentage_point_increase / baseline_percent

print (baseline_percent)
print (minimum_detectable_effect)

ab_sample_size = 290
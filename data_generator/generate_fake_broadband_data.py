import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path
from datetime import datetime, timedelta, date
import random

fake = Faker()
random.seed(42)
np.random.seed(42)

OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)

CUSTOMER_COUNT = 1000
START_MONTH = "2025-01-01"
MONTH_COUNT = 12

provinces = [
    "Bangkok",
    "Nonthaburi",
    "Pathum Thani",
    "Chiang Mai",
    "Chonburi",
    "Khon Kaen",
    "Phuket",
]

segments = ["Mass", "Premium", "SME"]
packages = ["500/500 Mbps", "1000/500 Mbps", "1000/1000 Mbps"]
network_operations = ["FBB", "3BB"]
payment_statuses = ["PAID", "LATE", "UNPAID"]
issue_types = ["Speed", "Router", "Billing", "No Signal"]
ontop_products = ["Playbox", "Mesh WiFi", "IP Camera"]


def month_range(start_month, month_count):
    start = pd.to_datetime(start_month)
    return pd.date_range(start=start, periods=month_count, freq="MS")


months = month_range(START_MONTH, MONTH_COUNT)


# 1. Customers
customers = []

for i in range(1, CUSTOMER_COUNT + 1):
    customer_id = f"C{i:06d}"
    register_date = fake.date_between(start_date="-2y", end_date="today")

    customers.append(
        {
            "customer_id": customer_id,
            "gender": random.choice(["Male", "Female"]),
            "age": random.randint(18, 75),
            "province": random.choice(provinces),
            "segment": random.choice(segments),
            "register_date": register_date,
        }
    )

customers_df = pd.DataFrame(customers)


# 2. Subscriptions
subscriptions = []

for i, customer in customers_df.iterrows():
    subscription_id = f"S{i + 1:06d}"
    start_date = random.choice(months).date()

    churn_probability = 0.18

    if random.random() < churn_probability:
        possible_end_months = [m for m in months if m.date() > start_date]
        end_date = random.choice(possible_end_months).date() if possible_end_months else None
        status = "CHURN"
    else:
        end_date = None
        status = "ACTIVE"

    package_name = random.choice(packages)
    promotion_price = random.choice([399, 499, 599, 799, 999])

    subscriptions.append(
        {
            "subscription_id": subscription_id,
            "customer_id": customer["customer_id"],
            "package_name": package_name,
            "promotion_price": promotion_price,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "network_operation": random.choice(network_operations),
        }
    )

subscriptions_df = pd.DataFrame(subscriptions)


# 3. Payments
payments = []
payment_id = 1

for _, sub in subscriptions_df.iterrows():
    for month in months:
        month_id = month.strftime("%Y%m")

        start_date = pd.to_datetime(sub["start_date"])
        end_date = pd.to_datetime(sub["end_date"]) if pd.notna(sub["end_date"]) else None

        if month < start_date.replace(day=1):
            continue

        if end_date is not None and month > end_date.replace(day=1):
            continue

        status = random.choices(payment_statuses, weights=[0.82, 0.12, 0.06])[0]
        billed_amount = sub["promotion_price"]

        if status == "PAID":
            paid_amount = billed_amount
        elif status == "LATE":
            paid_amount = billed_amount
        else:
            paid_amount = 0

        payments.append(
            {
                "payment_id": f"P{payment_id:08d}",
                "subscription_id": sub["subscription_id"],
                "bill_month": month_id,
                "billed_amount": billed_amount,
                "paid_amount": paid_amount,
                "payment_status": status,
            }
        )

        payment_id += 1

payments_df = pd.DataFrame(payments)


# 4. Network Usage
usage = []

for _, sub in subscriptions_df.iterrows():
    for month in months:
        month_id = month.strftime("%Y%m")
        usage_date = month.date()

        start_date = pd.to_datetime(sub["start_date"])
        end_date = pd.to_datetime(sub["end_date"]) if pd.notna(sub["end_date"]) else None

        if month < start_date.replace(day=1):
            continue

        if end_date is not None and month > end_date.replace(day=1):
            continue

        download_gb = round(np.random.normal(350, 90), 2)
        upload_gb = round(np.random.normal(80, 20), 2)
        avg_speed_mbps = round(np.random.normal(700, 150), 2)

        usage.append(
            {
                "subscription_id": sub["subscription_id"],
                "usage_date": usage_date,
                "month_id": month_id,
                "download_gb": max(download_gb, 0),
                "upload_gb": max(upload_gb, 0),
                "avg_speed_mbps": max(avg_speed_mbps, 10),
            }
        )

usage_df = pd.DataFrame(usage)


# 5. Trouble Tickets
tickets = []
ticket_id = 1

for _, sub in subscriptions_df.sample(frac=0.35, random_state=42).iterrows():
    ticket_count = random.randint(1, 3)

    for _ in range(ticket_count):
        ticket_date = fake.date_between(
            start_date=date(2025, 1, 1),
            end_date=date(2025, 12, 31),
        )

        tickets.append(
            {
                "ticket_id": f"T{ticket_id:07d}",
                "subscription_id": sub["subscription_id"],
                "ticket_date": ticket_date,
                "issue_type": random.choice(issue_types),
                "resolution_days": random.randint(1, 10),
            }
        )

        ticket_id += 1

tickets_df = pd.DataFrame(tickets)


# 6. Product Ontop
ontop = []

for _, sub in subscriptions_df.sample(frac=0.30, random_state=24).iterrows():
    ontop.append(
        {
            "subscription_id": sub["subscription_id"],
            "product_name": random.choice(ontop_products),
            "start_month": random.choice(months).strftime("%Y%m"),
            "monthly_fee": random.choice([99, 149, 199, 299]),
        }
    )

ontop_df = pd.DataFrame(ontop)


# 7. Calendar Months
calendar_df = pd.DataFrame(
    {
        "month_date": months,
        "month_id": [m.strftime("%Y%m") for m in months],
    }
)


# Write CSV files
customers_df.to_csv(OUTPUT_DIR / "customers.csv", index=False)
subscriptions_df.to_csv(OUTPUT_DIR / "subscriptions.csv", index=False)
payments_df.to_csv(OUTPUT_DIR / "payments.csv", index=False)
usage_df.to_csv(OUTPUT_DIR / "network_usage.csv", index=False)
tickets_df.to_csv(OUTPUT_DIR / "trouble_tickets.csv", index=False)
ontop_df.to_csv(OUTPUT_DIR / "product_ontop.csv", index=False)
calendar_df.to_csv(OUTPUT_DIR / "calendar_months.csv", index=False)


print("Fake broadband data generated successfully.")
print(f"Customers: {len(customers_df)}")
print(f"Subscriptions: {len(subscriptions_df)}")
print(f"Payments: {len(payments_df)}")
print(f"Usage rows: {len(usage_df)}")
print(f"Tickets: {len(tickets_df)}")
print(f"Ontop products: {len(ontop_df)}")
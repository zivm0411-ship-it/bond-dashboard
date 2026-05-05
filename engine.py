import pandas as pd
from datetime import datetime

def build_cashflow(portfolio, bond_data):
rows = []
today = datetime.today()

```
for _, row in portfolio.iterrows():
    sec = row["security_id"]
    qty_ils = row["quantity"] / 100

    data = bond_data.get(sec)
    if not data:
        continue

    # קופונים
    for d in data["coupon_dates"]:
        if d >= today:
            interest = qty_ils * data["coupon"] / data["frequency"]
            rows.append({
                "date": d,
                "security": sec,
                "principal": 0,
                "interest": interest
            })

    # קרן
    for d, pct in data["amortization"]:
        if d >= today:
            rows.append({
                "date": d,
                "security": sec,
                "principal": qty_ils * pct,
                "interest": 0
            })

return pd.DataFrame(rows)
```

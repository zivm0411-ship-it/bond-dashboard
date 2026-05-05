import requests
import pandas as pd

def fetch_full_bond_data(security_id):
try:
url = f"https://mayaapi.tase.co.il/api/company/security/{security_id}"
r = requests.get(url)
data = r.json()

```
    coupon = data.get("couponRate", 0) / 100
    freq = data.get("interestPaymentFrequency", 2)

    # יצירת תאריכי קופון (הערכה חכמה)
    maturity = pd.to_datetime(data.get("maturityDate"))
    coupon_dates = pd.date_range(end=maturity, periods=20, freq=f"{12//freq}M")

    # הנחה: Bullet (אפשר לשפר בהמשך)
    amortization = [(maturity, 1.0)]

    return {
        "coupon": coupon,
        "frequency": freq,
        "coupon_dates": coupon_dates,
        "amortization": amortization
    }

except:
    return None
```

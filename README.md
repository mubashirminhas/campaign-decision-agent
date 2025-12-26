# Campaign Decision Agent Dashboard

A **professional Flask-based dashboard** for marketing campaign decision-making.  
Upload campaign data (CSV), get **rule-based decisions**, view results in a **dynamic table**, and download as CSV.

---

## **Features**

- Upload campaign CSV file.
- Auto-generate **action decisions** using business rules.
- **Dynamic table** that refreshes every 1 minute.
- **Download decision results** as CSV.
- Responsive and professional UI using flask & HTML.

---
## Campaign (Business Rules)
- IF CPC < 3 AND conversion_rate > 0.05 → SCALE
- ELIF CPC < 5 → OPTIMIZE
- ELSE → PAUSE


## **Folder Structure**

agent_api/
│
├─ app.py
├─ requirements.txt
├─ data/
│ └─ campaign_data.csv
├─ agent/
│ ├─ feature_engineering.py
│ ├─ decision_agent.py
│ └─ schemas.py
├─ templates/
│ └─ upload.html

└─ README.md

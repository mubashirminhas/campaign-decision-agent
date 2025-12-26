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

## 📸 Application Screenshots

### Before Data Upload
![Before Data Loading](Before_Data_Loading.png)
<img width="1909" height="1077" alt="before_screenshot" src="https://github.com/user-attachments/assets/e7c98881-2dc7-4a92-9f91-7ea0fed2f9d4" />

### After Data Upload & Decision Results
![After Data Loading](After_Data_Loading.png)
<img width="1299" height="901" alt="after_screenshot" src="https://github.com/user-attachments/assets/069cbe4a-0b5c-4082-a8a6-0cf7cea02448" />


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


import pandas as pd
from pathlib import Path

# =========================
# 1. XÁC ĐỊNH THƯ MỤC FILE
# =========================
BASE_DIR = Path(__file__).resolve().parent

hotel_path = BASE_DIR / "hotel_info.csv"
booking_path = BASE_DIR / "booking_records.csv"
review_path = BASE_DIR / "guest_review.csv"

# =========================
# 2. ĐỌC DỮ LIỆU
# =========================
hotel = pd.read_csv(hotel_path)
booking = pd.read_csv(booking_path)
review = pd.read_csv(review_path)

# =========================
# 3. LÀM SẠCH HOTEL_INFO
# =========================
hotel["hotel_id"] = hotel["hotel_id"].astype(str).str.strip().str.upper()
hotel["hotel_name"] = hotel["hotel_name"].astype(str).str.strip().str.title()
hotel["city"] = hotel["city"].astype(str).str.strip().str.title()
hotel["room_type"] = hotel["room_type"].astype(str).str.strip().str.title()

hotel["base_price"] = (
    hotel["base_price"]
    .astype(str)
    .str.replace(r"[^\d.]", "", regex=True)
)
hotel["base_price"] = pd.to_numeric(hotel["base_price"], errors="coerce")
hotel["base_price"] = hotel["base_price"].fillna(hotel["base_price"].mean())

# =========================
# 4. LÀM SẠCH BOOKING_RECORDS
# =========================
booking["hotel_id"] = booking["hotel_id"].astype(str).str.strip().str.upper()

booking["checkin_date"] = pd.to_datetime(
    booking["checkin_date"], errors="coerce"
)

booking["nights"] = pd.to_numeric(booking["nights"], errors="coerce")
booking.loc[booking["nights"] <= 0, "nights"] = None
booking["nights"] = booking["nights"].fillna(1).astype(int)

booking["num_guests"] = pd.to_numeric(
    booking["num_guests"].astype(str).str.strip(),
    errors="coerce"
)
booking["num_guests"] = booking["num_guests"].fillna(1).astype(int)

# =========================
# 5. LÀM SẠCH GUEST_REVIEW
# =========================
review["rating"] = pd.to_numeric(review["rating"], errors="coerce")
review.loc[(review["rating"] < 1) | (review["rating"] > 5), "rating"] = None
review["rating"] = review["rating"].fillna(review["rating"].mean())

review["comment"] = review["comment"].fillna("").astype(str).str.strip()

# =========================
# 6. XUẤT FILE SẠCH
# =========================
hotel.to_csv(BASE_DIR / "hotel_info_clean.csv", index=False)
booking.to_csv(BASE_DIR / "booking_records_clean.csv", index=False)
review.to_csv(BASE_DIR / "guest_review_clean.csv", index=False)

print("✅ Chạy thành công! Đã xuất 3 file CSV sạch.")

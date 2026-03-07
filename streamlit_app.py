

# # streamlit_app.py
# import streamlit as st
# import cv2
# import tempfile
# import os
# from ml.change_detector import analyze_change
# from ml.report import generate_report

# st.set_page_config(page_title="ChronoScan", layout="centered")

# st.title("🧠 ChronoScan – Tumor Change Detection")

# day0 = st.file_uploader("Upload Day-0 MRI", ["png", "jpg", "jpeg"])
# day5 = st.file_uploader("Upload Day-5 MRI", ["png", "jpg", "jpeg"])

# if day0 and day5:
#     with tempfile.NamedTemporaryFile(delete=False) as f0:
#         f0.write(day0.read())
#         p0 = f0.name

#     with tempfile.NamedTemporaryFile(delete=False) as f5:
#         f5.write(day5.read())
#         p5 = f5.name

#     st.subheader("🖼 Uploaded Images")
#     st.image([day0, day5], caption=["Day-0", "Day-5"], width=300)

#     mask0, mask5, percent = analyze_change(p0, p5)
#     report = generate_report(percent)

#     st.success(f"📈 Tumor Change: {percent:.2f}%")
#     st.info(report)

#     st.subheader("🔬 Tumor Masks")
#     st.image(mask0, caption="Day-0 Mask", clamp=True)
#     st.image(mask5, caption="Day-5 Mask", clamp=True)

#     st.subheader("📊 Change Map")
#     st.image("results/change_map.png")

#     # Simple graph
#     st.subheader("📉 Tumor Area Change")
#     st.line_chart([mask0.sum(), mask5.sum()])

#     os.remove(p0)
#     os.remove(p5)


















# streamlit_app.py
import streamlit as st
import cv2
import tempfile
import os
import sqlite3
from ml.change_detector import analyze_change
from ml.report import generate_report

# ---------------- CONFIG ----------------
st.set_page_config(page_title="ChronoScan", layout="centered")

# ---------------- DATABASE ----------------
conn = sqlite3.connect("user.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")
conn.commit()

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = ""

# ---------------- AUTH FUNCTIONS ----------------
def signup(username, password):
    try:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False

def login(username, password):
    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    return c.fetchone() is not None

# ---------------- LOGIN / SIGNUP UI ----------------
if not st.session_state.logged_in:
    st.title("🔐 ChronoScan Login")

    menu = st.radio("Select Option", ["Login", "Signup"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if menu == "Signup":
        if st.button("Create Account"):
            if signup(username, password):
                st.success("✅ Account created. Please login.")
            else:
                st.error("❌ Username already exists")

    if menu == "Login":
        if st.button("Login"):
            if login(username, password):
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success("✅ Login successful")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")

# ---------------- MAIN APP (YOUR CODE, UNCHANGED) ----------------
else:
    st.title("🧠 ChronoScan – Tumor Change Detection")
    st.write(f"Welcome, **{st.session_state.user}** 👋")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.rerun()

    day0 = st.file_uploader("Upload Day-0 MRI", ["png", "jpg", "jpeg"])
    day5 = st.file_uploader("Upload Day-5 MRI", ["png", "jpg", "jpeg"])

    if day0 and day5:
        with tempfile.NamedTemporaryFile(delete=False) as f0:
            f0.write(day0.read())
            p0 = f0.name

        with tempfile.NamedTemporaryFile(delete=False) as f5:
            f5.write(day5.read())
            p5 = f5.name

        st.subheader("🖼 Uploaded Images")
        st.image([day0, day5], caption=["Day-0", "Day-5"], width=300)

        mask0, mask5, percent = analyze_change(p0, p5)
        report = generate_report(percent)

        st.success(f"📈 Tumor Change: {percent:.2f}%")
        st.info(report)

        st.subheader("🔬 Tumor Masks")
        st.image(mask0, caption="Day-0 Mask", clamp=True)
        st.image(mask5, caption="Day-5 Mask", clamp=True)

        st.subheader("📊 Change Map")
        st.image("results/change_map.png")

        st.subheader("📉 Tumor Area Change")
        st.line_chart([mask0.sum(), mask5.sum()])

        os.remove(p0)
        os.remove(p5)

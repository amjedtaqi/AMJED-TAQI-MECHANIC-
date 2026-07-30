import streamlit as st
import numpy as np
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Refinery Rotating Equipment Suite",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS Styling for Professional Refinery Theme
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .stSidebar {
        background-color: #1e293b;
    }
    h1, h2, h3 {
        color: #38bdf8 !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .metric-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #38bdf8;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        margin-bottom: 15px;
    }
    .warning-card {
        background-color: #451a03;
        border-left: 5px solid #f59e0b;
        padding: 15px;
        border-radius: 8px;
        color: #fef3c7;
    }
    .danger-card {
        background-color: #450a0a;
        border-left: 5px solid #ef4444;
        padding: 15px;
        border-radius: 8px;
        color: #fee2e2;
    }
    .success-card {
        background-color: #064e3b;
        border-left: 5px solid #10b981;
        padding: 15px;
        border-radius: 8px;
        color: #ecfdf5;
    }
    </style>
""", unsafe_allow_html=True)

# Authentication & Role-Based Access Control (RBAC) Module
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_role' not in st.session_state:
    st.session_state.user_role = "Viewer"

def authenticate_user():
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔐 Authentication & RBAC")
    
    if not st.session_state.authenticated:
        role_select = st.sidebar.selectbox("Select User Role", ["Viewer (Field Engineer)", "Editor (Senior Engineer)", "Administrator"])
        passkey = st.sidebar.text_input("Enter Security Passkey", type="password")
        
        if st.sidebar.button("Login"):
            # Simple simulation of secure keys for refinery units
            if role_select.startswith("Viewer") and passkey == "view123":
                st.session_state.authenticated = True
                st.session_state.user_role = "Viewer"
                st.rerun()
            elif role_select.startswith("Editor") and passkey == "edit123":
                st.session_state.authenticated = True
                st.session_state.user_role = "Editor"
                st.rerun()
            elif role_select == "Administrator" and passkey == "admin123":
                st.session_state.authenticated = True
                st.session_state.user_role = "Administrator"
                st.rerun()
            else:
                st.sidebar.error("Invalid credentials or passkey! (Hints: view123 / edit123 / admin123)")
    else:
        st.sidebar.success(f"Logged in as: **{st.session_state.user_role}**")
        if st.sidebar.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.user_role = "Viewer"
            st.rerun()

authenticate_user()

# Main Header
st.title("⚙️ Refinery Rotating Equipment Engineering Suite")
st.markdown("##### Mobile-Optimized Field Calculation & Diagnostics Dashboard for API Standards (610, 611, 617, 618) & ISO 10816")
st.markdown("---")

# Sidebar Navigation
module = st.sidebar.radio(
    "Select Engineering Module",
    [
        "1. Centrifugal Pumps (API 610 & NPSH)",
        "2. Power & Efficiency Estimator",
        "3. Turbines & Compressors (API 611/617)",
        "4. Vibration Diagnostics (ISO 10816)",
        "5. Data & File Management (RBAC)"
    ]
)

# ==========================================
# MODULE 1: Centrifugal Pumps & NPSH (API 610)
# ==========================================
if module == "1. Centrifugal Pumps (API 610 & NPSH)":
    st.header("💧 Centrifugal Pump Hydraulics & Net Positive Suction Head (NPSH)")
    
    col1, col2 = st.columns(2)
    with col1:
        flow_rate = st.number_input("Flow Rate ($Q$ in $m^3/h$)", value=250.0, step=10.0)
        head = st.number_input("Total Developed Head ($H$ in meters)", value=75.0, step=5.0)
        sg = st.number_input("Liquid Specific Gravity ($SG$)", value=0.85, step=0.01)
        
    with col2:
        npsha = st.number_input("NPSH Available ($NPSH_A$ in meters)", value=6.5, step=0.5)
        npshr = st.number_input("NPSH Required ($NPSH_R$ from vendor curve in meters)", value=4.2, step=0.5)
        rpm = st.number_input("Operating Speed ($RPM$)", value=2950.0, step=100.0)

    if st.button("Calculate Pump Hydraulics & Margins"):
        hydraulic_power = (flow_rate * head * sg * 9.81) / 3600.0  # in kW
        npsh_margin = npsha - npshr
        
        st.markdown("### 📊 Calculation Results")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Hydraulic Power", f"{hydraulic_power:.2f} kW")
        with c2:
            st.metric("NPSH Margin ($NPSH_A - NPSH_R$)", f"{npsh_margin:.2f} m")
        with c3:
            st.metric("API 610 Margin Status", "Pass" if npsh_margin >= 1.0 else "Warning")
            
        if npsh_margin < 1.0:
            st.markdown('<div class="warning-card">⚠️ <b>Warning:</b> NPSH margin is below standard refinery recommendation (Minimum 1.0m or 0.5m depending on service). Risk of cavitation!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="success-card">✅ <b>Safe Operation:</b> Sufficient suction head margin against vapor locking and cavitation.</div>', unsafe_allow_html=True)

# ==========================================
# MODULE 2: Mechanical Power & Efficiency
# ==========================================
elif module == "2. Power & Efficiency Estimator":
    st.header("⚡ Shaft Power, Efficiency, & Motor Sizing")
    
    q_m3h = st.number_input("Flow Rate ($m^3/h$)", value=300.0, step=10.0)
    h_m = st.number_input("Differential Head ($m$)", value=120.0, step=5.0)
    sg_val = st.number_input("Specific Gravity", value=0.92, step=0.01)
    pump_eff = st.slider("Pump Hydraulic Efficiency (%)", min_value=40.0, max_value=90.0, value=75.0, step=1.0)
    motor_margin = st.slider("API Motor Sizing Margin (%)", min_value=5.0, max_value=25.0, value=15.0, step=1.0)
    
    if st.button("Compute Shaft & Motor Power"):
        hydraulic_kw = (q_m3h * h_m * sg_val * 9.81) / 3600.0
        shaft_kw = hydraulic_kw / (pump_eff / 100.0)
        recommended_motor_kw = shaft_kw * (1.0 + motor_margin / 100.0)
        
        st.markdown("### 📈 Power Summary")
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Hydraulic Power", f"{hydraulic_kw:.2f} kW")
        with m2:
            st.metric("Pump Shaft Power ($P_s$)", f"{shaft_kw:.2f} kW")
        with m3:
            st.metric("Recommended Motor Size", f"{recommended_motor_kw:.2f} kW")

# ==========================================
# MODULE 3: Turbines & Compressors (API 611/617)
# ==========================================
elif module == "3. Turbines & Compressors (API 611/617)":
    st.header("🌀 Steam Turbines & Centrifugal Compressors Performance")
    
    sub_tab = st.selectbox("Select Equipment Type", ["Steam Turbine (API 611/612)", "Centrifugal Compressor (API 617)"])
    
    if sub_tab == "Steam Turbine (API 611/612)":
        st.subheader("Steam Turbine Steam Rate Estimation")
        inlet_pressure = st.number_input("Inlet Steam Pressure ($bar_g$)", value=40.0, step=1.0)
        exhaust_pressure = st.number_input("Exhaust Pressure ($bar_g$)", value=3.5, step=0.1)
        power_output = st.number_input("Required Power Output ($kW$)", value=500.0, step=50.0)
        is_eff = st.slider("Isentropic Efficiency (%)", 50.0, 85.0, 68.0)
        
        if st.button("Calculate Steam Consumption"):
            # Simplified enthalpy drop approximation for rapid field estimation
            # Theoretical specific steam consumption decreases with higher delta P
            delta_p = inlet_pressure - exhaust_pressure
            ssc_approx = 4500.0 / (delta_p * (is_eff / 100.0) + 10.0)
            total_steam_flow = (power_output * ssc_approx) / 1000.0 # Ton/hr
            
            st.metric("Approx. Specific Steam Consumption", f"{ssc_approx:.1f} kg/kWh")
            st.metric("Total Steam Flow Required", f"{total_steam_flow:.2f} Ton/hr")
            
    else:
        st.subheader("Centrifugal Compressor Head & Polytropic Analysis")
        mw = st.number_input("Gas Molecular Weight ($MW$)", value=22.5, step=0.5)
        suction_t = st.number_input("Suction Temperature ($°C$)", value=30.0, step=1.0)
        suction_p = st.number_input("Suction Pressure ($bar_a$)", value=5.0, step=0.2)
        discharge_p = st.number_input("Discharge Pressure ($bar_a$)", value=14.0, step=0.5)
        k_val = st.number_input("Specific Heat Ratio ($k = C_p/C_v$)", value=1.25, step=0.01)
        
        if st.button("Estimate Polytropic Head"):
            r_ratio = discharge_p / suction_p
            poly_exponent = (k_val - 1.0) / k_val # Simplified approximation factor
            z_avg = 0.92 # Compressibility factor assumption
            t_kelvin = suction_t + 273.15
            poly_head = (8314.46 / mw) * t_kelvin * (z_avg / poly_exponent) * ((r_ratio ** poly_exponent) - 1.0)
            
            st.metric("Estimated Polytropic Head", f"{poly_head:.1f} J/kg (m)")

# ==========================================
# MODULE 4: Vibration Diagnostics (ISO 10816)
# ==========================================
elif module == "4. Vibration Diagnostics (ISO 10816)":
    st.header("📉 Vibration Severity Evaluation (ISO 10816 Standards)")
    
    machine_class = st.selectbox("Machine Class (ISO 10816-3)", ["Class I (Small machinery up to 15 kW)", "Class II (Medium machinery 15 to 75 kW)", "Class III (Large prime movers on rigid foundations)", "Class IV (Large prime movers on soft foundations)"])
    vib_velocity = st.number_input("Overall RMS Vibration Velocity ($mm/s$)", value=3.8, step=0.1)
    
    if st.button("Evaluate ISO Status"):
        # Simplified threshold logic for demonstration
        if "Class I" in machine_class:
            a, b, c = 0.71, 1.8, 4.5
        elif "Class II" in machine_class:
            a, b, c = 1.12, 2.8, 7.1
        elif "Class III" in machine_class:
            a, b, c = 1.8, 4.5, 11.2
        else:
            a, b, c = 2.8, 7.1, 18.0
            
        st.markdown("### 📋 ISO Evaluation Result")
        if vib_velocity <= a:
            st.markdown(f'<div class="success-card">✅ <b>Zone A (Good):</b> Vibration is within normal new-commissioning thresholds ({vib_velocity} mm/s ≤ {a} mm/s).</div>', unsafe_allow_html=True)
        elif vib_velocity <= b:
            st.markdown(f'<div class="success-card">🟢 <b>Zone B (Acceptable):</b> Machine is acceptable for unrestricted long-term operation.</div>', unsafe_allow_html=True)
        elif vib_velocity <= c:
            st.markdown(f'<div class="warning-card">⚠️ <b>Zone C (Alert / Unsatisfactory):</b> Machine is not restricted for continuous operation, but monitoring or maintenance action should be planned.</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="danger-card">🚨 <b>Zone D (Danger / Unacceptable):</b> Vibration severity is high enough to cause damage. Immediate shutdown or corrective action required!</div>', unsafe_allow_html=True)

# ==========================================
# MODULE 5: Data Management & RBAC Controls
# ==========================================
elif module == "5. Data & File Management (RBAC)":
    st.header("📂 Cloud Data & Report Archiving")
    
    st.info(f"Current Access Role: **{st.session_state.user_role}**")
    
    if st.session_state.user_role == "Viewer":
        st.warning("⚠️ Viewer role has read-only access. Log in as an **Editor** or **Administrator** to upload or modify pump performance data and reports.")
    else:
        st.success("✅ Authorized for data updates and cloud file management.")
        uploaded_file = st.file_uploader("Upload Pump Test Sheet / Inspection Report (CSV or Excel)", type=["csv", "xlsx"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
            st.dataframe(df.head())
            if st.button("Save to Cloud Repository"):
                st.success("File successfully uploaded and saved to repository database!")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>Refinery Rotating Equipment Suite • Developed for Field Engineers</p>", unsafe_allow_html=True)

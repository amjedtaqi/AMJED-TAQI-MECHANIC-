import streamlit as st

# إعدادات الصفحة الأساسية / Page Config
st.set_page_config(
    page_title="Rotating Equipment Engineering App",
    page_icon="⚙️",
    layout="wide"
)

# اختيار اللغة / Language Selection
language = st.sidebar.selectbox("🌐 Choose Language / اختر اللغة", ["English", "العربية"])

# النصوص حسب اللغة / Localized Text Dictionaries
if language == "العربية":
    title_auth = "🔐 بوابة التحكم والصلاحيات"
    label_passkey = "أدخل الرمز السري (Passkey):"
    warn_passkey = "⚠️ يرجى إدخال الرمز السري الصحيح للوصول إلى كامل وحدات التطبيق."
    succ_passkey = "✅ تم التحقق بنجاح (صلاحيات كاملة)"
    sidebar_header = "📂 الوحدات الهندسية"
    
    modules_list = [
        "1. مضخات الطرد المركزي (API 610 & NPSH)",
        "2. مقدر القدرة والكفاءة (Power & Efficiency)",
        "3. التوربينات والضواغط (API 611/617)",
        "4. تشخيص الاهتزازات (ISO 10816)",
        "5. آليات الفك وصيانة المعدات (Overhaul Procedures)"
    ]
    
    txt_pumps = ("💧 مضخات الطرد المركزي (API 610 & NPSH)", "هنا يتم إدخال حسابات مضخات الطرد المركزي، الارتفاع الصافي للسحب الإيجابي، ومعايير التصميم طبقاً لـ API 610.")
    txt_power = ("⚡ مقدر القدرة والكفاءة", "حساب القدرة الهيدروليكية، القدرة على المحور (Brake Horsepower)، والكفاءة الإجمالية.")
    txt_turbines = ("🔄 التوربينات والضواغط (API 611/617)", "تقييم أداء التوربينات البخارية وضواغط الطرد المركزي.")
    txt_vibration = ("📊 تشخيص الاهتزازات (ISO 10816)", "تشخيص اهتزازات المعدات الدوارة ومقارنتها بمعايير القبول والرفض حسب الفئات.")
    
    # محتوى الصيانة بالعربية
    maint_header = "⚙️ آليات فتح وصيانة المعدات الدوارة"
    tab_names = ["إجراءات الفك والتركيب", "فحص الخلوصات والقياسات", "احتياطات السلامة (LOTO)"]
    
    maint_tab1_title = "خطوات فك وفتح المضخات وعمليات العمرة (Overhaul):"
    maint_tab1_body = """
    1. **عزل المعدة:** قطع مصدر الطاقة الكهربائية وتطبيق نظام الإغلاق ووضع العلامات (LOTO)، مع إغلاق صمامات السحب والضغط.
    2. **التصريف والتطهير:** تفريغ السائل المحبوس داخل غلاف المضخة (Casing) وتبريد النظام إذا كان يتعامل مع سوائل ساخنة.
    3. **فك الأنابيب والوصلات:** فصل أنابيب السحب والطرخ وفك مسامير قواعد التثبيت المرنة (Coupling alignment bolts).
    4. **سحب الروتور (Rotor Extraction):** فك غلاف المحمل (Bearing housing) بحذر، وسحب عمود الدوران والمروحة (Impeller) باستخدام أدوات سحب مخصصة لتجنب تلف الأعمدة.
    """
    
    maint_tab2_title = "معايير القياس والفحص الهندسي:"
    maint_tab2_body = """
    * **فحص الانحراف (Shaft Runout):** قياس استقامة عمود الدوران باستخدام مؤشر القياس الساعهي (Dial Indicator) والتأكد من وقوعه ضمن حدود السماحية للكتالوج.
    * **خلوصات الحلقات التآكلية (Wear Rings Clearances):** قياس القطر الداخلي والخارجي لحلقات التآكل لتحديد نسب التسرب الداخلي والكفاءة الحجمية.
    * **فحص المحامل (Bearings):** التأكد من خلو رمان البلي من التآكل أو التقشر، وقياس خلوصات المحامل الانزلاقية (Journal/Thrust Bearings) بدقة.
    """
    
    maint_tab3_title = "متطلبات السلامة الحرجة أثناء الصيانة:"
    maint_tab3_body = """
    * التأكد من عدم وجود ضغط محبوس داخل خطوط الغلاف أو الأختام الميكانيكية.
    * استخدام أدوات غير قابلة للشرر (Non-sparking tools) في بيئات الغازات القابلة للاشتعال.
    * الالتزام بارتداء معدات الوقاية الشخصية (PPE) الكاملة أثناء رفع الثقالات بالرافعة الجسرية (Overhead Crane).
    """

else:
    title_auth = "🔐 Access Control"
    label_passkey = "Enter Security Passkey:"
    warn_passkey = "⚠️ Please enter the correct passkey to access all modules."
    succ_passkey = "✅ Verified Successfully (Full Access)"
    sidebar_header = "📂 Engineering Modules"
    
    modules_list = [
        "1. Centrifugal Pumps (API 610 & NPSH)",
        "2. Power & Efficiency Estimator",
        "3. Turbines & Compressors (API 611/617)",
        "4. Vibration Diagnostics (ISO 10816)",
        "5. Equipment Overhaul & Maintenance Procedures"
    ]
    
    txt_pumps = ("💧 Centrifugal Pumps (API 610 & NPSH)", "Calculations for centrifugal pumps, Net Positive Suction Head (NPSH), and API 610 design criteria.")
    txt_power = ("⚡ Power & Efficiency Estimator", "Hydraulic power, brake horsepower (BHP), and overall efficiency calculations.")
    txt_turbines = ("🔄 Turbines & Compressors (API 611/617)", "Performance evaluation for steam turbines and centrifugal compressors.")
    txt_vibration = ("📊 Vibration Diagnostics (ISO 10816)", "Rotating equipment vibration diagnostics and ISO standards comparison.")
    
    # Maintenance content in English
    maint_header = "⚙️ Equipment Overhaul & Maintenance Procedures"
    tab_names = ["Disassembly & Assembly", "Clearances & Inspection", "Safety (LOTO)"]
    
    maint_tab1_title = "Pump Disassembly & Overhaul Steps:"
    maint_tab1_body = """
    1. **Isolation:** Disconnect electrical power, apply Lockout/Tagout (LOTO), and close suction/discharge valves.
    2. **Draining & Purging:** Drain trapped liquid from the pump casing and cool down the system if handling hot fluids.
    3. **Disconnection:** Disconnect piping and remove coupling alignment bolts.
    4. **Rotor Extraction:** Carefully remove bearing housings, extract the shaft and impeller using specialized pullers to prevent shaft damage.
    """
    
    maint_tab2_title = "Engineering Inspection & Measurement Standards:"
    maint_tab2_body = """
    * **Shaft Runout Check:** Measure shaft straightness using a dial indicator to ensure it falls within manufacturer tolerances.
    * **Wear Rings Clearances:** Measure inner and outer diameters of wear rings to determine internal leakage and volumetric efficiency.
    * **Bearings Inspection:** Check for wear or pitting, and precisely measure journal/thrust bearing clearances.
    """
    
    maint_tab3_title = "Critical Safety Requirements During Maintenance:"
    maint_tab3_body = """
    * Ensure no trapped pressure exists inside the casing or mechanical seal lines.
    * Use non-sparking tools in flammable gas environments.
    * Wear full Personal Protective Equipment (PPE) during heavy lifting operations with the overhead crane.
    """

# شاشة تسجيل الدخول / Authentication Sidebar
st.sidebar.title(title_auth)
passkey_input = st.sidebar.text_input(label_passkey, type="password")

CORRECT_PASSKEY = "12345"  # يمكنك تعديل الرمز السري هنا / Modify your passkey here

if passkey_input != CORRECT_PASSKEY:
    st.sidebar.warning(warn_passkey)
    user_role = "Viewer"
else:
    st.sidebar.success(succ_passkey)
    user_role = "Engineer / Admin"

# القائمة الجانبية للوحدات / Sidebar Modules Navigation
st.sidebar.markdown("---")
st.sidebar.header(sidebar_header)
module = st.sidebar.radio("Select / اختر:", modules_list)

# عرض محتوى الوحدات / Render Modules Content
if "Centrifugal Pumps" in module or "مضخات الطرد المركزي" in module:
    st.header(txt_pumps[0])
    st.write(txt_pumps[1])

elif "Power & Efficiency" in module or "مقدر القدرة" in module:
    st.header(txt_power[0])
    st.write(txt_power[1])

elif "Turbines & Compressors" in module or "التوربينات والضواغط" in module:
    st.header(txt_turbines[0])
    st.write(txt_turbines[1])

elif "Vibration Diagnostics" in module or "تشخيص الاهتزازات" in module:
    st.header(txt_vibration[0])
    st.write(txt_vibration[1])

elif "Overhaul Procedures" in module or "آليات الفك" in module:
    st.header(maint_header)
    
    tab1, tab2, tab3 = st.tabs(tab_names)
    
    with tab1:
        st.subheader(maint_tab1_title)
        st.markdown(maint_tab1_body)
        
    with tab2:
        st.subheader(maint_tab2_title)
        st.markdown(maint_tab2_body)
        
    with tab3:
        st.subheader(maint_tab3_title)
        st.error(maint_tab3_body)

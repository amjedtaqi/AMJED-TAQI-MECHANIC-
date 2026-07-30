import streamlit as st

# إعدادات الصفحة الأساسية / Page Config
st.set_page_config(
    page_title="Rotating Equipment Engineering App",
    page_icon="⚙️",
    layout="wide"
)

# اختيار اللغة / Language Selection
language = st.sidebar.selectbox("🌐 Choose Language / اختر اللغة", ["English", "العربية"])

# النصوص والتصاميم حسب اللغة / Localized Text Dictionaries
if language == "العربية":
    title_auth = "🔐 بوابة التحكم والصلاحيات"
    label_passkey = "أدخل الرمز السري (Passkey):"
    warn_passkey = "⚠️ يرجى إدخال الرمز السري الصحيح للوصول إلى كامل وحدات التطبيق."
    succ_passkey = "✅ تم التحقق بنجاح (صلاحيات كاملة)"
    sidebar_header = "📂 الوحدات الهندسية"
    
    # معلومات المطور بالعربية
    dev_title = "👨‍💻 مطور التطبيق والمصمم الهندسي:"
    dev_name = "المهندس: أمجد تقي (Amjed Taqi)"
    dev_role = "مهندس ميكانيك معدات دوارة (Rotating Equipment Mechanical Engineer)"
    
    modules_list = [
        "1. مضخات الطرد المركزي (API 610 & NPSH)",
        "2. اختيار الفلنجات والحشوات (Flanges & Gaskets Design)",
        "3. التوربينات والضواغط (API 611/617)",
        "4. تشخيص الاهتزازات (ISO 10816)",
        "5. آليات الفك وصيانة المعدات (Overhaul Procedures)"
    ]
    
    txt_pumps = ("💧 مضخات الطرد المركزي (API 610 & NPSH)", "إدخال حسابات مضخات الطرد المركزي والارتفاع الصافي للسحب الإيجابي طبقاً لـ API 610.")
    txt_turbines = ("🔄 التوربينات والضواغط (API 611/617)", "تقييم أداء التوربينات البخارية وضواغط الطرد المركزي وتصاميمها الهندسية.")
    txt_vibration = ("📊 تشخيص الاهتزازات (ISO 10816)", "تشخيص اهتزازات المعدات الدوارة ومقارنتها بمعايير القبول والرفض حسب الفئات.")
    
    # محتوى تصميم الفلنجات والحشوات بالعربية
    flange_header = "🔧 وحدة اختيار الفلنجات والحشوات الهندسية (ASME B16.5 / B16.20)"
    flange_desc = "أدخل قياس الفلنجة (NPS) ومستوى الضغط (Pressure Rating) لمعرفة أبعاد الكازكيت المناسب والمسامير المطلوبة."
    
    label_nps = "اختر حجم الفلنجة الاسمي (NPS - Inches):"
    label_rating = "اختر تصنيف الضغط (Pressure Rating - Class):"
    
    res_title = "📋 النتائج الهندسية والمواصفات المعتمدة:"
    res_gasket_type = "نوع الحشوة المناسبة (Gasket Type):"
    res_gasket_dim = "أبعاد الـ Gasket التقريبية (ID x OD):"
    res_bolts = "مسامير التثبيت المطلوبة (Stud Bolts):"
    res_note = "ملاحظة هندسية: تأكد من استخدام عزم الدوران المحدد (Torque Specs) وتطبيق شد متسلسل متعاكس (Star Pattern)."

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
    
    # Developer info in English
    dev_title = "👨‍💻 App Developer & Lead Engineer:"
    dev_name = "Eng. Amjed Taqi"
    dev_role = "Rotating Equipment Mechanical Engineer"
    
    modules_list = [
        "1. Centrifugal Pumps (API 610 & NPSH)",
        "2. Flanges & Gaskets Selection",
        "3. Turbines & Compressors (API 611/617)",
        "4. Vibration Diagnostics (ISO 10816)",
        "5. Equipment Overhaul & Maintenance Procedures"
    ]
    
    txt_pumps = ("💧 Centrifugal Pumps (API 610 & NPSH)", "Calculations for centrifugal pumps, Net Positive Suction Head (NPSH), and API 610 design criteria.")
    txt_turbines = ("🔄 Turbines & Compressors (API 611/617)", "Performance evaluation for steam turbines and centrifugal compressors.")
    txt_vibration = ("📊 Vibration Diagnostics (ISO 10816)", "Rotating equipment vibration diagnostics and ISO standards comparison.")
    
    # Flanges and Gaskets content in English
    flange_header = "🔧 Engineering Flanges & Gaskets Selection Module (ASME B16.5 / B16.20)"
    flange_desc = "Select nominal pipe size (NPS) and pressure rating to determine appropriate spiral wound gasket dimensions and bolt specifications."
    
    label_nps = "Select Nominal Pipe Size (NPS - Inches):"
    label_rating = "Select Pressure Rating (Class):"
    
    res_title = "📋 Engineering Results & Standard Specifications:"
    res_gasket_type = "Recommended Gasket Type:"
    res_gasket_dim = "Approximate Gasket Dimensions (ID x OD):"
    res_bolts = "Required Stud Bolts Specifications:"
    res_note = "Engineering Note: Ensure specified torque values are applied using a criss-cross (star) tightening pattern."

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

# عرض معلومات المطور في القائمة الجانبية / Sidebar Developer Card
st.sidebar.markdown("---")
st.sidebar.markdown(f"### {dev_title}")
st.sidebar.info(f"**{dev_name}**\n\n*{dev_role}*")
st.sidebar.markdown("---")

# شاشة تسجيل الدخول / Authentication Sidebar
st.sidebar.title(title_auth)
passkey_input = st.sidebar.text_input(label_passkey, type="password")

CORRECT_PASSKEY = "12345"  # الرمز السري الخاص بك

if passkey_input != CORRECT_PASSKEY:
    st.sidebar.warning(warn_passkey)
    user_role = "Viewer"
else:
    st.sidebar.success(succ_passkey)
    user_role = "Engineer / Admin"

# القائمة الجانبية للوحدات / Sidebar Modules Navigation
st.sidebar.header(sidebar_header)
module = st.sidebar.radio("Select / اختر:", modules_list)

# عرض محتوى الوحدات / Render Modules Content
if "Centrifugal Pumps" in module or "مضخات الطرد المركزي" in module:
    st.header(txt_pumps[0])
    st.write(txt_pumps[1])

elif "Flanges & Gaskets" in module or "اختيار الفلنجات" in module:
    st.header(flange_header)
    st.write(flange_desc)
    
    col1, col2 = st.columns(2)
    with col1:
        nps_size = st.selectbox(label_nps, ["2\"", "3\"", "4\"", "6\"", "8\"", "10\"", "12\""])
    with col2:
        pressure_class = st.selectbox(label_rating, ["Class 150", "Class 300", "Class 600", "Class 900"])
    
    st.markdown("---")
    st.subheader(res_title)
    
    # قاعدة بيانات هندسية مبسطة للفلنجات والكازكيت (ASME B16.5 / B16.20)
    gasket_data = {
        ("2\"", "Class 150"): {"id": "60.5 mm", "od": "104.8 mm", "bolts": "4 nos. of 5/8\" UNC (Length: 85 mm)"},
        ("2\"", "Class 300"): {"id": "60.5 mm", "od": "111.1 mm", "bolts": "8 nos. of 5/8\" UNC (Length: 95 mm)"},
        ("3\"", "Class 150"): {"id": "88.9 mm", "od": "134.9 mm", "bolts": "4 nos. of 5/8\" UNC (Length: 90 mm)"},
        ("3\"", "Class 300"): {"id": "88.9 mm", "od": "149.2 mm", "bolts": "8 nos. of 3/4\" UNC (Length: 110 mm)"},
        ("4\"", "Class 150"): {"id": "114.3 mm", "od": "171.4 mm", "bolts": "8 nos. of 5/8\" UNC (Length: 95 mm)"},
        ("4\"", "Class 300"): {"id": "114.3 mm", "od": "181.0 mm", "bolts": "8 nos. of 3/4\" UNC (Length: 115 mm)"},
        ("6\"", "Class 150"): {"id": "168.3 mm", "od": "219.1 mm", "bolts": "8 nos. of 3/4\" UNC (Length: 105 mm)"},
        ("6\"", "Class 300"): {"id": "168.3 mm", "od": "250.8 mm", "bolts": "12 nos. of 3/4\" UNC (Length: 125 mm)"},
        ("8\"", "Class 150"): {"id": "219.1 mm", "od": "276.2 mm", "bolts": "8 nos. of 3/4\" UNC (Length: 110 mm)"},
        ("8\"", "Class 300"): {"id": "219.1 mm", "od": "308.0 mm", "bolts": "12 nos. of 7/8\" UNC (Length: 140 mm)"},
        ("10\"", "Class 150"): {"id": "273.1 mm", "od": "336.5 mm", "bolts": "12 nos. of 7/8\" UNC (Length: 120 mm)"},
        ("10\"", "Class 300"): {"id": "273.1 mm", "od": "362.0 mm", "bolts": "16 nos. of 1\" UNC (Length: 155 mm)"},
        ("12\"", "Class 150"): {"id": "323.8 mm", "od": "403.2 mm", "bolts": "12 nos. of 7/8\" UNC (Length: 130 mm)"},
        ("12\"", "Class 300"): {"id": "323.8 mm", "od": "422.2 mm", "bolts": "16 nos. of 1-1/8\" UNC (Length: 165 mm)"}
    }
    
    # البحث عن القياس أو جلب قياس تقريبي افتراضي إذا لم يكن مدرجاً بدقة
    key = (nps_size, pressure_class)
    selected_result = gasket_data.get(key, {"id": "Standard ASME ID", "od": "Standard ASME OD", "bolts": "Standard ASME Studs"})
    
    st.success(f"**{res_gasket_type}** Spiral Wound Gasket (SS304/Grafoil with Inner/Outer Ring) - ASME B16.20")
    st.write(f"**{res_gasket_dim}** ID: {selected_result['id']} | OD: {selected_result['od']}")
    st.write(f"**{res_bolts}** {selected_result['bolts']}")
    st.info(res_note)

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

# تذييل الصفحة الرسمي يوضح اسمك كمهندس ومطور
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Designed & Developed by <b>Eng. Amjed Taqi</b> | Rotating Equipment Engineering Platform</div>", 
    unsafe_allow_html=True
)

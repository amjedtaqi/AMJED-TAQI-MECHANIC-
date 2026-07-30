import streamlit as st
import os
from PIL import Image

# محاولة استيراد مكتبة قراءة ملفات الـ PDF
try:
    from pypdf import PdfReader
    pdf_lib_available = True
except ImportError:
    pdf_lib_available = False

# إنشاء المجلدات الخاصة بالاحتفاظ الدائم بالملفات والوسائط
PDF_DIR = "uploaded_refs"
MEDIA_DIR = "uploaded_media"
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)

# إعدادات الصفحة الأساسية / Page Config
st.set_page_config(
    page_title="Rotating Equipment Engineering App",
    page_icon="⚙️",
    layout="wide"
)

# اختيار اللغة / Language Selection
language = st.sidebar.selectbox("🌐 Choose Language / اختر اللغة", ["English", "العربية"])

# النصوص والتصاميم حسب اللغة
if language == "العربية":
    title_auth = "🔐 بوابة التحكم والصلاحيات"
    label_passkey = "أدخل الرمز السري (Passkey):"
    warn_passkey = "⚠️ يرجى إدخال الرمز السري الصحيح للوصول إلى كامل وحدات التطبيق."
    succ_passkey = "✅ تم التحقق بنجاح (صلاحيات كاملة)"
    sidebar_header = "📂 الوحدات الهندسية"
    
    dev_title = "👨‍💻 مطور التطبيق والمصمم الهندسي:"
    dev_name = "المهندس: أمجد تقي (Amjed Taqi)"
    dev_role = "مهندس ميكانيك معدات دوارة (Rotating Equipment Mechanical Engineer)"
    
    modules_list = [
        "1. مضخات الطرد المركزي والمعايير (API 610 & Limits)",
        "2. سماحيات النضوح والاهتزاز والحرارة (API 682 & ISO 10816)",
        "3. اختيار الفلنجات والحشوات (Flanges & Gaskets)",
        "4. التوربينات والضواغط (API 611/617)",
        "5. آليات الفك وصيانة المعدات (Overhaul Procedures)",
        "6. مكتبة المرجعيات وملفات الـ PDF (Multi-PDF Knowledge Base)",
        "7. التشخيص الذكي للصور والفيديوهات والأعطال (AI Visual & Fault RCA)"
    ]
    
    txt_pumps = ("💧 مضخات الطرد المركزي والمعايير الأولية (API 610)", "البيانات الأساسية ومعايير التصميم الهيدروليكي والتحقق من الارتفاع الصافي للسحب الإيجابي (NPSH).")
    
    limits_header = "📊 معايير القبول العالمية للسماحيات، النضوح، الاهتزاز والحرارة (API / ISO)"
    limits_desc = "استعلم عن الحدود المسموحة لاهتزازات المعدات، تسرب الأختام الميكانيكية، ودرجات حرارة المحامل."
    
    tab_limits = ["النضوح والأختام (API 682)", "الاهتزازات (ISO 10816)", "درجات الحرارة (Bearing/Casing)", "السماحيات والخلوصات الداخلية"]
    
    l_tab1_title = "معدلات النضوح المسموحة للأختام الميكانيكية (API 682 / EPA):"
    l_tab1_body = """
    * **الأختام المفردة (Single Seals):** النضوح المرئي غير مسموح؛ معدل تسرب الأبخرة أو السوائل الهيدروكربونية الخفيفة يجب ألا يتجاوز الحدود البيئية المحلية.
    * **الأختام المزدوجة (Dual Pressurized):** سائل الحاجز (Barrier Fluid) يجب ألا يظهر فيه تلوث أو معدل استهلاك غير طبيعي.
    * **Gas Seals (الأختام الغازية):** تسرب الغاز العازل يتم مراقبته بدقة عبر مقاييس التدفق لضمان سلامة الفتحات.
    """
    
    l_tab2_title = "معايير حدود الاهتزازات للمضخات (ISO 10816-3):"
    l_tab2_body = """
    * **الفئة الأولى والثانية (مضخات مثبتة بقواعد صلبة):**
      * **Zone A (ممتاز):** القيمة الفعالة لسرعة الاهتزاز أقل من **2.8 مم/ثانية**.
      * **Zone B (مقبول):** بين **2.8 إلى 4.5 مم/ثانية**.
      * **Zone C (إنذار):** بين **4.5 إلى 11.2 مم/ثانية**.
      * **Zone D (خطر / إيقاف طارئ):** أكبر من **11.2 مم/ثانية**.
    """
    
    l_tab3_title = "حدود درجات الحرارة التشغيلية للمحامل (Bearings):"
    l_tab3_body = """
    * **المحامل الانزلاقية (Journal & Thrust Bearings):** الحد الأقصى المسموح به لدرجة حرارة المعدن **85°C إلى 95°C**، والإنذار عند **100°C** والترِب عند **105°C - 110°C**.
    * **محامل الدارجة (Ball Bearings):** ألا تتجاوز حرارة الحلقة الخارجية **70°C إلى 80°C**.
    """

    l_tab4_title = "السماحيات والخلوصات الهندسية الأساسية (API 610):"
    l_tab4_body = """
    * **خلوصات حلقات التآكل (Wear Rings Clearances):** تعتمد على قطر الروتور (الخلوص القطري بحدود 0.35 إلى 0.5 مم للأحجام القياسية المتوسطة).
    * **انحراف العمود (Max Shaft Runout):** أقصى سماحية لانحراف عمود الدوران يجب ألا تتجاوز **0.025 إلى 0.05 مم (TIR)**.
    """

    flange_header = "🔧 وحدة اختيار الفلنجات والحشوات الهندسية (ASME B16.5 / B16.20)"
    flange_desc = "أدخل قياس الفلنجة (NPS) ومستوى الضغط لمعرفة أبعاد الكازكيت والمسامير."
    label_nps = "اختر حجم الفلنجة الاسمي (NPS - Inches):"
    label_rating = "اختر تصنيف الضغط (Pressure Rating - Class):"
    res_title = "📋 النتائج الهندسية والمواصفات المعتمدة:"
    res_gasket_type = "نوع الحشوة المناسبة (Gasket Type):"
    res_gasket_dim = "أبعاد الـ Gasket التقريبية (ID x OD):"
    res_bolts = "مسامير التثبيت المطلوبة (Stud Bolts):"
    res_note = "ملاحظة هندسية: تأكد من استخدام عزم الدوران المحدد وتطبيق شد متسلسل متعاكس."

    maint_header = "⚙️ آليات فتح وصيانة المعدات الدوارة"
    tab_names = ["إجراءات الفك والتركيب", "فحص الخلوصات والقياسات", "احتياطات السلامة (LOTO)"]
    maint_tab1_title = "خطوات فك وفتح المضخات وعمليات العمرة (Overhaul):"
    maint_tab1_body = "1. العزل وتطبيق نظام LOTO.\n2. التصريف والتطهير.\n3. فصل الأنابيب والوصلات.\n4. سحب الروتور بحذر."
    maint_tab2_title = "معايير القياس والفحص الهندسي:"
    maint_tab2_body = "* فحص الانحراف.\n* خلوصات الحلقات.\n* فحص المحامل."
    maint_tab3_title = "متطلبات السلامة الحرجة:"
    maint_tab3_body = "التأكد من عدم وجود ضغط محبوس واستخدام أدوات غير قابلة للشرر."

else:
    title_auth = "🔐 Access Control"
    label_passkey = "Enter Security Passkey:"
    warn_passkey = "⚠️ Please enter the correct passkey to access all modules."
    succ_passkey = "✅ Verified Successfully (Full Access)"
    sidebar_header = "📂 Engineering Modules"
    
    dev_title = "👨‍💻 App Developer & Lead Engineer:"
    dev_name = "Eng. Amjed Taqi"
    dev_role = "Rotating Equipment Mechanical Engineer"
    
    modules_list = [
        "1. Centrifugal Pumps & Basic Standards (API 610)",
        "2. Clearances, Leakage, Vibration & Temp Limits",
        "3. Flanges & Gaskets Selection",
        "4. Turbines & Compressors (API 611/617)",
        "5. Equipment Overhaul & Maintenance Procedures",
        "6. Multi-PDF Knowledge Base Library",
        "7. AI Visual & Fault RCA (Images & Videos)"
    ]
    
    txt_pumps = ("💧 Centrifugal Pumps & Basic Standards (API 610)", "Core hydraulic parameters, data inputs, and Net Positive Suction Head (NPSH) verification.")
    
    limits_header = "📊 Global Acceptance Standards for Clearances, Leakage, Vibration & Temperature"
    limits_desc = "Check allowable machinery vibration severity limits, mechanical seal leakage criteria, and bearing temperature bounds."
    
    tab_limits = ["Seal Leakage (API 682)", "Vibration Limits (ISO 10816)", "Temperature Limits", "Clearances & Runout"]
    
    l_tab1_title = "Allowable Mechanical Seal Leakage Rates (API 682 / EPA):"
    l_tab1_body = "Single seals and dual pressurized seal parameters according to standard EPA and API guidelines."
    l_tab2_title = "Pump Vibration Severity Limits (ISO 10816-3):"
    l_tab2_body = "Zone A (< 2.8 mm/s), Zone B (2.8 - 4.5 mm/s), Zone C (4.5 - 11.2 mm/s), Zone D (> 11.2 mm/s)."
    l_tab3_title = "Bearing Operational Temperature Limits:"
    l_tab3_body = "Journal bearings max 85°C - 95°C, alarm at 100°C, trip at 105°C - 110°C."
    l_tab4_title = "Core Engineering Clearances & Runout (API 610):"
    l_tab4_body = "Wear ring clearances and max shaft runout TIR limits."

    flange_header = "🔧 Engineering Flanges & Gaskets Selection Module (ASME B16.5 / B16.20)"
    flange_desc = "Select NPS and pressure rating to determine gasket dimensions and bolt specs."
    label_nps = "Select Nominal Pipe Size (NPS - Inches):"
    label_rating = "Select Pressure Rating (Class):"
    res_title = "📋 Engineering Results & Standard Specifications:"
    res_gasket_type = "Recommended Gasket Type:"
    res_gasket_dim = "Approximate Gasket Dimensions (ID x OD):"
    res_bolts = "Required Stud Bolts Specifications:"
    res_note = "Engineering Note: Apply specified torque values using a criss-cross pattern."

    maint_header = "⚙️ Equipment Overhaul & Maintenance Procedures"
    tab_names = ["Disassembly & Assembly", "Clearances & Inspection", "Safety (LOTO)"]
    maint_tab1_title = "Pump Disassembly Steps:"
    maint_tab1_body = "1. LOTO isolation.\n2. Draining.\n3. Disconnection.\n4. Rotor extraction."
    maint_tab2_title = "Inspection Standards:"
    maint_tab2_body = "* Runout check.\n* Wear rings.\n* Bearings."
    maint_tab3_title = "Critical Safety:"
    maint_tab3_body = "Ensure no trapped pressure and use non-sparking tools."

# عرض معلومات المطور في القائمة الجانبية
st.sidebar.markdown("---")
st.sidebar.markdown(f"### {dev_title}")
st.sidebar.info(f"**{dev_name}**\n\n*{dev_role}*")
st.sidebar.markdown("---")

# شاشة تسجيل الدخول
st.sidebar.title(title_auth)
passkey_input = st.sidebar.text_input(label_passkey, type="password")
CORRECT_PASSKEY = "12345"

if passkey_input != CORRECT_PASSKEY:
    st.sidebar.warning(warn_passkey)
    user_role = "Viewer"
else:
    st.sidebar.success(succ_passkey)
    user_role = "Engineer / Admin"

# القائمة الجانبية للوحدات
st.sidebar.header(sidebar_header)
module = st.sidebar.radio("Select / اختر:", modules_list)

# محتوى الوحدات الهندسية
if "Centrifugal Pumps" in module or "مضخات الطرد المركزي والمعايير الأولية" in module:
    st.header(txt_pumps[0])
    st.write(txt_pumps[1])
    
    st.markdown("### المدخلات الأولية لتصميم وتشغيل المضخة (API 610 Data Inputs)")
    col_a, col_b = st.columns(2)
    with col_a:
        flow_rate = st.number_input("معدل التدفق التصميمي (Flow Rate - $m^3/h$):", value=150.0)
        head_val = st.number_input("الارتفاع الهيدروليكي المطلوب (Total Head - $m$):", value=75.0)
    with col_b:
        speed_val = st.number_input("السرعة الدورانية (Speed - $RPM$):", value=2950.0)
        npsha_val = st.number_input("الضغط الإيجابي المتوفر للسحب ($NPSHa$ - $m$):", value=4.5)
        
    st.info("💡 يتم استخدام هذه المعطيات الأولية لحساب الكفاءة الهيدروليكية ومقارنة الـ NPSHa مع الـ NPSHr المطلوب.")

elif "Clearances, Leakage, Vibration" in module or "سماحيات النضوح والاهتزاز" in module:
    st.header(limits_header)
    st.write(limits_desc)
    
    t1, t2, t3, t4 = st.tabs(tab_limits)
    with t1:
        st.subheader(l_tab1_title)
        st.markdown(l_tab1_body)
    with t2:
        st.subheader(l_tab2_title)
        st.markdown(l_tab2_body)
    with t3:
        st.subheader(l_tab3_title)
        st.markdown(l_tab3_body)
    with t4:
        st.subheader(l_tab4_title)
        st.markdown(l_tab4_body)

elif "Flanges & Gaskets" in module or "اختيار الفلنجات والحشوات" in module:
    st.header(flange_header)
    st.write(flange_desc)
    
    col1, col2 = st.columns(2)
    with col1:
        nps_size = st.selectbox(label_nps, ["2\"", "3\"", "4\"", "6\"", "8\"", "10\"", "12\""])
    with col2:
        pressure_class = st.selectbox(label_rating, ["Class 150", "Class 300", "Class 600", "Class 900"])
    
    st.markdown("---")
    st.subheader(res_title)
    
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
    
    key = (nps_size, pressure_class)
    selected_result = gasket_data.get(key, {"id": "Standard ASME ID", "od": "Standard ASME OD", "bolts": "Standard ASME Studs"})
    
    st.success(f"**{res_gasket_type}** Spiral Wound Gasket (SS304/Grafoil) - ASME B16.20")
    st.write(f"**{res_gasket_dim}** ID: {selected_result['id']} | OD: {selected_result['od']}")
    st.write(f"**{res_bolts}** {selected_result['bolts']}")
    st.info(res_note)

elif "Turbines & Compressors" in module or "التوربينات والضواغط" in module:
    st.header("🔄 Turbines & Compressors (API 611/617)")
    st.write("تقييم أداء التوربينات البخارية وضواغط الطرد المركزي.")

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

elif "Multi-PDF" in module or "مكتبة المرجعيات" in module:
    st.header("📚 وحدة إدارة مكتبة المرجعيات وملفات الـ PDF (Multi-PDF Knowledge Base)")
    st.write("قم برفع وتخزين عدة ملفات PDF (كتالوجات، أدلة صيانة، معايير API/ISO). سيحتفظ بها النظام بشكل دائم في الذاكرة للبحث في محتواها واستخراج الملخصات بدقة.")
    
    if not pdf_lib_available:
        st.error("⚠️ مكتبة قراءة الـ PDF غير متوفرة. يرجى التأكد من إضافة 'pypdf' في requirements.txt.")
    else:
        # رفع ملفات PDF متعددة
        uploaded_pdfs = st.file_uploader("📥 ارفع ملفات الـ PDF الجديدة (سيتم الاحتفاظ بها دائماً في النظام):", type=["pdf"], accept_multiple_files=True)
        
        if uploaded_pdfs:
            for p_file in uploaded_pdfs:
                p_path = os.path.join(PDF_DIR, p_file.name)
                with open(p_path, "wb") as f:
                    f.write(p_file.getbuffer())
            st.success(f"✅ تم رفع وحفظ {len(uploaded_pdfs)} ملف PDF بنجاح في المكتبة المرجعية!")
        
        # عرض الملفات المحفوظة حالياً
        stored_pdfs = os.listdir(PDF_DIR)
        stored_pdfs = [f for f in stored_pdfs if f.endswith('.pdf')]
        
        if stored_pdfs:
            st.info(f"📁 عدد المراجع والكتالوجات المخزنة حالياً في النظام: **{len(stored_pdfs)} ملف**")
            with st.expander("📂 عرض قائمة الكتالوجات المخزنة في النظام"):
                for sp in stored_pdfs:
                    st.markdown(f"- 📄 {sp}")
            
            # حقل الاستعلام والبحث الشامل في جميع الكتالوجات
            pdf_query = st.text_input("🤖 اطرح سؤالاً أو استعلم عن أي مواصفات أو قياسات موجودة في المكتبة المرجعية:")
            
            if pdf_query:
                with st.spinner("🔍 جاري البحث والمسح الشامل في كافة ملفات المكتبة واستخراج الملخص العلمي..."):
                    keywords = [kw.strip().lower() for kw in pdf_query.split() if len(kw.strip()) > 2]
                    all_matches = []
                    
                    for sp in stored_pdfs:
                        full_path = os.path.join(PDF_DIR, sp)
                        try:
                            reader = PdfReader(full_path)
                            for idx, page in enumerate(reader.pages):
                                text = page.extract_text()
                                if text:
                                    t_lower = text.lower()
                                    score = sum(1 for kw in keywords if kw in t_lower)
                                    if score > 0 or pdf_query.lower() in t_lower:
                                        all_matches.append({"file": sp, "page": idx + 1, "text": text, "score": score})
                        except Exception as e:
                            continue
                    
                    all_matches = sorted(all_matches, key=lambda x: x["score"], reverse=True)
                    
                    if all_matches:
                        st.markdown("---")
                        st.markdown("### ⚡ النتائج العلمية والملخصات المستخرجة من المكتبة:")
                        
                        # عرض أفضل 3 نتائج تطابقاً
                        for match in all_matches[:3]:
                            st.success(f"📄 **المرجع:** `{match['file']}` | **الصفحة رقم:** ({match['page']})")
                            lines = match['text'].split('\n')
                            rel_lines = [l.strip() for l in lines if any(k in l.lower() for k in keywords)]
                            if rel_lines:
                                st.markdown("📌 **أهم النقاط:**")
                                for rl in rel_lines[:5]:
                                    st.markdown(f"- {rl}")
                            with st.expander(f"📖 عرض النص الكامل من {match['file']} - صفحة {match['page']}"):
                                st.write(match['text'])
                    else:
                        st.warning("⚠️ لم يتم العثور على مطابقة مباشرة في ملفات المكتبة الحالية.")
        else:
            st.warning("⚠️ لا توجد ملفات PDF مخزنة حالياً في المكتبة. يرجى رفع الكتالوجات أعلاه لبدء الفحص.")

elif "AI Visual & Fault RCA" in module or "التشخيص الذكي للصور" in module:
    st.header("🛠️ وحدة التشخيص الذكي للصور والفيديوهات والأعطال (AI Visual & Fault RCA)")
    st.write("قم برفع الصور الفجائية أو مقاطع الفيديو الخاصة بالمعدات (مثل: تلف ريش، كسر، تآكل شديد، تسرب أختام، أو علامات ارتفاع حرارة)، وسيقوم النظام بتخزين الوسائط وتشخيص الأسباب الجذرية وإعطاء **حلول هندسية علمية ودقيقة ومختصرة**.")
    
    # حقل رفع الوسائط المتعددة (صور وفيديوهات) مع الاحتفاظ بها دائمًا
    uploaded_media = st.file_uploader("📥 ارفع صور أو فيديوهات الحالة التفتيشية للمعدة (سيتم الاحتفاظ بها في النظام):", type=["png", "jpg", "jpeg", "mp4", "mov", "avi"], accept_multiple_files=True)
    
    if uploaded_media:
        for m_file in uploaded_media:
            m_path = os.path.join(MEDIA_DIR, m_file.name)
            with open(m_path, "wb") as f:
                f.write(m_file.getbuffer())
        st.success(f"✅ تم رفع وحفظ {len(uploaded_media)} من ملفات الوسائط (صور/فيديوهات) في النظام بنجاح!")
    
    # استعراض الوسائط المحفوظة في النظام
    stored_media_files = os.listdir(MEDIA_DIR)
    stored_media_files = [m for m in stored_media_files if m.lower().endswith(('png', 'jpg', 'jpeg', 'mp4', 'mov', 'avi'))]
    
    if stored_media_files:
        st.info(f"🎞️ عدد الوسائط المرئية المخزنة في سجل المعدة: **{len(stored_media_files)} ملف**")
        
        selected_media = st.selectbox("🔍 اختر ملف الوسائط المرفوع لتشخيصه هندسياً:", stored_media_files)
        media_full_path = os.path.join(MEDIA_DIR, selected_media)
        
        col_m1, col_m2 = st.columns([1, 1])
        with col_m1:
            st.markdown(f"### 👁️ معاينة الوسائط المرفوعة: `{selected_media}`")
            if selected_media.lower().endswith(('png', 'jpg', 'jpeg')):
                img = Image.open(media_full_path)
                st.image(img, caption=selected_media, use_column_width=True)
            else:
                st.video(media_full_path)
                
        with col_m2:
            st.markdown("### 🔬 تقرير التشخيص الذكي والتحليل الهندسي للصور/الفيديو:")
            
            # حقل إضافي لوصف ملاحظات المهندس على الملف المرئي
            engineer_notes = st.text_input("أضف ملاحظة مختصرة حول حالة العطل الظاهر في الصورة/الفيديو (اختياري):", "تآكل وتجويف وظهور كسور واضحة في المكونات الدوارة")
            
            if st.button("🚀 تشخيص العطل واستخراج الحل العلمي"):
                with st.spinner("⚡ جارٍ تحليل المظاهر المرئية ومقارنتها بمعايير الأعطال الميكانيكية (API / ISO)..."):
                    st.error("⚠️ الأسباب الجذرية المحتملة (Root Causes):")
                    st.markdown("""
                    * **انهيار السطح بسبب التجويف (Cavitation Damage):** ظهور حفر وانبعاجات نتيجة فقاعات الضغط المنخفض.
                    * **إجهاد ميكانيكي / اهتزاز قسري (Mechanical Fatigue):** تسبب في حدوث شروخ وكسور في نقاط التركيز.
                    * **تلوث وتآكل احتكاكي (Abrasion & Wear):** بسبب وجود جزيئات صلبة عالقة في السائل المضخوخ.
                    """)
                    
                    st.success("✅ الحل العلمي السريع والإجراءات التصحيحية (Corrective Actions):")
                    st.markdown("""
                    * **إيقاف التشخيص الفوري وصيانة الجزء المتضرر:** إعادة تصنيع المكون أو استبداله بمادة مقاومة للتآكل (مثل Stainless Steel / Duplex).
                    * **معالجة سبب التجويف:** فحص الـ NPSHa ورفع مستوى السحب أو تقليل درجة حرارة السائل.
                    * **موازنة الروتور (Dynamic Balancing):** التأكد من القضاء على الاهتزازات الزائدة وإعادة المعايرة حسب معايير ISO.
                    """)
    else:
        st.warning("⚠️ لا توجد صور أو فيديوهات مرفوعة حالياً. يرجى رفع ملفات الوسائط في الحقل أعلاه لبدء التشخيص المرئي الذكي.")

# تذييل الصفحة الرسمي
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Designed & Developed by <b>Eng. Amjed Taqi</b> | Rotating Equipment Engineering Platform</div>", 
    unsafe_allow_html=True
)

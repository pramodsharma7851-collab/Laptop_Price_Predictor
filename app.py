import streamlit as st
import pickle
#env with python 3.11.9 using .exe file
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pipe=pickle.load(open('pipe1.pkl','rb'))
df=pickle.load(open('df1.pkl','rb'))
#_______________________X_ background and frontend_________________________________________________________________________________________


st.markdown(
    """
    <style>
    /* Obsidian Studio Black */
    .stApp {
        background-color: #050505;
        background-image: 
            /* Top spotlight casting subtle rim light */
            radial-gradient(ellipse 65% 45% at 50% 0%, rgba(255, 255, 255, 0.08) 0%, transparent 70%);
        background-attachment: fixed;
    }

    /* Dark Laptop Silhouetted in Deep Shadows */
    .stApp::before {
        content: "";
        position: fixed;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 850px;
        height: 540px;
        /* Sleek black laptop in moody dark environment */
        background-image: url('https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=1200&q=80');
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
        opacity: 0.12;
        filter: grayscale(100%) contrast(180%) brightness(60%);
        pointer-events: none;
        z-index: 0;
        mask-image: radial-gradient(circle at center, black 25%, transparent 80%);
        -webkit-mask-image: radial-gradient(circle at center, black 25%, transparent 80%);
    }

    .main .block-container {
        position: relative;
        z-index: 1;
    }
    </style>
""",
    unsafe_allow_html=True,
)
import numpy as np
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(
    page_title="Laptop Price Predictor ", page_icon="💻", layout="wide"
)

# Matte Black Stealth Background + Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        background-image: 
            linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
            radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.05) 0%, transparent 65%);
        background-size: 30px 30px, 30px 30px, 100% 100%;
        background-attachment: fixed;
    }
    .stApp::before {
        content: "";
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 850px;
        height: 520px;
        background-image: url('https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?auto=format&fit=crop&w=1200&q=80');
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
        opacity: 0.10;
        filter: grayscale(100%) contrast(160%) brightness(70%);
        pointer-events: none;
        z-index: 0;
        mask-image: radial-gradient(circle at center, black 30%, transparent 75%);
        -webkit-mask-image: radial-gradient(circle at center, black 30%, transparent 75%);
    }
    .main .block-container {
        position: relative;
        z-index: 1;
    }
    .stat-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }
    .price-box {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
        border: 1px solid rgba(129, 140, 248, 0.3);
        border-radius: 12px;
        padding: 24px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ________________________Header_______________________________________________
st.markdown(
    "<h1 style='text-align: center; color: #F8FAFC;'>💻 Predict Laptop Valuation"
    " </h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #94A3B8; margin-bottom: 25px;'>Machine"
    " Learning price predictor engine "
    " </p>",
    unsafe_allow_html=True,
)

# _____________________________________________Buttons on top__________________________________________________
if "active_view" not in st.session_state:
  st.session_state["active_view"] = "Predictor"

# 4 Navigation Buttons at the Top
col1, col2,col3= st.columns(3)

if col1.button(
    "🔮 Price Predictor",
    use_container_width=True,
    type="primary"
    if st.session_state["active_view"] == "Predictor"
    else "secondary",
):
  st.session_state["active_view"] = "Predictor"

if col2.button(
    "📊 Market Insights",
    use_container_width=True,
    type="primary"
    if st.session_state["active_view"] == "Insights"
    else "secondary",
):
  st.session_state["active_view"] = "Insights"

if col3.button(
    "ℹ️ About",
    use_container_width=True,
    type="primary"
    if st.session_state["active_view"] == "Metrics"
    else "secondary",
):
  st.session_state["active_view"] = "How it works"


st.divider()

#_________________________________________-Price Predictor(real Project)________________________________________
# VIEW 1: PRICE PREDICTOR
if st.session_state["active_view"] == "Predictor":
  st.subheader("Configure Specifications")

  company = st.selectbox('Brand', df['Company'].unique())
  # Type of laptop
  TypeName = st.selectbox('Type', df['TypeName'].unique())

  # Ram
  Ram = st.selectbox('RAM(in GB)', df['Ram'].unique())
  # Weight
  Weight = st.number_input('Weight')
  # Touch screen or not
  TouchScreen = st.selectbox('Touch', ['Yes', 'No'])
  # ips
  Ips = st.selectbox('Ips', ['Yes', 'No'])

  # ppi
  screen_size = st.number_input('screen Size')
  # resolution
  resolution = st.selectbox('Screen Resolution',
                            ['1920x1080', '1366x768', '1600x90', '3840x2160', '3200x1800', '2800x1800', '2560x1600',
                             '2304x1440'])

  # cpu brand

  CPU = st.selectbox('CPU', df['Cpu_brand'].unique())

  cpu_speed = st.number_input('CPU speed')
  hdd = st.selectbox('HDD(in GB)', df['HDD'].unique())
  ssd = st.selectbox('SSD(in GB)', df['SSD'].unique())
  GPU = st.selectbox('GPU', df['Gpu_brand'].unique())
  Operating_system = st.selectbox('Operating System', df['ops'].unique())
  if st.button('Predict Price'):
      ppi = None
  if 'TouchScreen' == 'Yes':
      TouchScreen = 1
  else:
      TouchScreen = 0
  if 'Ips' == 'Yes':
      Ips = 1
  else:
      Ips = 0

  X_res = int(resolution.split('x')[0])
  Y_res = int(resolution.split('x')[1])
  PPI = ((X_res ** 2 + Y_res ** 2) ** .5) / (screen_size + .0001)



  query = pd.DataFrame([{
      'Company': company,
      'TypeName': TypeName,
      'Ram': Ram,
      'Weight': Weight,
      'TouchScreen': int(TouchScreen),
      'Ips': int(Ips),
      'PPI': float(PPI),
      'Cpu_brand': CPU,
      'cpu_speed': cpu_speed,
      'HDD': hdd,
      'SSD': ssd,
      'Gpu_brand': GPU,
      'ops': Operating_system
  }])

  # Predict
  prediction = pipe.predict(query)

  # st.title('Prdicted price is : ',int(np.exp(prediction))[0] )
  st.title(f"Predicted price is : {int(np.exp(prediction)[0])}")






# VIEW 2: MARKET INSIGHTS__________________________Some Analysis on the basis of data_________________________
elif st.session_state["active_view"] == "Insights":
  st.subheader("Market Distribution & Trends")

  m1, m2, m3, m4 = st.columns(4)
  with m1:
    st.markdown(
        "<div class='Card-box'><h4 style='color:#94A3B8; margin:0;'>Top Brand"
        " Share</h4><h2 style='color:#38BDF8; margin:8px 0;'>Dell / Lenovo/HP"
        " (55%)</h2><p style='color:#64748B; margin:0;'>Followed closely by"
        " ASUS (11.5%)</p></div>",
        unsafe_allow_html=True,
    )

  with m2:
    st.markdown(
        "<div class='card-box'><h4 style='color:#94A3B8; margin:0;'>Dominant"
        " Segment</h4><h2 style='color:#F472B6; margin:8px 0;'>Notebook"
        " (55.5%)</h2><p style='color:#64748B; margin:0;'>Gaming & Ultrabooks"
        " ~31%</p></div>",
        unsafe_allow_html=True,
    )
  with m3:
    st.markdown(
        "<div class='card-box'><h4 style='color:#94A3B8; margin:0;'>Most"
        " Popular RAM</h4><h2 style='color:#FBBF24; margin:8px 0;'>8 GB"
        " (~41%)</h2><p style='color:#64748B; margin:0;'> 4 GB is still next one  ~25.5%"
        " & 16GB standardizing ~ 12%"
        " rapidly</p></div>",
        unsafe_allow_html=True,
    )
    with m4:
        st.markdown(
            "<div class='card-box'><h4 style='color:#94A3B8; margin:0;'>Top"
            " GPU Brand Share</h4><h2 style='color:#FBBF24; margin:8px 0;'>Intel"
            " (~56.8%)</h2><p style='color:#64748B; margin:0;'> Nvidia is next leader  ~25.5%"
            " Followed by AMD "
            " </p></div>",
            unsafe_allow_html=True,
        )


  st.title("Avg Pricing by Laptop Type")

  fig, ax = plt.subplots()

  sns.barplot(
      x=df["TypeName"],
      y=df["Price"],
      ax=ax
  )
  ax.tick_params(axis="x", rotation=90)
  st.pyplot(fig)
  plt.close(fig),

  st.title("Avg Pricing by GPU")

  fig, ax = plt.subplots()

  sns.barplot(
      x=df["Gpu_brand"],
      y=df["Price"],
      ax=ax
  )
  ax.tick_params(axis="x", rotation=90)
  st.pyplot(fig)
  plt.close(fig),

  st.title("Avg Pricing by CPU Type")

  fig, ax = plt.subplots()

  sns.barplot(
      x=df["Cpu_brand"],
      y=df["Price"],
      ax=ax
  )
  ax.tick_params(axis="x", rotation=90)
  st.pyplot(fig)
  plt.close(fig),

  #

  st.title("Avg Pricing by Ops category")

  fig, ax = plt.subplots()

  sns.barplot(
      x=df["ops"],
      y=df["Price"],
      ax=ax
  )
  ax.tick_params(axis="x", rotation=90)
  st.pyplot(fig)
  plt.close(fig),


elif st.session_state["active_view"] == "Insights":
    st.title('Ops vs price')
    sns.barplot(x=df['ops'],y=df['Price'])
    plt.xticks(rotation=90)
#___________________________________________How it Works_______________________________________________________________
elif st.session_state["active_view"] == "How it works":



    st.html("""
     <style>
    
     .how-wrapper {
         width: 100%;
         max-width: 900px;
         margin: 80px auto 30px auto;
         text-align: center;
     }
    
     /* Main heading */
     .how-title {
         font-size: 36px;
         font-weight: 700;
         margin-bottom: 8px;
         color: #f5f5f5;
     }
    
     .how-title span {
         color: #8b7cff;
     }
    
     .how-subtitle {
         color: #8f98a8;
         font-size: 16px;
         margin-bottom: 35px;
     }
    
    
     /* Individual step card */
     .how-card {
         width: 90%;
         max-width: 700px;
         margin: 0 auto;
    
         display: flex;
         align-items: center;
    
         text-align: left;
    
         padding: 22px 25px;
    
         background: rgba(15, 22, 40, 0.85);
    
         border: 1px solid #27375c;
         border-radius: 14px;
    
         box-sizing: border-box;
    
         transition: all 0.25s ease;
     }
    
     /* Hover effect */
     .how-card:hover {
         transform: translateY(-2px);
         border-color: #7669e8;
         box-shadow: 0 8px 25px rgba(80, 70, 180, 0.15);
     }
    
    
     /* Left icon */
     .how-icon {
         width: 55px;
         height: 55px;
    
         min-width: 55px;
    
         display: flex;
         align-items: center;
         justify-content: center;
    
         border-radius: 12px;
    
         background: #111d38;
    
         font-size: 26px;
    
         margin-right: 18px;
     }
    
    
     /* Step number */
     .how-number {
         width: 38px;
         height: 38px;
    
         min-width: 38px;
    
         border-radius: 50%;
    
         display: flex;
         align-items: center;
         justify-content: center;
    
         font-size: 14px;
         font-weight: 700;
    
         color: white;
    
         margin-right: 18px;
     }
    
    
     /* Step content */
     .how-content {
         flex: 1;
     }
    
     .how-heading {
         font-size: 19px;
         font-weight: 650;
         color: #f2f2f2;
         margin-bottom: 6px;
     }
    
     .how-text {
         font-size: 14px;
         line-height: 1.55;
         color: #8f98a8;
     }
    
    
     /* Number colors */
     .n1 {
         background: #635bff;
     }
    
     .n2 {
         background: #27c99a;
     }
    
     .n3 {
         background: #f2a33a;
     }
    
     .n4 {
         background: #d957b6;
     }
    
     .n5 {
         background: #31bce8;
     }
    
    
     /* Arrow */
     .how-arrow {
         height: 42px;
    
         display: flex;
         align-items: center;
         justify-content: center;
    
         font-size: 27px;
    
         color: #7569e8;
     }
    
    
     /* Bottom line */
     .how-footer {
         width: 90%;
         max-width: 700px;
    
         margin: 45px auto 0 auto;
    
         padding-top: 20px;
    
         border-top: 1px solid #252c3a;
    
         color: #737b8c;
    
         font-size: 13px;
     }
    
    
     /* Mobile */
     @media (max-width: 700px) {
    
         .how-wrapper {
             margin-top: 60px;
         }
    
         .how-title {
             font-size: 30px;
         }
    
         .how-card {
             width: 94%;
             padding: 18px;
         }
    
         .how-icon {
             width: 48px;
             height: 48px;
             min-width: 48px;
             font-size: 22px;
             margin-right: 12px;
         }
    
         .how-number {
             width: 34px;
             height: 34px;
             min-width: 34px;
             font-size: 12px;
             margin-right: 12px;
         }
    
         .how-heading {
             font-size: 17px;
         }
    
         .how-text {
             font-size: 13px;
         }
    
     }
    
     </style>
    
    
     <div class="how-wrapper">
    
         <!-- Heading -->
    
         <div class="how-title">
             💻 How It <span>Works</span>
         </div>
    
         <div class="how-subtitle">
             From laptop specifications to estimated price
         </div>
    
    
         <!-- STEP 1 -->
    
         <div class="how-card">
    
             <div class="how-icon">
                 🗄️
             </div>
    
             <div class="how-number n1">
                 01
             </div>
    
             <div class="how-content">
    
                 <div class="how-heading">
                     Data Loading
                 </div>
    
                 <div class="how-text">
                         A dataset of more than 3000 laptops containing specifications
        such as brand, processor, RAM, storage, display and price..
                 </div>
    
             </div>
    
         </div>
    
    
         <!-- Arrow -->
         <div class="how-arrow">
             ↓
         </div>
    
    
    
         <!-- STEP 2 -->
    
         <div class="how-card">
    
             <div class="how-icon">
                 🔍
             </div>
    
             <div class="how-number n2">
                 02
             </div>
    
             <div class="how-content">
    
                 <div class="how-heading">
                     EDA(Investigation of Data)
                 </div>
    
                 <div class="how-text">
                    We explore the dataset, understand feature relationships,Detecting Missing Values,
         Visualizing the relationship between Features and Price using Matplotlib,Seaborn and Plotly.
                 </div>
    
             </div>
    
         </div>
    
         <!-- Arrow -->
    
         <div class="how-arrow">
             ↓
         </div>
    
    
    
         <!-- STEP 2 -->
    
         <div class="how-card">
    
             <div class="how-icon">
                 ⚙️
             </div>
    
             <div class="how-number n2">
                 03
             </div>
    
             <div class="how-content">
    
                 <div class="how-heading">
                     Data Cleaning & Feature Engineering
                 </div>
    
                 <div class="how-text">
                     Raw features are cleaned and useful information is
                     extracted, such as CPU brand, RAM, weight, SSD storage
                     and screen PPI.
                 </div>
    
             </div>
    
         </div>
    
    
         <!-- Arrow -->
    
         <div class="how-arrow">
             ↓
         </div>
    
    
         <!-- STEP 3 -->
    
         <div class="how-card">
    
             <div class="how-icon">
                🔄
             </div>
    
             <div class="how-number n3">
                 04
             </div>
    
             <div class="how-content">
    
                 <div class="how-heading">
                     Column Transformation
                 </div>
    
                 <div class="how-text">
                     Categorical features are converted into Numerical Columns using
                     One-Hot Encoding .
                 </div>
    
             </div>
    
         </div>
    
    
         <!-- Arrow -->
    
         <div class="how-arrow">
             ↓
         </div>
    
    
         <!-- STEP 4 -->
    
         <div class="how-card">
    
             <div class="how-icon">
                 🔗
             </div>
    
             <div class="how-number n4">
                 05
             </div>
    
             <div class="how-content">
    
                 <div class="how-heading">
                     Machine Learning Pipeline
                 </div>
    
                 <div class="how-text">
                     ColumnTransformer is connected with the 
                     machine learning model through a Pipeline .
                 </div>
    
             </div>
    
         </div>
    
    
         <!-- Arrow -->
    
         <div class="how-arrow">
             ↓
         </div>
    
    
         <!-- STEP 5 -->
    
         <div class="how-card">
    
             <div class="how-icon">
                 🎯
             </div>
    
             <div class="how-number n5">
                 06
             </div>
    
             <div class="how-content">
    
                 <div class="how-heading">
                     Price Prediction
                 </div>
    
                 <div class="how-text">
               Multiple models were evaluated using R² Score and MAE to select the best-performing model.
               Stacking Regressor performed best with R² Score .925 .
                     
                 </div>
    
             </div>
    
         </div>
         
         <div class="how-arrow">
             ↓
         </div>
    
    
         <!-- STEP 4 -->
    
         <div class="how-card">
    
             <div class="how-icon">
                 🌐
             </div>
    
             <div class="how-number n4">
                 Live
             </div>
    
             <div class="how-content">
    
                 <div class="how-heading">
                     Deployment
                 </div>
    
                 <div class="how-text">
                     The Model is Converted to a webapp using the streamlit and Deployed on Streamlit Cloud and Git hub.
                 </div>
    
             </div>
    
         </div>
    
    
         <!-- Arrow -->
    
    
         <!-- Footer -->
    
         <div class="how-footer">
             💻 Laptop Price Predictor &nbsp; • &nbsp;
             Built with Streamlit 
         </div>
    
     </div>
     """)







































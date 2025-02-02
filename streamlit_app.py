import streamlit as st

# Branding: Seitenkonfiguration
st.set_page_config(page_title="LinkedIn ROI-Rechner", page_icon="📊", layout="centered")

# Branding: Logo & Header
st.image("C:\Users\ersin\Downloads\Kein Titel (389 x 129 px) (389 x 129 px) (3).png", width=200)  # Ersetze mit deinem eigenen Logo
st.title("🚀 LinkedIn ROI-Rechner")
st.write("Berechne schnell und einfach deine LinkedIn-Marketing-Rentabilität.")

# Eingabefelder mit verbessertem Design
st.markdown("### 📌 Gib deine Werte ein:")
spent = st.number_input("💰 Geld ausgegeben auf LinkedIn ($)", min_value=0.0, format="%.2f")
earned = st.number_input("💵 Geld verdient durch LinkedIn ($)", min_value=0.0, format="%.2f")

# ROI Berechnung
def calculate_linkedin_roi(spent, earned):
    if spent == 0:
        return "Kein Investment getätigt. ROI kann nicht berechnet werden."
    roi = ((earned - spent) / spent) * 100
    return f"Ihr LinkedIn-ROI beträgt {roi:.2f}%. {'✅ Rentabel' if roi > 0 else '❌ Nicht rentabel'}"

# Button für Berechnung
if st.button("📊 ROI berechnen"):
    result = calculate_linkedin_roi(spent, earned)
    st.success(result)

# Footer mit Branding
st.markdown("---")
st.write("💡 Entwickelt von **[Dein Unternehmen]** | 🔗 [Mehr erfahren](https://dein-link.com)")

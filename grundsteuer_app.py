import streamlit as st

# FDP-Logo einbinden
logo_url = "https://www.fdp-mv.de/sites/default/files/2020-10/MV-Logo.png"
st.markdown(
    f"""
    <div style="display: flex; justify-content: flex-end; align-items: center;">
        <img src="{logo_url}" width="120" style="margin-top: 10px; margin-right: 10px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Titel der App
st.title("Grundsteuerberechnung in Wismar - Vergleich alte und neue Grundsteuer")

# Eingabefelder für den alten und neuen Grundsteuermessbetrag
alter_grundsteuermessbetrag = st.number_input("Alter Grundsteuermessbetrag (Euro)", min_value=0.0, step=1.0)
neuer_grundsteuermessbetrag = st.number_input("Neuer Grundsteuermessbetrag (Euro)", min_value=0.0, step=1.0)

# Hebesätze für alte und neue Grundsteuer
alter_hebesatz = 580
neuer_hebesatz = 541

# Berechnung der alten Grundsteuer
alte_grundsteuer = (alter_grundsteuermessbetrag * alter_hebesatz) / 100

# Berechnung der neuen Grundsteuer
neue_grundsteuer = (neuer_grundsteuermessbetrag * neuer_hebesatz) / 100

# Berechnung des erforderlichen Hebesatzes für Aufkommensneutralität
if neuer_grundsteuermessbetrag > 0:
    neutral_hebesatz = (alte_grundsteuer / neuer_grundsteuermessbetrag) * 100
else:
    neutral_hebesatz = None

# Berechnung der Differenz zwischen neuer und alter Grundsteuer
steuer_differenz = neue_grundsteuer - alte_grundsteuer

# Anzeige der Ergebnisse in Tabellen
st.subheader("Alte Grundsteuerberechnung")
st.write(f"Alter Grundsteuermessbetrag: {alter_grundsteuermessbetrag} Euro")
st.write(f"Alter Hebesatz: {alter_hebesatz} v.H.")
st.write(f"Berechnete alte Grundsteuer: {alte_grundsteuer:.2f} Euro")

st.subheader("Neue Grundsteuerberechnung")
st.write(f"Neuer Grundsteuermessbetrag: {neuer_grundsteuermessbetrag} Euro")
st.write(f"Neuer Hebesatz: {neuer_hebesatz} v.H.")
st.write(f"Berechnete neue Grundsteuer: {neue_grundsteuer:.2f} Euro")

# Anzeige des erforderlichen Hebesatzes für Aufkommensneutralität
if neutral_hebesatz is not None:
    st.subheader("Erforderlicher Hebesatz für Aufkommensneutralität")
    st.write(f"Um die gleiche Steuerlast wie zuvor zu erreichen, müsste der Hebesatz bei {neutral_hebesatz:.2f} v.H. liegen.")
else:
    st.write("Bitte geben Sie einen neuen Grundsteuermessbetrag größer als 0 ein, um den erforderlichen Hebesatz zu berechnen.")

# Anzeige der Differenz zwischen neuer und alter Grundsteuer
st.subheader("Veränderung der Steuerlast")
st.write(f"Die Differenz zwischen der neuen und der alten Grundsteuer beträgt: {steuer_differenz:.2f} Euro")
if steuer_differenz > 0:
    st.write("Die Steuerlast wird voraussichtlich steigen.")
elif steuer_differenz < 0:
    st.write("Die Steuerlast wird voraussichtlich sinken.")
else:
    st.write("Die Steuerlast bleibt unverändert.")

# Erklärung der Rechenschritte
st.subheader("Erklärung der Berechnungsschritte")
st.write("""
1. **Berechnung der alten Grundsteuer**: Der alte Grundsteuermessbetrag wird mit dem alten Hebesatz (580 v.H.) multipliziert.
2. **Berechnung der neuen Grundsteuer**: Der neue Grundsteuermessbetrag wird mit dem neuen Hebesatz (541 v.H.) multipliziert.
3. **Erforderlicher Hebesatz für Aufkommensneutralität**: Die alte Grundsteuer wird durch den neuen Grundsteuermessbetrag geteilt. So wird der Hebesatz berechnet, der für eine persönliche Aufkommensneutralität nötig wäre.
4. **Differenz der Steuerlast**: Die Differenz zwischen der neuen und alten Grundsteuer wird berechnet, um die Änderung der Steuerlast aufzuzeigen.
""")

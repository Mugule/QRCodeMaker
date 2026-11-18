import io

import streamlit as st
import qrcode

st.title("Générateur de QR code")

texte = st.text_input("Données du QR code ci-dessous")

if st.button("Envoyer"):
    if texte:
        img = qrcode.make(texte)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        st.image(buffer.getvalue(), caption="Votre QR code")
    else:
        st.warning("Veuillez saisir un texte.")

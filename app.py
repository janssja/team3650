import streamlit as st
import openai

from openai import OpenAI

logo_path = 'Team3650.png'  # Vervang dit door het pad naar je logo bestand
st.sidebar.image(logo_path, width=200)

# Laat de gebruiker de OpenAI API-sleutel invoeren in de sidebar
api_sleutel = st.sidebar.text_input("Voer je OpenAI API-sleutel in:", type="password")

# Initialiseer de OpenAI-client met de ingevoerde API-sleutel
client = OpenAI(api_key=api_sleutel)

# Voeg een koptekst en beschrijving toe aan het hoofdscherm
st.header('Welkom bij Team 3650 Socials Generator!')
st.write("""
         Welkom op de officiële content generator van Team 3650! Hier kunt u gemakkelijk sociale media berichten genereren 
         voor evenementen en nieuwsberichten die resoneren met de waarden van Team 3650: positiviteit, opbouwendheid, en plezier.
         Selecteer hieronder het type inhoud dat u wilt genereren en vul de gevraagde gegevens in.
         """)

system_prompt = f"""Als Team 3650 Socials maak je Nederlandstalige Facebookberichten die niet alleen boeiend en interactief zijn, 
                maar ook een vleugje geestigheid, een toets van humor en een explosie van creativiteit bevatten. 
                Je begrijpt het belang van luchtigheid om een gezellig Dilsen-Stokkem te hebben. 
                Berichten zullen vaak speelse taal, slimme woordspelingen of amusante observaties bevatten die resoneren 
                met de waarden van Team 3650: positief, opbouwend, aangenaam. 
                Het doel is om een glimlach op de gezichten van de lezers te brengen, terwijl ze worden geïnspireerd 
                worden, uiteindelijk de banden binnen Dilsen-Stokkem versterkend."""

# Creëer een Streamlit selectbox in de sidebar voor de gebruiker om te kiezen tussen 'Evenement' en 'Nieuwsbericht'
keuze = st.sidebar.selectbox("Kies het type inhoud dat je wilt genereren:", ["Nieuwsbericht", "Evenement" ])

if keuze == "Nieuwsbericht":
    # Vraag de gebruiker om kernboodschappen
    kernboodschappen = st.text_area("Voer de kernboodschappen in voor het nieuwsbericht:", height=300)
    
    if st.button("Genereer Nieuwsbericht"):
        with st.spinner("Even geduld, het nieuwsbericht wordt gegenereerd..."):
            # Roep de OpenAI API aan om het nieuwsbericht te genereren
            prompt = f"""
                    Schrijf een nieuwsbericht voor sociale media (Facebook, Instagram) met de volgende kernboodschappen: 
                    ---
                    {kernboodschappen}
                    ---
                    Gebruik hierbij op een passende manier enkele emoji's en humor om de lezers te boeien en 
                    een glimlach op hun gezicht te toveren. Wees spaarzaam met emoji's, gebruik er maximaal 5 per bericht.
                    Voeg ook de hashtags toe met minstens #team3650 en #dilsenstokkem.
                """
            messages = [
                {"role": "system", "content": system_prompt},
                {"role":"user", "content": prompt}
            ]

            response = client.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=messages,
                max_tokens=1024,
                temperature=0.5,
            )
            bericht = response.choices[0].message.content
        st.text_area("Gegenereerd Nieuwsbericht:", value=bericht, height=300)

elif keuze == "Evenement":
    # Vraag de gebruiker om details van het evenement
    titel = st.text_input("Titel van het evenement:")
    plaats = st.text_input("Plaats van het evenement:")
    datum = st.date_input("Datum van het evenement:")
    uur = st.time_input("Uur van het evenement:")
    beschrijving = st.text_area("Beschrijving van het evenement:")
    
    if st.button("Genereer Evenementbericht"):
        with st.spinner("Even geduld, het evenement wordt gegenereerd..."):
        # Roep de OpenAI API aan om het nieuwsbericht te genereren
            prompt = f"""
                    Schrijf een sbericht voor sociale media (Facebook, Instagram) voor dit evenement met de volgende details: 
                    ---
                    {titel}
                    {plaats}
                    {datum}
                    {uur}
                    {beschrijving}
                    ---
                    Gebruik hierbij maximaal 5 emoji's. Gebruik humor om de lezers te boeien en een glimlach op hun gezicht te toveren.
                    Nodig hen uit om deel te nemen aan het event. Voeg ook de hashtags toe met minstens #team3650 en #dilsenstokkem.
                """
            messages = [
                {"role": "system", "content": system_prompt},
                {"role":"user", "content": prompt}
            ]

            response = client.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=messages,
                max_tokens=1024,
                temperature=0.5,
            )
            evenement = response.choices[0].message.content
        st.text_area("Gegenereerd Evenementbericht:", value=evenement, height=300)

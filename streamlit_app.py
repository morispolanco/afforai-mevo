import streamlit as st
import requests

def get_api_response(question):
    url = "https://api.afforai.com/api/api_completion"
    api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
    session_id = "65489d7c9ad727940f2ab26f"
    payload = {
        "apiKey": api_key,
        "sessionID": session_id,
        "history": [{"role": "user", "content": question}],
        "powerful": False,
        "google": True
    }
    response = requests.post(url, json=payload)
    return response.json()

def main():
    st.title("Preguntas sobre las leyes de Guatemala")
    question = st.text_input("Hacer una pregunta")

    if st.button("Obtener respuesta"):
        if question:
            response = get_api_response(question)
            st.write("Respuesta:")
            st.write(response)
        else:
            st.write("Por favor ingresa una pregunta antes de presionar el botón.")

if __name__ == "__main__":
    main()


import streamlit as st

def main():
    st.title("Currículum Vitae")

    st.sidebar.header("Navegación")
    page = st.sidebar.radio("Ir a", ["Perfil", "Experiencia", "Educación", "Habilidades", "Contactar"])

    if page == "Perfil":
        st.image("static/img/imagen.jpeg", width=200)
        st.header("Perfil")
        st.write("Nombre: Juan Pérez")
        st.write("Descripción: Ingeniero de Software con más de 5 años de experiencia en desarrollo web.")

    elif page == "Experiencia":
        st.header("Experiencia Profesional")
        st.write("Empresa XYZ, Ingeniero de Software, 2020 - Presente")
        st.write("Responsabilidades: Desarrollo de aplicaciones web usando Python y JavaScript.")

    elif page == "Educación":
        st.header("Educación")
        st.write("Universidad ABC, Licenciatura en Ciencias de la Computación, 2015 - 2019")

    elif page == "Habilidades":
        st.header("Habilidades")
        st.write("- Python")
        st.write("- JavaScript")
        st.write("- React")
        st.write("- SQL")

    elif page == "Contactar":
        st.header("Contactar")
        st.write("Email: juan.perez@example.com")
        st.write("Teléfono: +1234567890")

if __name__ == "__main__":
    main()

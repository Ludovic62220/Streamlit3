import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu



# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()


def accueil():
    with st.sidebar:
        # Récupérer le nom de l'utilisateur connecté
        nom_utilisateur = st.session_state["name"]
        st.write(f"Bienvenue sur mon site")
        st.write(
                    f"""
                    <div style="color: red">
                        <strong>{nom_utilisateur}</strong>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


        # Bouton de déconnexion
        authenticator.logout("Déconnexion")
    with st.sidebar:
        selection = option_menu(
        menu_title=None,
        options = ["Accueil", "Photos de Chats", "Photos de Chiens"]
    )

    st.title("Bienvenue chez Ludovic")




    # Création du menu qui va afficher les choix qui se trouvent dans la variable options

    # On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
        st.write("Bienvenue sur ma bio")
        st.write("Fort de plus de 15 ans d’expérience en ressources humaines et en gestion des données, je souhaite aujourd’hui valoriser mes compétences en analyse de données en tant que Data Analyst.")
        st.write("Spécialiste d’Excel, VBA et Access, je maîtrise l’automatisation et l’organisation des données pour éclairer les prises de décision stratégiques. Mon parcours m’a permis de concevoir des outils d’analyse efficaces, d’optimiser les workflows informatiques et de produire des reportings précis répondant aux besoins stratégiques.")
        st.write("Doté d’un esprit rigoureux et orienté solutions, je suis déterminé à accompagner les organisations dans l’exploitation de leurs données pour améliorer leur performance et leur stratégie globale.")

    elif selection == "Photos de Chats":
        st.write("Bienvenue sur la page des chats")
        st.write("Le chat domestique (Felis catus ou Felis silvestris catus) est la forme domestique du chat sauvage Felis silvestris, une espèce de mammifères carnivores, de la famille des Félidés.")
        st.write("Selon les résultats de travaux menés en 2006 et 20071, le chat domestique est une sous-espèce du chat sauvage issue d’ancêtres appartenant à la sous-espèce du chat sauvage d’Afrique (Felis silvestris lybica). Les premières domestications ont probablement lieu il y a 8 000 à 10 000 ans au Néolithique dans le Croissant fertile, époque correspondant au début de la culture de céréales et à l'engrangement de réserves susceptibles d'être attaquées par des rongeurs, le chat devenant alors pour l’Homme un auxiliaire utile se prêtant à la domestication.")
        st.page_link("https://fr.wikipedia.org/wiki/Chat", label="Lien sur Wikipédia spécial Chat")
        
        chat1, chat2, chat3 = st.columns(3)

        with chat1:
            st.header("Chat 1")
            st.image("https://feelloo.com/wp-content/uploads/2019/10/jeune-chat-pexels-104827-900x598.jpeg")

        with chat2:
            st.header("Chat 2")
            st.image("https://www.lesrecettesdedaniel.fr/modules/hiblog/views/img/upload/original/488818546d009ef951fa45b42f404daa.jpg")

        with chat3:
            st.header("Chat 3")
            st.image("https://www.agria.fr/imagevault/publishedmedia/9vgy569fypmkernjg4x6/Orange_cat_laying_indoor.jpg")

    elif selection == "Photos de Chiens":
        st.write("Bienvenue sur la page des chien")
        st.write("Le Chien (Canis lupus familiaris) est la sous-espèce domestique de Canis lupus (Loup gris), un mammifère de la famille des Canidés (Canidae), laquelle comprend également le dingo, chien domestique retourné à l'état sauvage.")
        st.page_link("https://fr.wikipedia.org/wiki/Chien", label="Lien sur Wikipédia spécial Chien")
        
      

        chien1, chien2 = st.columns(2)

        with chien1:
            st.header("Chien 1")
            st.image("https://sevetys.fr/_next/image/?url=https%3A%2F%2Fcharming-angel-5ca83bf286.media.strapiapp.com%2FLes_5_races_de_chiens_preferees_des_Francais_057c589a8c.webp&w=3840&q=75")

        with chien2:
            st.header("Chien 2")
            st.image("https://cdn.futura-sciences.com/sources/images/actu/esperance-vie-chiens-chiot-golden-retriever.jpg")



if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
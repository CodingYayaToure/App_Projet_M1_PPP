import streamlit as st
import numpy as np
import plotly.graph_objects as go

def setup_page_configuration():
    """Configuration de la page Streamlit avec en-tête personnalisé"""
    st.set_page_config(
        page_title="Simulateur Dynamique Avancé",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
def display_sidebar():
    """Affiche le logo et les paramètres dans la barre latérale"""
    # Ajouter le logo en haut de la barre latérale
    st.sidebar.image("logo_unchk.png", width=200)  # Remplacez par votre logo

    # Paramètres de simulation
    st.sidebar.header("🔧 Paramètres de Simulation")
    population_initiale = st.sidebar.slider(
        "Population Initiale", 
        min_value=10**3, 
        max_value=10**7, 
        value=10**6
    )
    taux_decroissance = st.sidebar.slider(
        "Taux de Décroissance", 
        min_value=0.0001, 
        max_value=0.01, 
        value=0.001, 
        step=0.0001
    )
    
    # Informations sous les paramètres
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Informations")
    st.sidebar.markdown("""
    **Projet proposé par :**
    -**Tuteur** : Dr. Abou SENE
     Email: abou1.sene@unchk.edu.sn
    -**Étudiant :** Yaya TOURE  
     Email : yaya.toure@unchk.edu.sn  
    [🔗 LinkedIn](https://www.linkedin.com/in/yaya-toure-8251a4280/)  
    [🌐 GitHub](https://github.com/CodingYayaToure)
    """)
    
    return population_initiale, taux_decroissance

def population_model(t, p0=10**6, r=0.001):
    """
    Modèle dynamique de population avec paramètres configurables
    
    Args:
        t (np.ndarray): Valeurs de temps
        p0 (float): Population initiale
        r (float): Taux de décroissance
    
    Returns:
        np.ndarray: Population à l'instant t
    """
    # Calculer K
    K = (p0 - 2) / (p0 + 1)
    
    # Calculer p(t)
    return (K * np.exp(-r * t) + 2) / (1 - K * np.exp(-r * t))

def derivative_analysis(p, r=0.003, c=0.001, d=0.002):
    """
    Analyse de la stabilité par la dérivée
    
    Args:
        p (np.ndarray): Valeurs de population
        r (float): Taux de croissance
        c (float): Coefficient de croissance
        d (float): Constante de stabilisation
    
    Returns:
        np.ndarray: Taux de changement
    """
    return r * p - c * p**2 - d

def create_three_plots(t_values, p_values, p_range, dp_values):
    """
    Création des trois graphiques Plotly
    
    Args:
        t_values (np.ndarray): Valeurs de temps
        p_values (np.ndarray): Valeurs de population
        p_range (np.ndarray): Plage de population
        dp_values (np.ndarray): Valeurs de dérivée
    
    Returns:
        tuple: Figures Plotly (fig1, fig2, fig3)
    """
    
    # Premier graphique : Évolution complète
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=t_values, y=p_values, mode='lines', 
        name='Population $p(t)$', line=dict(color='blue')
    ))
    
    fig1.add_trace(go.Scatter(
        x=t_values, y=[2]*len(t_values), mode='lines', 
        name="Équilibre stable $p=2$", line=dict(color='green', dash='dash')
    ))
    
    fig1.add_trace(go.Scatter(
        x=t_values, y=[1]*len(t_values), mode='lines', 
        name="Équilibre instable $p=1$", line=dict(color='red', dash='dash')
    ))
    
    fig1.update_layout(
        title="Évolution de la population de poissons au fil du temps",
        xaxis_title="Temps (minutes)",
        yaxis_title="Population $p(t)$",
        legend=dict(x=0.01, y=0.99),
        template="plotly_white"
    )

   # Deuxième graphique : Zoom sur les équilibres
    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=t_values, y=p_values, mode='lines', 
        name='Population $p(t)$', line=dict(color='blue')
    ))
    fig2.add_trace(go.Scatter(
        x=t_values, y=[2]*len(t_values), mode='lines', 
        name="Équilibre stable $p=2$", line=dict(color='green', dash='dash')
    ))
    fig2.add_trace(go.Scatter(
        x=t_values, y=[1]*len(t_values), mode='lines', 
        name="Équilibre instable $p=1$", line=dict(color='red', dash='dash')
    ))
    fig2.update_yaxes(range=[0.5, 2.5])
    fig2.update_layout(
        title="Zoom sur les équilibres $p=1$ (instable) et $p=2$ (stable)",
        xaxis_title="Temps (minutes)",
        yaxis_title="Population $p(t)$",
        legend=dict(x=0.01, y=0.99),
        template="plotly_white"
    )

    # Troisième graphique : Analyse de la stabilité
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=p_range, y=dp_values, mode='lines', 
        name="Taux de changement $\\frac{dp}{dt}$", line=dict(color='blue')
    ))
    fig3.add_trace(go.Scatter(
        x=[2]*len(dp_values), y=np.linspace(-0.01, 0.01, len(dp_values)), 
        mode='lines', name="Équilibre stable $p=2$", 
        line=dict(color='green', dash='dash')
    ))
    fig3.add_trace(go.Scatter(
        x=[1]*len(dp_values), y=np.linspace(-0.01, 0.01, len(dp_values)), 
        mode='lines', name="Équilibre instable $p=1$", 
        line=dict(color='red', dash='dash')
    ))
    fig3.add_trace(go.Scatter(
        x=p_range, y=[0]*len(p_range), mode='lines', 
        name="État stable $\\frac{dp}{dt} = 0$", line=dict(color='black', dash='dash')
    ))
    fig3.update_layout(
        title="Analyse de la stabilité autour des équilibres",
        xaxis_title="Population $p$",
        yaxis_title="Taux de changement $\\frac{dp}{dt}$",
        legend=dict(x=0.01, y=0.99),
        template="plotly_white"
    )

    return fig1, fig2, fig3

def main():
    try:
        setup_page_configuration()
        
        # Affichage des paramètres dans la barre latérale
        population_initiale, taux_decroissance = display_sidebar()

        # Génération des données
        t_values = np.linspace(0, 5000, 1000)
        p_values = population_model(t_values, p0=population_initiale, r=taux_decroissance)

        p_range = np.linspace(0.5, 2.5, 100)
        dp_values = derivative_analysis(p_range)

        # Créer les graphiques
        fig1, fig2, fig3 = create_three_plots(t_values, p_values, p_range, dp_values)

        # Affichage des graphiques
        st.plotly_chart(fig1, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(fig2, use_container_width=True)
        
        with col2:
            st.plotly_chart(fig3, use_container_width=True)

        # Section d'analyse
        st.markdown("### 📊 Analyse et Interprétation")
        st.markdown("""
            #### Observations Clés
            - **Équilibre Stable** : La population converge vers un point d'équilibre à 2.
            - **Dynamique Non-Linéaire** : Comportement complexe influencé par les paramètres initiaux.
            - **Points d'Équilibre** : 
              * $p=1$ : Point d'équilibre instable.
              * $p=2$ : Point d'équilibre stable.
            - **Comportement Dynamique** : La population tend naturellement vers l'équilibre stable.
            """)

    except Exception as e:
        st.exception(e)  # Affiche l'erreur dans une manière conviviale

if __name__ == "__main__":
    main()


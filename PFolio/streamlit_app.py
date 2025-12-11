import streamlit as st

st.set_page_config(
    page_title="Anil Vasudevakurup | Product Management Portfolio",
    page_icon="💼",
    layout="wide"
)

NAME = "Anil Vasudevakurup"
ROLE = "Director of Product Management | SaaS, AI, Field Service, ERP Integrations | Customer Success Leader"
LOCATION = "Denver, CO"
EMAIL = "your.email@example.com"
LINKEDIN_URL = "https://www.linkedin.com/in/anil-vasudevakurup/"

HEADSHOT_PATH = "assets/anil_headshot.jpg"


def main():

    # ---------- HEADER ----------
    cols = st.columns([1, 3])

    with cols[0]:
        try:
            st.image(HEADSHOT_PATH, use_container_width=True)
        except:
            pass

    with cols[1]:
        st.title(NAME)
        st.write(ROLE)
        st.markdown(
            f"**{LOCATION}** • 📧 `{EMAIL}` • "
            f"[LinkedIn]({LINKEDIN_URL})"
        )

    st.divider()

    # ---------- QUICK LINKS ----------
    st.subheader("Quick Portfolio Links")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.link_button("🔗 LinkedIn", LINKEDIN_URL)
    with col2:
        st.link_button("📄 Download Resume", "#")
    with col3:
        st.link_button("🌐 Portfolio Website",
                       "https://avasudev18.github.io/PFolioAV.github.io/index.html")

    st.divider()

    # ---------- CORE EXPERTISE ----------
    st.subheader("Core Expertise")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
### Product Leadership  
- Strategy & Vision  
- Roadmapping & Prioritization  
- Cross-Functional Alignment  
- Go-to-Market Execution  

### AI / Data  
- AI Agents & GenAI  
- RAG & Retrieval Pipelines  
- Recommendations & Forecasting  
            """
        )

    with col2:
        st.markdown(
            """
### Enterprise Systems  
- Oracle Field Service  
- ERP Commerce Integrations  
- SaaS Platform Architecture  

### Customer Success  
- Adoption Frameworks  
- Renewal Strategy  
- NRR / GRR / CSAT Analytics  
            """
        )

    st.info("Use the **sidebar navigation** to explore Bio, Case Studies, Leadership Work, Innovation Lab, and Experience.")


if __name__ == "__main__":
    main()

st.divider()
st.subheader("Explore the Portfolio")

# Create 5 cards in a grid layout
card_cols = st.columns(3)

with card_cols[0]:
    st.markdown(
        """
        <div style="padding:15px; border-radius:10px; border:1px solid #ddd;">
            <h4>🧑‍💼 Bio</h4>
            <p>Professional background, values, and leadership philosophy.</p>
            <a href="/Bio" target="_self">
                <button style="padding:6px 12px;">Open</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

with card_cols[1]:
    st.markdown(
        """
        <div style="padding:15px; border-radius:10px; border:1px solid #ddd;">
            <h4>💼 Live Implementations</h4>
            <p>Case studies on AI commerce, OFS, ERP integrations, and digital transformation.</p>
            <a href="/Live_Implementations" target="_self">
                <button style="padding:6px 12px;">Open</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

with card_cols[2]:
    st.markdown(
        """
        <div style="padding:15px; border-radius:10px; border:1px solid #ddd;">
            <h4>📊 Customer Success Leadership</h4>
            <p>Portfolio transformation, revenue growth, and NRR/GRR frameworks.</p>
            <a href="/Customer_Success_Leadership" target="_self">
                <button style="padding:6px 12px;">Open</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Second row
card_cols_2 = st.columns(2)

with card_cols_2[0]:
    st.markdown(
        """
        <div style="padding:15px; border-radius:10px; border:1px solid #ddd;">
            <h4>🤖 Innovation Lab</h4>
            <p>AI agents, prototypes, product research, and future-thinking workflows.</p>
            <a href="/Thought_Leadership_&_Innovation_Lab" target="_self">
                <button style="padding:6px 12px;">Open</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

with card_cols_2[1]:
    st.markdown(
        """
        <div style="padding:15px; border-radius:10px; border:1px solid #ddd;">
            <h4>📜 Experience & Education</h4>
            <p>Career milestones, certifications, and academic journey.</p>
            <a href="/Experience_&_Education" target="_self">
                <button style="padding:6px 12px;">Open</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

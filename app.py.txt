if file:
    portfolio = pd.read_csv(file)
    st.dataframe(portfolio)

    bond_data = {}
    with st.spinner("Fetching bond data..."):
        for sec in portfolio["security_id"]:
            bond_data[sec] = fetch_full_bond_data(sec)

    df = build_cashflow(portfolio, bond_data)

    if not df.empty:
        pivot = df.groupby("date")[["principal","interest"]].sum().reset_index()
        pivot["total"] = pivot["principal"] + pivot["interest"]

        st.subheader("📅 Cashflow")
        st.dataframe(pivot)

        fig = px.bar(pivot, x="date", y="total", title="Liquidity Load")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🔍 Detailed")
        st.dataframe(df)

        st.download_button(
            "Download",
            df.to_csv(index=False),
            "cashflow.csv"
        )
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Candlestick Merger", layout="centered")

st.title("🕯️ Merge Two 5-min Candlesticks into One 10-min Candle")

st.markdown("### Input Two 5-minute Candles")

col1, col2 = st.columns(2)

with col1:
    o1 = st.number_input("Candle 1 - Open", value=100.0)
    h1 = st.number_input("Candle 1 - High", value=105.0)
    l1 = st.number_input("Candle 1 - Low", value=98.0)
    c1 = st.number_input("Candle 1 - Close", value=102.0)

with col2:
    o2 = st.number_input("Candle 2 - Open", value=102.0)
    h2 = st.number_input("Candle 2 - High", value=108.0)
    l2 = st.number_input("Candle 2 - Low", value=101.0)
    c2 = st.number_input("Candle 2 - Close", value=107.0)

# Merge logic
merged_open = o1
merged_high = max(h1, h2)
merged_low = min(l1, l2)
merged_close = c2

# Plot
fig = go.Figure(data=[
    go.Candlestick(
        x=['5-min Candle 1', '5-min Candle 2', 'Merged 10-min Candle'],
        open=[o1, o2, merged_open],
        high=[h1, h2, merged_high],
        low=[l1, l2, merged_low],
        close=[c1, c2, merged_close],
        increasing_line_color='green',
        decreasing_line_color='red'
    )
])

fig.update_layout(
    title="Candlestick Chart",
    xaxis_title="Candles",
    yaxis_title="Price",
    xaxis_rangeslider_visible=False
)

st.plotly_chart(fig, use_container_width=True)

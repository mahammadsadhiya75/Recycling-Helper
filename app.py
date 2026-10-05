import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Recycling Helper",
    page_icon="♻️",
    layout="centered"
)

# ---------------- CUSTOM STYLE ----------------

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 25px;
    font-weight: bold;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
    '<div class="main-title">♻️ Recycling Helper</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">A simple tool to identify waste and learn how to dispose of it responsibly.</div>',
    unsafe_allow_html=True
)

# ---------------- TEXT WASTE CLASSIFICATION ----------------

st.markdown(
    '<div class="section-title">🗑️ Check Waste Category</div>',
    unsafe_allow_html=True
)

item = st.text_input(
    "Enter a waste item:",
    placeholder="Example: plastic bottle"
)

if st.button("🔍 Check Waste Category"):

    if item:
        item = item.lower().strip()

        # Recyclable waste
        if any(word in item for word in [
            "plastic bottle",
            "plastic",
            "paper",
            "cardboard",
            "glass bottle"
        ]):
            st.success("♻️ Category: Recyclable Waste")
            st.info("🗑️ Put this item in the recyclable waste collection.")
            st.write("💡 Tip: Make sure the item is clean before recycling.")

        # Biodegradable waste
        elif any(word in item for word in [
            "food",
            "banana peel",
            "vegetable",
            "fruit",
            "food waste"
        ]):
            st.success("🌱 Category: Biodegradable Waste")
            st.info("🗑️ Put this item in the wet-waste or compost bin.")
            st.write("💡 Tip: Organic waste can be converted into compost.")

        # E-waste
        elif any(word in item for word in [
            "mobile phone",
            "phone",
            "laptop",
            "computer",
            "charger",
            "electronic"
        ]):
            st.warning("🔌 Category: E-Waste")
            st.info("🗑️ Take this item to an authorized e-waste collection centre.")
            st.write("💡 Tip: Do not put electronic items in normal household waste.")

        # Hazardous waste
        elif any(word in item for word in [
            "battery",
            "medicine",
            "chemical",
            "paint"
        ]):
            st.error("⚠️ Category: Hazardous Waste")
            st.info("🗑️ Do not put this item in regular household waste.")
            st.write("💡 Tip: Give hazardous waste to an appropriate collection facility.")

        else:
            st.warning("❓ Waste category not found.")
            st.write("Try items such as:")
            st.write(
                "Plastic bottle, Paper, Food, Battery, "
                "Mobile phone, Cardboard"
            )

    else:
        st.warning("Please enter an item.")

# ---------------- IMAGE UPLOAD ----------------

st.divider()

st.markdown(
    '<div class="section-title">📷 Upload a Waste Image</div>',
    unsafe_allow_html=True
)

uploaded_image = st.file_uploader(
    "Choose an image of a waste item",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:

    st.image(
        uploaded_image,
        caption="Uploaded Waste Image",
        width="stretch"
    )

    st.success("✅ Image uploaded successfully!")

    # ---------------- DISPOSAL GUIDE ----------------

    st.info("🗑️ Disposal Guide")

    st.write("""
♻️ **Recyclable Waste:** Put it in the dry/recyclable waste bin.

🌱 **Biodegradable Waste:** Put it in the wet-waste or compost bin.

🔌 **E-Waste:** Take it to an authorized e-waste collection centre.

⚠️ **Hazardous Waste:** Do not put it in regular household waste.
Give it to an appropriate collection facility.
""")

    # ---------------- RECYCLING TIPS ----------------

    st.info("💡 Recycling Tips")

    st.write("""
♻️ **Recyclable:** Clean and dry recyclable items before putting them in the bin.

🌱 **Biodegradable:** Use food and garden waste for composting whenever possible.

🔌 **E-Waste:** Never throw electronic items in regular household bins.

⚠️ **Hazardous:** Keep batteries, medicines and chemicals separate from normal waste.
""")

# ---------------- FOOTER ----------------

st.divider()

st.caption("♻️ Recycling Helper | Promoting responsible waste management")
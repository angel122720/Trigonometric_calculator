import streamlit as st
import numpy as np

# Page Configuration
st.set_page_config(page_title="TrigVerify - BSED Math Project", layout="centered")

st.title("📐 Trigonometric Identity Verifier")
st.write("BSED Mathematics: Technology in Teaching and Learning Project")

# Sidebar Reference
st.sidebar.header("📚 Identity Cheat Sheet")
st.sidebar.info("""
- **Quotient:** tan(x) = sin(x)/cos(x)
- **Reciprocal:** sec(x) = 1/cos(x)
- **Pythagorean:** sin²x + cos²x = 1
- **Co-Function:** sin(π/2 - x) = cos(x)
""")

# Main UI
col1, col2 = st.columns(2)

with col1:
    lhs = st.text_input("Left-Hand Side (LHS)", placeholder="e.g., sin(x)/cos(x)")

with col2:
    rhs = st.text_input("Right-Hand Side (RHS)", placeholder="e.g., tan(x)")

if st.button("Check Identity"):
    if lhs and rhs:
        try:
            # Create a range of values to test the identity
            x = np.linspace(0, 2*np.pi, 100)
            
            # Define math functions for eval
            safe_dict = {
                "sin": np.sin, "cos": np.cos, "tan": np.tan,
                "arcsin": np.arcsin, "arccos": np.arccos, "arctan": np.arctan,
                "pi": np.pi, "x": x,
                "sec": lambda x: 1/np.cos(x),
                "csc": lambda x: 1/np.sin(x),
                "cot": lambda x: 1/np.tan(x)
            }
            
            # Evaluate both sides
            left_val = eval(lhs.replace('^', '**'), {"__builtins__": None}, safe_dict)
            right_val = eval(rhs.replace('^', '**'), {"__builtins__": None}, safe_dict)
            
            # Compare with tolerance
            if np.allclose(left_val, right_val, equal_nan=True):
                st.success("✨ Correct! This is a valid identity.")
                st.balloons()
            else:
                st.error("❌ Not an identity. The values do not match.")
                
        except Exception as e:
            st.warning("⚠️ Format Error! Please use (x) and proper math symbols.")
    else:
        st.info("Please enter expressions in both boxes.")

st.divider()
st.caption("Tip: Use x for theta, * for multiply, and ^ for exponents (e.g., sin(x)^2).")

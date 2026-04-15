import streamlit as st
from sympy import symbols, sin, cos, tan, sec, csc, cot, diff, simplify, trigsimp, latex

# Page Setup
st.set_page_config(page_title="TrigSolver - BSED Math", page_icon="📐")

# Custom CSS for aesthetics
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stTextInput>div>div>input { background-color: #ffffff; border-radius: 10px; border: 2px solid #3498db; }
    .result-card { background-color: #ffffff; padding: 20px; border-radius: 15px; border-left: 5px solid #3498db; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("📐 Interactive Trig Assistant")
st.write("Enter a trigonometric expression to see its **Identities** and **Derivative**.")

# User Input
user_input = st.text_input("Enter Trig Expression (e.g., sin(x), tan(x)^2, sin(x)*cos(x))", "sin(x)")

if user_input:
    try:
        # Define the symbol x
        x = symbols('x')
        
        # Parse the input (replaces ^ with ** for Python)
        expr = eval(user_input.replace('^', '**'))
        
        st.divider()

        # 1. DERIVATIVE CALCULATION
        st.subheader("📝 Derivative")
        derivative = diff(expr, x)
        st.latex(f"\\frac{{d}}{{dx}}({latex(expr)}) = {latex(derivative)}")
        
        # 2. IDENTITIES / SIMPLIFICATION
        st.subheader("🔄 Equivalent Identities")
        
        # We use trigsimp to find the simplest form
        simplified = trigsimp(expr)
        
        if simplified == expr:
            # If trigsimp doesn't change it, we try to expand it using basic rules
            st.info("This expression is already in its simplest fundamental form.")
            
            # Show basic breakdown if it's tan, sec, etc.
            if "tan" in user_input:
                st.latex(f"{latex(expr)} = \\frac{{\\sin(x)}}{{\\cos(x)}}")
            elif "sec" in user_input:
                st.latex(f"{latex(expr)} = \\frac{{1}}{{\\cos(x)}}")
        else:
            st.success("Alternative identity found:")
            st.latex(f"{latex(expr)} \\equiv {latex(simplified)}")

        # 3. INTERACTIVE CHALLENGE
        st.sidebar.header("💡 Learning Challenge")
        st.sidebar.write(f"Can you prove why the derivative of **{user_input}** is **{derivative}**?")
        if st.sidebar.button("Show Hint"):
            st.sidebar.write("Try using the Power Rule or Product Rule if the expression is complex!")

    except Exception as e:
        st.error("⚠️ Invalid Syntax. Please use format like `sin(x)` or `cos(x)**2`.")

st.divider()
st.caption("BSED Mathematics - Technology in Teaching and Learning Project")

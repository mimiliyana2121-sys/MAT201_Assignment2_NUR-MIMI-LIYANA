import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Title and formatting
st.title("MAT201: Multivariable Gradient Visualizer")
st.markdown("This app explains the **Gradient and Direction of Steepest Ascent**.")

# 1. Interactive Input Section
st.sidebar.header("User Settings")
equation = st.sidebar.selectbox("Select Function", ["Paraboloid: x² + y²", "Wave: sin(x) * cos(y)"])
x_p = st.sidebar.slider("X coordinate", -2.0, 2.0, 1.0)
y_p = st.sidebar.slider("Y coordinate", -2.0, 2.0, 1.0)

# 2. Mathematical Logic (CO1: Fundamental Concepts)
if equation == "Paraboloid: x² + y²":
    z_func = lambda x, y: x**2 + y**2
    gx, gy = 2*x_p, 2*y_p  # Derivatives
else:
    z_func = lambda x, y: np.sin(x) * np.cos(y)
    gx, gy = np.cos(x_p)*np.cos(y_p), -np.sin(x_p)*np.sin(y_p)

z_p = z_func(x_p, y_p)

# 3. 3D Visualisation (CO1: Cognitive Application)
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)
Z = z_func(X, Y)

fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, opacity=0.8)])
# Add the point and the gradient vector
fig.add_trace(go.Scatter3d(x=[x_p], y=[y_p], z=[z_p], mode='markers', marker=dict(size=8, color='red')))
fig.add_trace(go.Line3d(x=[x_p, x_p+gx*0.5], y=[y_p, y_p+gy*0.5], z=[z_p, z_p], line=dict(color='yellow', width=7)))

st.plotly_chart(fig)
st.write(f"**Gradient Vector at ({x_p}, {y_p}):** ∇f = <{gx:.2f}, {gy:.2f}>")

from frontend.candidate_ui import render_registration, render_interview
from frontend.dashboard import analytics_dashboard
from frontend.candidate_portal import candidate_portal
from frontend.admin_controls import render_admin_panel
import streamlit as st
from utils.session_manager import initialize_session  # Import initialize_session
from frontend.candidate_ui import render_registration
from backend.analysis_engine import analyze_resume
from config import load_positions

# Load position configurations
POSITION_CONFIG = load_positions()

def main():
    """Main application controller"""
    st.set_page_config(
        page_title="AI Recruiter Pro v5.2",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Menu", [
        "Registration", 
        "Interview", 
        "Dashboard", 
        "Candidate Portal", 
        "Admin"
    ], key="main_nav")
    
    # Check if the user is coming from the registration form
    if "current_page" in st.session_state and st.session_state["current_page"] == "interview":
        render_interview()
    elif menu == "Registration":
        render_registration(POSITION_CONFIG)
    elif menu == "Interview":
        state = initialize_session()
        if state.stage == "interview":
            render_interview()
        else:
            st.info("Please complete registration first")
    elif menu == "Dashboard":
        analytics_dashboard()
    elif menu == "Candidate Portal":
        candidate_portal()
    elif menu == "Admin":
        render_admin_panel()

if __name__ == "__main__":
    main()
import streamlit as st
from phi.agent import Agent
from phi.model.openai.like import OpenAILike
from fpdf import FPDF
import tempfile
from datetime import datetime
import os
import json

# PDF Export Class Definition
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Developer Community Agents Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf(topic, response):
    pdf = PDF()
    pdf.add_page()
    
    # Add title and date
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f'Topic: {topic}', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 10, f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 1)
    pdf.ln(10)
    
    # Add the response content
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, response)
    
    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        pdf.output(tmp_file.name)
        return tmp_file.name

# Set page configuration
st.set_page_config(page_title="👨‍💻 Developer Community Agents", layout="centered")

# Initialize session state for API keys, topic, and responses
if 'gaia_api_key' not in st.session_state:
    st.session_state['gaia_api_key'] = ''
if 'topic' not in st.session_state:
    st.session_state['topic'] = ''
if 'response' not in st.session_state:
    st.session_state['response'] = None

# Streamlit sidebar for API key and About the Agents section
with st.sidebar:
    st.title("Configuration")
    st.session_state['gaia_api_key'] = st.text_input("Enter your Gaia API Key", type="password").strip()
    
    # Add info about API key
    st.info("Get your own free Gaia API key: https://docs.gaianet.ai/getting-started/authentication", icon="ℹ️")

    # About the Agents section with expandable details
    st.markdown("### About the Agents")
    
    # Developer Relations Agent
    with st.expander("👨‍💻 **Developer Relations Agent**"):
        st.markdown("""
        - **Role**: Educates developers about the platform via webinars, blogs, and tutorials.
        - **Responsibilities**:
          - Create engaging tutorials, SDKs, and sample projects.
          - Engage with the developer community through forums, Discord, GitHub, and other platforms.
          - Create troubleshooting guides and ensure active communication channels.
        """)
    
    # Community Manager Agent
    with st.expander("👩‍💼 **Community Manager Agent**"):
        st.markdown("""
        - **Role**: Onboards new community members and facilitates discussions.
        - **Responsibilities**:
          - Create onboarding playbooks with guidelines and resources for new members.
          - Facilitate discussions, Q&A sessions, and regular events like AMAs, hackathons, or study groups.
          - Moderate community spaces to ensure adherence to the code of conduct.
        """)
    
    # Partnerships Manager Agent
    with st.expander("🤝 **Partnerships Manager Agent**"):
        st.markdown("""
        - **Role**: Identifies and manages partnerships with companies, universities, and influencers.
        - **Responsibilities**:
          - Identify opportunities to collaborate with companies, universities, and influencers.
          - Negotiate partnerships for co-branded events, integrations, or sponsorships.
          - Create partnership proposal templates and agreements.
        """)
    
    # Community Lead Agent
    with st.expander("🧭 **Community Lead Agent**"):
        st.markdown("""
        - **Role**: Strategizes the vision and direction of the community's growth and initiatives.
        - **Responsibilities**:
          - Strategize the vision and direction of the community's growth and initiatives.
          - Align community goals with the platform's mission and values.
          - Create a long-term roadmap for community development and establish a leadership structure with ambassador/mentor programs.
        """)

# Validate API keys
if not st.session_state['gaia_api_key']:
    st.error("Please enter your Gaia API key in the sidebar.")
    st.stop()

# Create the Developer Relations Agent
devrel_agent = Agent(
    name="Developer Relations Agent",
    role="Educates developers about the platform via webinars, blogs, and tutorials.",
    model=OpenAILike(
        id="llama",
        api_key=st.session_state['gaia_api_key'],  # Pass the API key here
        base_url="https://llama8b.gaia.domains/v1"  # Custom base URL
    ),
    instructions=[
        "Create engaging tutorials, SDKs, and sample projects for the given topic.",
        "Engage with the developer community through forums, Discord, GitHub, and other platforms.",
        "Create troubleshooting guides and ensure active communication channels.",
        "Respond with a detailed text response that includes all the necessary information.",
    ],
    show_tool_calls=False,  # Disable tool calls
    markdown=True,
)

# Create the Community Manager Agent
community_manager_agent = Agent(
    name="Community Manager Agent",
    role="Onboards new community members and facilitates discussions.",
    model=OpenAILike(
        id="llama",
        api_key=st.session_state['gaia_api_key'],  # Pass the API key here
        base_url="https://llama8b.gaia.domains/v1"  # Custom base URL
    ),
    instructions=[
        "Create onboarding playbooks with guidelines and resources for new community members.",
        "Facilitate discussions, Q&A sessions, and regular events like AMAs, hackathons, or study groups.",
        "Moderate community spaces to ensure adherence to the code of conduct.",
        "Respond with a detailed text response that includes all the necessary information.",
        "If tasked with increasing engagement on Discord, provide a JSON object containing suggestions for activities, channels, and roles to boost participation.",
    ],
    show_tool_calls=False,  # Disable tool calls
    markdown=True,
)

# Create the Partnerships Manager Agent
partnerships_manager_agent = Agent(
    name="Partnerships Manager Agent",
    role="Identifies and manages partnerships with companies, universities, and influencers.",
    model=OpenAILike(
        id="llama",
        api_key=st.session_state['gaia_api_key'],  # Pass the API key here
        base_url="https://llama8b.gaia.domains/v1"  # Custom base URL
    ),
    instructions=[
        "Identify opportunities to collaborate with companies, universities, and influencers.",
        "Negotiate partnerships for co-branded events, integrations, or sponsorships.",
        "Create partnership proposal templates and agreements.",
        "Respond with a detailed text response that includes all the necessary information.",
    ],
    show_tool_calls=False,  # Disable tool calls
    markdown=True,
)

# Create the Community Lead Agent
community_lead_agent = Agent(
    name="Community Lead Agent",
    role="Strategizes the vision and direction of the community's growth and initiatives.",
    model=OpenAILike(
        id="llama",
        api_key=st.session_state['gaia_api_key'],  # Pass the API key here
        base_url="https://llama8b.gaia.domains/v1"  # Custom base URL
    ),
    instructions=[
        "Strategize the vision and direction of the community's growth and initiatives.",
        "Align community goals with the platform's mission and values.",
        "Create a long-term roadmap for community development and establish a leadership structure with ambassador/mentor programs.",
        "Respond with a detailed text response that includes all the necessary information.",
    ],
    show_tool_calls=False,  # Disable tool calls
    markdown=True,
)

# Combine all agents into a team
developer_community_team = Agent(
    team=[devrel_agent, community_manager_agent, partnerships_manager_agent, community_lead_agent],
    model=OpenAILike(
        id="llama",
        api_key=st.session_state['gaia_api_key'],  # Pass the API key here
        base_url="https://llama8b.gaia.domains/v1"  # Custom base URL
    ),
    instructions=[
        "Collaborate to generate a comprehensive response for the given topic.",
        "Ensure the response includes detailed information from all agents.",
        "Use clear and structured formatting.",
        "If a task is transferred to another agent, ensure the receiving agent completes the task and returns a response.",
    ],
    show_tool_calls=False,  # Disable tool calls
    markdown=True,
)

# Streamlit main UI
st.title("👨‍💻 Developer Community Agents")
st.markdown("Enter a topic to generate resources and strategies for developer community engagement.")

# Predefined options for common tasks
st.markdown("### Try the tool with these common tasks:")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Increase Discord Engagement"):
        st.session_state['topic'] = "Increase user engagement on our Discord server"
with col2:
    if st.button("Create Onboarding Plan"):
        st.session_state['topic'] = "Create an onboarding plan for new community members"
with col3:
    if st.button("Develop Partnership Strategy"):
        st.session_state['topic'] = "Develop a partnership strategy for the community"
with col4:
    if st.button("Design Community Roadmap"):
        st.session_state['topic'] = "Design a long-term roadmap for community growth"

# Query bar for topic input
st.session_state['topic'] = st.text_input("Or enter your own topic:", value=st.session_state.get('topic', ''), placeholder="e.g., API Integration, Community Building, etc.")

# Start button
if st.button("Start"):
    if not st.session_state['topic']:
        st.error("Please enter a topic.")
    else:
        # Display loading animations while generating responses
        with st.spinner("Generating Developer Community Resources..."):
            response = developer_community_team.run(
                f"the topic is: {st.session_state['topic']}",
                stream=False
            )
        
        # Store response in session state
        st.session_state['response'] = response.content

# Display response if it exists in session state
if st.session_state.get('response'):
    st.markdown("### Developer Community Response:")
    
    # Hide agent delegation details and focus on the final response
    final_response = st.session_state['response']
    if "transfer_task_to_community_manager_agent" in final_response:
        # Extract the JSON task transfer and process it
        try:
            task_transfer = json.loads(final_response.split("```json")[1].split("```")[0].strip())
            st.markdown(f"**Task Transferred to Community Manager Agent:** {task_transfer['parameters']['task_description']}")
            
            # Simulate the Community Manager Agent processing the task
            community_manager_response = community_manager_agent.run(
                f"Task: {task_transfer['parameters']['task_description']}",
                stream=False
            )
            
            st.markdown("### Community Manager Agent Response:")
            st.markdown(community_manager_response.content)
        except Exception as e:
            st.error(f"Error processing task transfer: {str(e)}")
    else:
        st.markdown(final_response)
    
    st.divider()

    # Add Export to PDF button
    if st.button("Export to PDF"):
        try:
            pdf_file = create_pdf(
                st.session_state['topic'],
                final_response
            )
            
            with open(pdf_file, "rb") as file:
                pdf_data = file.read()
            
            st.download_button(
                label="📥 Download PDF",
                data=pdf_data,
                file_name=f"developer_community_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/pdf",
                key='download-pdf'
            )
        except Exception as e:
            st.error(f"Error generating PDF: {str(e)}")

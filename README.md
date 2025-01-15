
# Developer Community Agents

A Streamlit-based application that leverages AI agents to help manage and grow developer communities. The app provides tools for creating onboarding plans, increasing Discord engagement, developing partnership strategies, and designing community roadmaps.

## Features

- **Developer Relations Agent**: Creates tutorials, SDKs, and sample projects to educate developers.
- **Community Manager Agent**: Onboards new members, facilitates discussions, and moderates community spaces.
- **Partnerships Manager Agent**: Identifies and manages partnerships with companies, universities, and influencers.
- **Community Lead Agent**: Strategizes the vision and direction of the community's growth and initiatives.
- **Interactive UI**: Users can input topics and receive detailed responses from the agents.
- **PDF Export**: Export generated responses as PDFs for easy sharing and documentation.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.8 or higher**
- **Streamlit**: Install via `pip install streamlit`
- **FPDF**: Install via `pip install fpdf`
- **Gaia API Key**: Obtain a free API key from [Gaia](https://docs.gaianet.ai/getting-started/authentication).

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/harishkotra/developer-community-agents.git
   cd developer-community-agents
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**:
   ```bash
   streamlit run dev_comm_agents.py
   ```
4. **Enter Your Gaia API Key**:
  When the app launches, enter your Gaia API key in the sidebar. Obtain a free API key from [Gaia](https://docs.gaianet.ai/getting-started/authentication)

## Usage

1. Enter a Topic:
	- Use the input field to enter a topic or click one of the predefined task buttons (e.g., "Increase Discord Engagement").
2. Generate Responses:
	-	Click the "Start" button to generate a response from the team of agents.
3. View and Export Responses:
	- The generated response will be displayed on the screen.
	- Click "Export to PDF" to download the response as a PDF.
4. Explore Agent Details:
	- In the sidebar, click on an agent's name to learn more about its role and responsibilities.

## Extending the Project with Composio.dev

[Composio.dev](https://composio.dev) is a platform that allows you to integrate AI agents with external tools and APIs. Here are some ideas for extending this project using Composio:
1. Integrate with Discord:
	- Use Composio to connect the Community Manager Agent with Discord's API.
	- Automatically post engagement strategies or onboarding plans directly to your Discord server.
2. Google Docs Integration:
	- Use Composio to integrate with Google Docs.
	- Automatically save generated responses as Google Docs for easy collaboration.
3. GitHub Integration:
	- Connect the Developer Relations Agent with GitHub's API.
	- Automatically create repositories or issues for sample projects and tutorials.
4. Slack Integration:
	- Use Composio to integrate with Slack.
	- Send notifications or updates about community activities directly to your Slack channels.
5. CRM Integration:
	- Connect the Partnerships Manager Agent with a CRM like HubSpot or Salesforce.
	- Automatically track and manage partnership opportunities.

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes and push to the branch.
- Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

### Credits
Inspired by Shubham Saboo's [demo](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_tutorials/ai_teaching_agent_team).

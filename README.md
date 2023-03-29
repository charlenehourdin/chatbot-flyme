# :dart: Welcome to Fly Me Chatbot !
The aim of this project is to build a 1st version of a MVP chatbot, which will help colleagues of the FlyMe company to book a vacation.

<p>
  <a href="https://www.python.org/" target="_blank"> 
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"
      alt="python"/>
  </a>
  <img alt="azure" src="https://img.shields.io/badge/Azure_DevOps-0078D7?style=for-the-badge&logo=azure-devops&logoColor=white"/>
  

It does implement the following features :

- Use [LUIS](https://www.luis.ai) to implement core AI capabilities
- Implement a multi-turn conversation using Dialogs
- Handle user interruptions for such things as `Help` or `Cancel`
- Prompt for and validate requests for information from the user
- Use [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/cloudservices) to monitor your bot

This bot uses LUIS, an AI based cognitive service, to implement language understanding and Application Insights, an extensible Application Performance Management (APM) service for web developers on multiple platforms.

It can be used to book a travel with the following information :

- Origin
- Destination
- Start date
- End date
- Budget

**Expected output**: the Bot should be able to reformulate the flight's details, ask confirmation (yes/no) from the user, then, if correct, end conversation with a booking message.

## Task of project 
  
:heavy_check_mark: Perform Exploratory Data Analysis (EDA) and Data wrangling;
  
:heavy_check_mark: Build LUIS App;
  
:heavy_check_mark: Copy [Microsoft Core Bot Python Samples, including App Insights](https://github.com/microsoft/BotBuilder-Samples/tree/main/samples/python/21.corebot-app-insights) from Github, and adapt the scripts to the project's objectives;
  
:heavy_check_mark: Monitor the performance of the chatbot with App Insights;
  
:heavy_check_mark: Plan and integrate automated testing;
  
:heavy_check_mark: Embed in Azure Web App for model serving (deploy).

# :scroll: To try this sample
 
- Clone the repository

```bash
git clone https://github.com/charlenehourdin/chatbot-flyme.git
```
- In a terminal, navigate to the bot folder
- Activate your desired virtual environment
- In the terminal, type `pip install -r requirements.txt`
- Run your bot with `python app.py`
  

# :robot: Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- You can test the bot using Bot Framework Emulator
  
### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- File -> Open Bot
- Enter a Bot URL of `http://localhost:8000/api/messages`
  
# :cloud: Deployment to Azure

To learn more about deploying a bot to Azure, see [Deploy your bot to Azure](https://aka.ms/azuredeployment) for a
complete list of deployment instructions.


# :computer: Tools and Dependencies
Azure Portal, Azure LUIS cognitive services (Language Understanding), Microsoft Bot Framework SDK, Azure Web App, Azure Application Insights, VS Code, Github (CI/CD)

<code>pip install botbuilder-core</code><br>
<code>pip install botbuilder-ai</code><br>
<code>pip install botbuilder-dialogs</code><br>
<code>pip install botbuilder-applicationinsights</code><br>
<code>pip install botbuilder-integration-applicationinsights-aiohttp</code><br>
<code>pip install datatypes-date-time</code><br>

# :pushpin: References 
- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Dialogs](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0)
- [Gathering Input Using Prompts](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-prompts?view=azure-bot-service-4.0&tabs=csharp)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Language Understanding using LUIS](https://docs.microsoft.com/en-us/azure/cognitive-services/luis/)
- [Channels and Bot Connector Service](https://docs.microsoft.com/en-us/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)
- [Application insights Overview](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview)
- [Getting Started with Application Insights](https://github.com/Microsoft/ApplicationInsights-aspnetcore/wiki/Getting-Started-with-Application-Insights-for-ASP.NET-Core)
- [Filtering and preprocessing telemetry in the Application Insights SDK](https://docs.microsoft.com/azure/azure-monitor/app/api-filtering-sampling)

 



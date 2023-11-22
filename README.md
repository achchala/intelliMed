# IntelliMed QueryBot

### PointClickCare AI Hackathon Project
- AI-powered chatbot leveraging language models to simplify the extraction of data from Electronic Health Record (EHR)
databases and provide critical insights
- The LangChain library, OpenAI ChatCompletion API, and prompt engineering are used to transform plain language input and database schema into SQL queries, and then provide medical insights back in plain language based on the SQL query results
  - The LLM learns from the schema about the structure of the data
  - It uses this knowledge to construct a SQL query to fetch the data to answer the user's question
  - After executing the query, LLM checks the answer
  - If it's valid, the answer is presented to the user in plain language
  - If it's invalid, LLM uses the feedback to refine the query and repeat the process
- This solution aims to streamline the interaction between health professionals and electronic health records and make data access more robust

<p align="center">
  <a href="https://youtu.be/NJLV1SX9dqY" target="_blank">
    <img src="https://github.com/achchala/intelliMed/assets/54039275/082bbc0f-0928-4ff3-8be6-2fa2b21e8176" alt="Image" width="50%">
  </a>
</p>

  
- Note: This repository does not contain the front-end code, this chatbot functionality was integrated into PointClickCare's CORE web application

### Next Steps!

- [ ] Fine-tuning LLama-2 for this specific use case; this approach would've required more costs (processing power and time) for implementation but may yield better results

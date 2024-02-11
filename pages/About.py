import streamlit as st


def show():

    st.title("InnSight")

    st.subheader("Inspiration")
    st.markdown("""<div style="text-align: justify;">You\'re scheduling your well-deserved vacation after a stressful few months.
                 And if you're on a tight budget, you want to make the most of your trip while staying within your means. 
                However, while looking for hotels and flights, you face a brick wall right away. You wind up spending
                 a lot of time on Google looking for hotels.. Some hotels are pricey, others have negative ratings, 
                and some are rather far from where you want to stay. Furthermore, you do not receive the expected results, 
                and after repeated disappointment, you give up on your quest. And your hard-earned trip is postponed 
                to another day, leaving you disappointed. That is where InnSight comes into play. We created InnSight 
                to assist you in discovering hotels and accommodations for your next vacation in the most efficient manner. 
                You just enter your specifications and receive a information of hotels/stays along with insights about it, 
                that meets your needs without any fuss. It is as straightforward and handy as speaking with 
                your personal travel agent.</div>""", unsafe_allow_html=True)

    st.subheader("What does it do?")
    st.markdown("""<div style="text-align: justify;">InnSight is a Generative AI chatbots which helps an individual with findin
                g hotels in a city and providing insights about the hotel like location, reviews, ratings, price level, etc as
                 per his/her preferences. InnSight is a RAG (Retrieval Augmented Generation) chatbot using vector database for
                 semantic similarity search. The model was trained on the traversaal_ai/hotels_dataset available
                 on HuggingFace</div>""", unsafe_allow_html=True)
    

    st.subheader("How did we build it?")

    st.markdown("""\n Level 1:""")
    st.markdown("""<div style="text-align: justify;">The offered code describes the creation of a complex system developed for Retrieval-Augmented Generation (RAG) capability, which responds to users' semantic inquiries about hotels. Using Qdrant as a vector database, the system allows customers to enter sophisticated questions about their hotel preferences. Initially, the code prepares the environment by setting the QdrantClient and loading the OpenAI API key from a YAML file. To help with semantic query processing, the system defines a function, which searches the Qdrant collection based on user prompts and returns top matched results that are structured for user understanding. The system also augments user prompts with extra context collected from Qdrant search results. Finally, using OpenAI's GPT-3.5 model, the rag function creates replies by submitting enhanced prompts for completion requests, giving consumers detailed explanations of why selected hotels match their choices.</div>""", unsafe_allow_html=True)

    st.markdown("""\n Level 2:""")
    st.markdown("""<div style="text-align: justify;">Our conversational system was substantially improved by incorporating dynamic data from the Traversaal AI’s API. This connection enabled our chatbot to retrieve real-time and contextually appropriate information about hotels or places depending on user questions. We created a method that communicates with the Traversaal API, passing user requests and getting relevant data. When we receive an API response, we parse it to retrieve important facts such as response text providing hotel or location information, as well as connected site URLs. For ease of handling, this structured data has been contained into a data class entitled SearchResult. Integrating this information into our RAG application allows our chatbot to offer more relevant and context-appropriate replies. By dynamically combining facts obtained from the Traversaal API, our chatbot acquires a greater grasp of user questions and context, enabling more tailored and relevant conversations.</div>""", unsafe_allow_html=True)
    
    st.markdown("""\n Level 3:""")
    st.markdown("""<div style="text-align: justify;">We used Python & various libraries, including langchain, OpenAI, and Qdrant, to create a fully functional chatbot. We used langchain's schema to define message structures, allowing the chatbot to interpret system, human, and AI-generated communications. To easily activate OpenAI functions for RAG outputs, we added the langchain_openai module, which allows for direct connection with OpenAI's API. This integration enabled our chatbot to dynamically change its replies to user requests, exploiting the immense information contained within GPT-3.5. Our chatbot provides tailored hotel suggestions, responds to user inquiries, and engages in meaningful conversations about travel preferences by combining natural language processing techniques and intelligent dialogue management. </div>""", unsafe_allow_html=True)

    st.subheader("\n Challenges we ran into")
    st.markdown("""<div style="text-align: justify;">We used Mistral's LLM model before switching to Open AI's LLM. However, we discovered that the querying performance was poor since there were insufficient GPU resources available on the Intel Developer cloud, and hence the model could not be quantized. Furthermore, the Mistral model is memory intensive. During peak hours, IDC required 100% of its CPU, so we tried running Google Collaboratory, but it took up to 15 GB of memory. 
                \nHuggingface was unavailable for an extended period of time, exacerbating the project's deadline. </div>""", unsafe_allow_html=True)

    st.subheader("\n Accomplishments that we are proud of")
    st.markdown("""<div style="text-align: justify;">Developing a GenAI project from scratch with zero knowledge within 24hours. \n</div>""", unsafe_allow_html=True)    
    
    st.subheader("\n What we learned")
    st.markdown("""<div style="text-align: justify;"> In the course of our project, we delved into the fundamentals of Risk Assessment and Governance (RAG), General Artificial Intelligence (Gen AI), and Large Language Models (LLMs). Our exploration of these critical concepts has not only broadened our understanding but has also offered valuable insights into the intricate landscape of modern technologies.
                \nFirstly, our study of Risk Assessment and Governance (RAG) equipped us with a comprehensive understanding of how to evaluate and manage risks within the technological domain. We delved into various frameworks and methodologies employed in RAG, gaining insights into the identification, assessment, and mitigation of potential risks associated with our project and similar endeavors.
                \nSecondly, our exploration of General Artificial Intelligence (Gen AI) provided us with a deeper appreciation for the broader implications and applications of artificial intelligence beyond narrow, task-specific functions. Understanding the principles of Gen AI allowed us to appreciate the potential societal impact, ethical considerations, and the challenges associated with developing and deploying advanced AI systems.
                \nLastly, our focus on Large Language Models (LLMs) opened up new horizons in natural language processing and generation. We gained insights into the capabilities and limitations of LLMs, recognizing their significance in various applications such as chatbots, language translation, and content generation. Understanding the underlying mechanisms of LLMs enhanced our ability to leverage these models effectively in our project.
                \nIn summary, our exploration of RAG, Gen AI, and LLMs has not only enriched our theoretical knowledge but has also provided us with practical insights that are directly applicable to the successful execution of our project. These fundamental learnings lay a robust foundation for informed decision-making and strategic planning in the ever-evolving landscape of technology and artificial intelligence.</div>""", unsafe_allow_html=True)

    
    st.subheader("\n What's next for InnSight?")
    st.markdown("""<div style="text-align: justify;">The model can be improved in the following way: 
                \n1. Fine-tune the model to ensure it performs well on specific tasks or datasets. 
                \n2. Enhance the metaprompt to guide the model towards generating desired outputs more effectively. 
                \n3. Implement streaming responses to provide immediate feedback to users, rather than waiting for the entire response to be generated. 
                \n4. Display web search results within the chatbot interface to offer users additional resources or context. 
                \n5. Transition from proprietary platforms like OpenAI to open-source alternatives like Llama or Mistral for greater transparency and control over AI development.
                \n\nMoreover, the potential of Innsight can be expanded in following ways:
                \n1. Full fledged travel itinerary can be developed by InnSight. 
                \n2. The app can potentially provide flight plans, locations to travel, detailed day-to-day itineraries that maximize travel experience and satisfaction. 
                </div>""", unsafe_allow_html=True)

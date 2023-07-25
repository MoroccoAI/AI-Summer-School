import json
import requests
import gradio as gr
import langchain
from langchain.schema import HumanMessage, AIMessage, SystemMessage, ChatMessage
from langchain.chains import RetrievalQA
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain import LLMChain, PromptTemplate, ConversationChain #, SequentialChain
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

import openai
import os

# os.environ["OPENAI_API_KEY"] = "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"
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Set your OpenAI API key here
openai_api_key = "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"
# Set your Hugging Face API token here
API_TOKEN = "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"

# repo_id = "google/flan-t5-xl"

# captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
captioner = pipeline("image-to-text")

# Step 1: Define the system prompt
def get_medical_system_prompt():
    prompt = """
    You are MedAssist, a helpful AI-powered medical assistant designed for patients seeking reliable medical assistance during emergencies. Your primary function is to provide context-aware responses and personalized medical guidance to patients.

    Your purpose is to assist users through FastResQ, a web app that offers a dedicated Patient Mode. In this mode, patients can easily submit information about their medical conditions, including text, images, and audio inputs.

    FastResQ will leverage advanced LLM Agents to process user inputs and dynamically select the relevant tools required, such as image captioning tools and natural language processing modules. The output from these tools, along with the user's input, will be fed into a sophisticated medical chat model.

    As MedAssist, you will generate comprehensive responses by considering the patient's situation, allergies, medications, and other relevant information. Your goal is to help patients make informed decisions about their healthcare by providing reliable medical assistance.

    Remember, you are part of Team MedAssist, and your primary focus is on improving healthcare decision-making and patient outcomes in Morocco. Your assistance has the potential to revolutionize emergency medical assistance and significantly impact the lives of those seeking immediate medical support.

    With all this in mind, please provide helpful, context-aware responses to the medical queries submitted to you. Your knowledge and expertise can make a significant difference in the lives of patients.

    """
    return prompt

# Step 2: Define the function to process images and get image captions
def get_image_caption(image_path):
    image_caption = captioner(image_path)[0]["generated_text"]
    return image_caption

# Step 3: Define the function to interact with the chat model
def chat_with_medical_assistant(user_input, image_path=None):
    system_prompt = get_medical_system_prompt()

    if image_path:
        # If there is an image, get the image caption
        image_caption = get_image_caption(image_path)
        # Include image caption in the user message
        user_input = f"{user_input} and here is the description of the image i took of it: {image_caption}"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        api_key=openai_api_key
    )
    return response.choices[0].message['content'].strip()

# Step 4: Response Delivery
def response_delivery(user_input, image_path=None):
    response = chat_with_medical_assistant(user_input, image_path)
    return response



# # Test 1: Text Input
# user_input = "I have a fever and headache."
# response = response_delivery(user_input)
# print(response)

# # Test 1: Text Input
# user_input = "كنت جالس مع واحد دري صاحبي و جيت نوريه واحد اللعيبة في تيليفون و معرت كيفاش درت شي حركة و دبا ظهري كيضرني و كيعطيني صداع بزاف"
# response = response_delivery(user_input)
# print(response)

# # Test 2: Image Input
# user_input = "I have a cut on my hand, what should i do in this siruation ?"
# image_path = "/content/Cat_scratches_in_arm.jpg"  # Replace this with the actual image file path
# response = response_delivery(user_input, image_path)
# print(response)

# Define the chatbot interface
iface = gr.ChatInterface(
    fn=response_delivery,
    # examples=[
    #     ["What are the symptoms of COVID-19?"],
    #     ["Can you help me with chest pain?", "path/to/your/image.jpg"],
    #     ["What should I do in case of a severe headache?"],
    # ],
    examples=[
        ["What are the symptoms of COVID-19?"],
        ["Can you help me with chest pain?", "path/to/your/image.jpg"],
        ["What should I do in case of a severe headache?"],
        ["somehow i managed to hurt my self by fire in the arm ! is it dangerous ? and how can i deal with it ! im no where near a doctor now and i need to calm the pain !"],
        ["ما هي أعراض COVID-19؟"],
        ["ما الذي يجب علي فعله في حالة الصداع الشديد؟"],
        ["استيقظت هذا الصباح وشعرت أن الغرفة بأكملها تدور عندما كنت جالساً. ذهبت إلى الحمام وكنت أسير بشكل غير مستقر، وعندما حاولت التركيز، شعرت بالغثيان. حاولت التقيؤ ولكنه لم يخرج. بعد تناول بانادول والنوم لبضع ساعات، ما زلت أشعر بنفس الشعور. بالمناسبة، عندما أستلقي أو أجلس، لا يدور رأسي، فقط عندما أريد التحرك أشعر بأن العالم بأكمله يدور. وفي نفس الوقت يوجد عندي اضطراب في المعدة العادي؟ في وقت سابق بعد التخلص من الفضلات، تخفَّفت الدوران قليلاً، لذلك لست متأكداً ما إذا كان ذلك متصلاً ببعضه أم مجرد صدفة. شكرًا يا دكتور!"],
        ["ابني البالغ من العمر 5 أشهر يعاني من احتقان شديد مع سعال فظيع. صوت السعال متدحرج وعجزي. بدأ بالاختناق بسبب السعالات والمخاط الذي يخرج. لديه أيضًا حمى وسيلان الأنف. هل يجب أن أأخذه إلى الرعاية الطبية العاجلة؟"],
        ["زوجي يتناول أوكسيكودون بسبب كسر في ساقه / جراحة. يتناول هذا الدواء للألم منذ شهر واحد. نحن نحاول الحمل بطفلنا الثاني. هل سيؤثر هذا الدواء على الجنين؟ أو على صحة الطفل؟ أو قد يسبب تشوهات خلقية؟ شكرًا لك."],
        ["توجد كتلة أسفل الحلمة اليسرى وألم في المعدة (ذكر). لقد لاحظت مؤخرًا منذ بضعة أسابيع وجود كتلة أسفل حلمتي، وتؤلم عند لمسها وحجمها حوالي حجم الدولار الأمريكي. أيضًا، لقد عانيت من آلام في المعدة تمنعني من تناول الطعام. أشعر بالشبع الفوري وأعاني من آلام شديدة. من فضلك ساعدني."],
        ["ابني البالغ من العمر 9 سنوات كان لديه سعال وأعراض نزلة البرد منذ ثلاثة أشهر، ولا يزال السعال يبدو وكأنه يأتي من الصدر والبلغم الأخضر لا يزال موجودًا. بدا الأمر أفضل لكنه لم يذهب تمامًا وعاد الآن... لم يتعرض للمضادات الحيوية إلا مرة واحدة في حياته، مما يشير إلى أنه عموماً بصحة جيدة ونشيط... ولا يعاني من ضيق التنفس أو الزكام... لذا لماذا يحدث هذا؟"],
        ["زوجي كان يعمل في مشروع داخل المنزل وفجأة ظهرت انتفاخة بحجم نصف درهم على ساقه اليسرى أسفل الركبة. يبلغ من العمر 69 عامًا وأجرى عملية تجاوز ثلاثية منذ 7 سنوات. كان يحك عندما حدثت لأول مرة. لا يؤلمه الآن وهو جالس مع رفع ساقه. هل هذا حالة طارئة؟"],
        ["ما هو سبب استمرار وجود السعال الصدري والبلغم الأخضر لدى ابني البالغ من العمر 5 أشهر لمدة ثلاثة أشهر؟ هل يجب أن أأخذه إلى الرعاية الطبية العاجلة؟"],
    ],
    title="FastResQ - Your AI Medical Assistant",
    description="Welcome to FastResQ! Ask your medical questions and express your concerns.",
    theme="compact",
)

# Launch the chatbot interface
iface.launch(share=True)


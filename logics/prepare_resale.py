from crewai_tools import ScrapeWebsiteTool,  FileWriterTool
import os, time, random, json

from crewai_tools import  FileReadTool
from crewai import Agent, Task, Crew
import json, os, random

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI

from pathlib import Path

FOLDER_1 = 'data'
FOLDER_2= 'resale'

#interesting steps for windws/linux fun
def do_folder():

    current_directory = Path(__file__).resolve()
    # Parent directory
    parent_directory = current_directory.parent.parent

    # # Get the directory of the current script
    # base_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(parent_directory, FOLDER_1 )

    index_directory =  os.path.join(directory, FOLDER_2+".index" )

    directory = os.path.join(directory, FOLDER_2 )

    return (directory, index_directory )






def scrape(url):
    print(url)
    #Initialize the tool, potentially passing the session
    tool = ScrapeWebsiteTool(website_url=url)  
    text = tool.run()
    return (text)

#simaple crew to extract useful info only
def gen_resale(txt):

    agent_extract = Agent(
        role='Senior HDB policy officer',
        goal=f'To extract information specifically related to the buying procedure for new HDB flats.',
        backstory=f'''As an experienced HDB policy officer well-versed in the buying procedure for resaleHDB flats, you are provided with text scraped from the HDB public webpage below.
        {txt}
        ''',
        verbose=True,
        allow_delegation=False,
        # memory = True,       
    )

    task_extract= Task(
       description="Extract ALL relevant information regarding the buying procedure for resale HDB flats from the provided text.",
        agent= agent_extract,
        expected_output="All relevant information related to the purchase of resale HDB flats from the provided text. "
        
    )

    crew = Crew(
        agents=[agent_extract],
        tasks=[task_extract]
    )

    crew.kickoff()

    task_output =   task_extract.output

    print(f"Task Description: {task_output.description}")
    print(f"Task Summary: {task_output.summary}")
    print(f"Raw Output: {task_output.raw}")

    # if task_output.json_dict:
    #     print(f"JSON Output: {json.dumps(task_output.json_dict, indent=2)}")
    # if task_output.pydantic:
    #     print(f"Pydantic Output: {task_output.pydantic}")

    # try:
    #     o = json.loads(task_output.raw ) 
    # except:
    #     o = gen_quiz(txt)
    return task_output.raw
    




def all_urls():
    urls = ['https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/conditions-after-buying', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/application-for-an-hdb-flat-eligibility-hfe-letter', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/ability-to-pay', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/budget-for-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/credit-to-finance-a-flat-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/design-features-for-new-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/standard-plus-and-prime-housing-models', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/resale-seminars', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/my-nice-home-gallery', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/timeline', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/modes-of-sale', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/booking-of-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/sign-agreement-for-lease', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/key-collection', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/overview', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-completion', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/eligibility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/cpf-housing-grants', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/buying-procedures', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/conditions-after-buying-for-ec', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/conditions-after-buying', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/seniors', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-hdb', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-financial-institutions', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/application-for-an-hdb-flat-eligibility-hfe-letter/income-guidelines', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/application-for-an-hdb-flat-eligibility-hfe-letter', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/ability-to-pay', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/budget-for-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/credit-to-finance-a-flat-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/timeline/plan-your-finances', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/mode-of-financing', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats/community-care-apartments', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats/Short-lease-2-room-Flexi-Flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/design-features-for-new-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/standard-plus-and-prime-housing-models', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/resale-seminars', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/timeline', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/modes-of-sale/faqs-for-sales-launch', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application/priority-schemes', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application/fresh-start-housing-scheme', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/modes-of-sale', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/booking-of-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/sign-agreement-for-lease', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/key-collection', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/overview', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/option-to-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/request-for-value', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/acceptance-and-approval', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/request-for-enhanced-contra-facility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/managing-the-flat-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-completion', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/eligibility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/cpf-housing-grants', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/buying-procedures', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/conditions-after-buying-for-ec', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/enhanced-cpf-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/cpf-housing-grants-for-resale-flats-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/step-up-cpf-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/proximity-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/enhanced-cpf-housing-grant-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/cpf-housing-grant-for-resale-flats-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/proximity-housing-grant-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/seniors', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-hdb', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-financial-institutions', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/application-for-an-hdb-flat-eligibility-hfe-letter/income-guidelines', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/timeline/plan-your-finances', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/eip-spr-quota', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/conversion-scheme-application-procedure', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/mode-of-financing', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats/community-care-apartments', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats/Short-lease-2-room-Flexi-Flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/modes-of-sale/faqs-for-sales-launch', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application/priority-schemes', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application/fresh-start-housing-scheme', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/option-to-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/request-for-value', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/acceptance-and-approval', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/request-for-enhanced-contra-facility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/managing-the-flat-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/enhanced-cpf-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/cpf-housing-grants-for-resale-flats-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/step-up-cpf-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/proximity-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/enhanced-cpf-housing-grant-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/cpf-housing-grant-for-resale-flats-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/proximity-housing-grant-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/eip-spr-quota', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/conversion-scheme-application-procedure']
    urls = list(set(urls))
    urls.sort()
    return urls




#scarpnig resale pages
def write_resale(urls, folder):

    print(len(urls))

    for url in urls:
        #Initialize the tool, potentially passing the session
        time.sleep(6+ random.randint(6, 9 ) )
        text = gen_resale ( scrape(url)  )
        

    
        f_name = url[-60:].replace("/", "_")+".txt"

        f_path = os.path.join('data/'+folder, f_name)

    
        # print(text)

        # with open(f_path , 'w', encoding='utf-8') as f:
        # with open(f_path , 'w',encoding="cp437", errors='ignore') as f:
        with open(f_path , 'w',encoding='utf-8', errors='ignore') as f:
            f.write(text)

##index resale folder and persist to resale.index folder
def index_resale():

    # f_path = os.path.join('data/', folder)
    # f_index = os.path.join('data/', folder+".index")
    f_path, f_index = do_folder()

    print( [f_path, f_index])

    # Load documents 
    documents = SimpleDirectoryReader(f_path).load_data()

    Settings.llm = OpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    system_prompt="""You are a senior HDB officer .
    You are here to answer any question related to "buying procedure for  resale flat"
    If the question is not related to "buying procedure for  resale flat", you will notify the user politely that the question is not within your scope.
    If you are not able to find answer within your knowledge base for question related to "buying procedure for resale flat", please ask user to leave his/her contact for human officer to follow up.""",
    )
    # Create an index 
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(f_index)


def load_index():
    # f_path = os.path.join('data/', folder)
    # f_index = os.path.join('data/', folder+".index")

    f_path, f_index = do_folder()

    print( [f_path, f_index])

    # Rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir=f_index )
    try:
        index = load_index_from_storage(storage_context)
        return  index
    except Exception as  e:
        print("exception: {e}" )

def load_chat():

    Settings.llm = OpenAI(
        model="gpt-4o-mini",
        temperature=0.1,
        system_prompt="""You are a senior HDB officer .
        You are here to answer any question related to "buying procedure for resale flat"
        If the question is not related to "buying procedure for resale flat", you will notify the user politely that the question is not within your scope.
        If you are not able to find answer within your knowledge base for question related to "buying procedure for resale flat", please ask user to leave his/her contact for human officer to follow up.""",
    )
    index = load_index()

    return index.as_chat_engine(
        chat_mode="condense_plus_context", verbose=True, streaming=True
    )



if __name__ == "__main__":
    # index_resale()
    load_chat()
    # print(do_folder() ) 



##topics
# understanding-your-eligibility-and-housing-loan-options
# buying-procedure-for-resale-flats
# buying-procedure-for-new-flats
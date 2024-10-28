from crewai_tools import ScrapeWebsiteTool,  FileWriterTool
import os, time, random, json

from crewai_tools import  FileReadTool, LlamaIndexTool
from crewai import Agent, Task, Crew
import json, os, random

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI

# from llama_index.core.tools import QueryPlanTool, QueryEngineTool, 


def scrape(url):
    print(url)
    #Initialize the tool, potentially passing the session
    tool = ScrapeWebsiteTool(website_url=url)  
    text = tool.run()
    return (text)




def all_urls():
    urls = ['https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/conditions-after-buying', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/application-for-an-hdb-flat-eligibility-hfe-letter', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/ability-to-pay', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/budget-for-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/credit-to-finance-a-flat-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/design-features-for-new-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/standard-plus-and-prime-housing-models', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/resale-seminars', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/my-nice-home-gallery', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/timeline', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/modes-of-sale', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/booking-of-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/sign-agreement-for-lease', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/key-collection', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/overview', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-completion', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/eligibility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/cpf-housing-grants', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/buying-procedures', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/conditions-after-buying-for-ec', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/conditions-after-buying', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/seniors', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-hdb', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-financial-institutions', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/application-for-an-hdb-flat-eligibility-hfe-letter/income-guidelines', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/application-for-an-hdb-flat-eligibility-hfe-letter', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/ability-to-pay', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/budget-for-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/working-out-your-flat-budget/credit-to-finance-a-flat-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/timeline/plan-your-finances', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/mode-of-financing', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats/community-care-apartments', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats/Short-lease-2-room-Flexi-Flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/design-features-for-new-flats', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/standard-plus-and-prime-housing-models', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/resale-seminars', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/timeline', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/modes-of-sale/faqs-for-sales-launch', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application/priority-schemes', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application/fresh-start-housing-scheme', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/modes-of-sale', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/booking-of-flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/sign-agreement-for-lease', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/key-collection', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/overview', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/option-to-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/request-for-value', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/acceptance-and-approval', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/request-for-enhanced-contra-facility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/managing-the-flat-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-completion', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/eligibility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/cpf-housing-grants', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/buying-procedures', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/executive-condominium/conditions-after-buying-for-ec', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/enhanced-cpf-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/cpf-housing-grants-for-resale-flats-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/step-up-cpf-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/proximity-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/enhanced-cpf-housing-grant-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/cpf-housing-grant-for-resale-flats-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/proximity-housing-grant-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/seniors', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-hdb', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/housing-loan-options/housing-loan-from-financial-institutions', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/application-for-an-hdb-flat-eligibility-hfe-letter/income-guidelines', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/timeline/plan-your-finances', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/eip-spr-quota', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/conversion-scheme-application-procedure', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/mode-of-financing', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats/community-care-apartments', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/finding-a-flat/types-of-flats/Short-lease-2-room-Flexi-Flat', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/modes-of-sale/faqs-for-sales-launch', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application/priority-schemes', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-new-flats/application/fresh-start-housing-scheme', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/option-to-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/request-for-value', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/application', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/acceptance-and-approval', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-application/request-for-enhanced-contra-facility', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/managing-the-flat-purchase', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/enhanced-cpf-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/cpf-housing-grants-for-resale-flats-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/step-up-cpf-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families/proximity-housing-grant-families', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/enhanced-cpf-housing-grant-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/cpf-housing-grant-for-resale-flats-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/singles/proximity-housing-grant-singles', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/eip-spr-quota', 'https://hdb.gov.sg/cs/infoweb/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/conversion-scheme-application-procedure']
    urls = list(set(urls))
    urls.sort()
    return urls


def index_elig(folder):
    f_path = os.path.join('data/', folder)
    f_index = os.path.join('data/', folder+".index")

    print( [f_path, f_index])

    # Load documents 
    documents = SimpleDirectoryReader(f_path).load_data()

    Settings.llm = OpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    system_prompt="""You are a senior HDB officer .
    You are here to answer any question related to "eligibility for HDB flats and housing loan options"
    If the question is not related to "eligibility for HDB flats and housing loan options", you will notify the user politely that the question is not within your scope.
    If you are not able to find answer within your knowledge base for question related to "eligibility for HDB flats and housing loan options", please ask user to leave his/her contact for human officer to follow up.""",
    )
    # Create an index 
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(f_index)


    # simple query test
    # query_engine = index.as_query_engine()
    # response = query_engine.query("What is procedure for resale flats?")
    # print(response)

def load_index(folder):
    f_path = os.path.join('data/', folder)
    f_index = os.path.join('data/', folder+".index")

    print( [f_path, f_index])

    # Rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir=f_index )
    try:
        # Load index from the storage context
        index = load_index_from_storage(storage_context)
        return  index
        # simple query test
        # query_engine = index.as_query_engine()
        # response = query_engine.query("What is procedure for resale flats?")
        # print(response)
    except Exception as  e:
        print("exception: {e}" )

def load_chat():

    Settings.llm = OpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    system_prompt="""You are a senior HDB officer .
    You are here to answer any question related to "eligibility for HDB flats and housing loan options"
    If the question is not related to "eligibility for HDB flats and housing loan options", you will notify the user politely that the question is not within your scope.
    If you are not able to find answer within your knowledge base for question related to "eligibility for HDB flats and housing loan options", please ask user to leave his/her contact for human officer to follow up.""",
    )
    index = load_index('eligibility')

    return index.as_chat_engine(
        chat_mode="condense_plus_context", verbose=True, streaming=True
    )

def load_query():

    Settings.llm = OpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    system_prompt="""You are a senior HDB officer .
    You are here to answer any question related to "eligibility for HDB flats and housing loan options"
    If the question is not related to "eligibility for HDB flats and housing loan options", you will notify the user politely that the question is not within your scope.
    If you are not able to find answer within your knowledge base for question related to "eligibility for HDB flats and housing loan options", please ask user to leave his/her contact for human officer to follow up.""",
    )
    index = load_index('eligibility')
    return  index.as_query_engine(similarity_top_k=5, llm = Settings.llm )

def load_query_tool():
    query_engine = load_query()
    return  LlamaIndexTool.from_query_engine(
        query_engine,
        name="tools for eligibility and housing loan options ",
        description="Use this tool to lookup eligibility and housing loan options",)



if __name__ == "__main__":
    pass
    # urls = all_urls()

    # new = list(filter(lambda x: x.find("buying-procedure-for-new-flats") >= 0 , urls))
    # resale = list(filter(lambda x: x.find("buying-procedure-for-resale-flats") >= 0 , urls))
    # eligibility = list(filter(lambda x: x.find("understanding-your-eligibility-and-housing-loan-options") >= 0 , urls))

    # write_resale(  resale , "resale")

    # write_quiz(  new , "new")
     
    # index_elig('eligibility')

    # load_index('resale')

    # print(load_query_tool())





# understanding-your-eligibility-and-housing-loan-options
# buying-procedure-for-resale-flats
# buying-procedure-for-new-flats
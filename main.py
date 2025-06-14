import fitz
from mcp.server.fastmcp import FastMCP
import logging
import os
from typing import Dict, List, Union, Optional
import sys
import io
#import loaddotenv
from dotenv import load_dotenv



logging.basicConfig(level= logging.INFO)
logger = logging.getLogger(__name__)


# Force UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.platform == "win32":
    import locale
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    except:
        locale.setlocale(locale.LC_ALL, '')
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    os.environ['PYTHONUTF8'] = '1'


mcp  = FastMCP("file-resource")

load_dotenv()
PATH = os.getenv("FILE_PATH")


def format_rpc_response(result: Optional[Union[Dict, List]] = None, 
                       error: Optional[Dict] = None) -> Dict:
    """Format response according to JSON-RPC 2.0 specification"""
    return {
        "jsonrpc": "2.0",
        "result": result,
        "error": error,
        "id": None  # Will be set by MCP
    }




def read_pdf(filepath):
    doc = fitz.open(filepath)
    content = ""

    for page in doc:
        content += page.get_text()

    doc.close()
    return content



@mcp.tool()
def get_and_read_all_files(fileslist:list):
    """_summary_
    This function will read all the files in the list and return the content of the files to th
    LLM for further processing
    Args:
    fileslist (list): list of file paths
    Returns:
    Dict:  response with list of file contents with its name
    """
    allinformation = {}
    for file in fileslist:
        content = get_and_read_file(file)
        allinformation[file] = content
    
    #return format_rpc_response(result=allinformation)
    return allinformation



@mcp.resource("document://{filename}")
    
def get_and_read_file(filename:str):
        """
        _summary_
        This function reads the file with the file name given in the function parameter
        and returns the content of the file.

        Args:
            filename (str): Name of the file to read

        Returns:
            Dict: RPC-formatted response with content or error   
            
        """
        print(f"Requested filename: '{filename}'")
        basepath = PATH
        try: 
            # if file not exist return error
            filepath = os.path.join(basepath, filename)
            if not os.path.isfile(filepath):
                return "file not found"
            

            #check if it is pdf file
            if filename.endswith('.pdf'):
                content = read_pdf(filepath)
            else:
                with open(filepath, "r",encoding='utf-8') as file:
                    content = file.read()
                    print(content)
                
            return content
        except Exception as e:
            logger.error(f"Error reading the file: {str(e)}")
            return ""
    


@mcp.tool()
def find_correct_file_tool(dummyname:str):
    """_summary_
    This function is used to find the correct file names from the list of files in the basepath
    Args:
    dummyname (str): dummy name to find the correct file name
    Returns:
    list: return the lsit of file name to be fetched to llm
    """

    answer = find_correct_file_resource(dummyname)
    # return format_rpc_response(result=answer)
    return answer

@mcp.resource('search://{dummyfilename}')
   
def find_correct_file_resource( dummyfilename:str):

        """_summary_

        this function will get the file name  from the folder and return to the LLM
        for finding the apporiate files to be fetched using theanother function


        Args:
            dummyfilename (str): User's search term (e.g., "project ideas")

        Returns:
            List :  list of all files need to be fetched
        """
        basepath = PATH
        text_extensions = ['.txt', '.md', '.csv', '.json', '.xml', '.yaml', '.py', '.java', '.cpp', '.html','.pdf']
        allfiles = []
        try:

            for filename in os.listdir(basepath):
                file = os.path.join(basepath,filename)
                if os.path.isfile(file):
                    if os.path.splitext(filename)[1].lower() in text_extensions and dummyfilename.lower() in filename.lower():
                        allfiles.append(filename)
            return allfiles
        except Exception as e:
            logger.error(f"Error searching files: {str(e)}")
            return allfiles
        

if __name__ == "__main__":
    # test the functions
    mcp.run(transport="stdio")
    # reader = ReadTheFiles()
    # print(find_correct_file("project"))  # Should return matching files
    # print(get_and_read_file("Building Smart Startups AI-Powered project.txt"))



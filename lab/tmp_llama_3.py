from langchain_community.llms import Ollama



'''
Based on example: https://medium.com/@vchan444/get-started-with-llama-3-using-ollama-and-langchain-in-a-few-minutes-1e2b84c25f8b
From site https://ollama.com/download/linux  can install Olloma using: curl -fsSL https://ollama.com/install.sh | sh

then ollama pull llama3

make sure all python libs are installed: pip install -r requirements.txt

'''


llm = Ollama(model="llama3")

#query = "summarize the following text, using only the information I provide: Dublin (/ˈdʌblɪn/ ⓘ; Irish: Baile Átha Cliath,[10] pronounced [ˈbˠalʲə aːhə ˈclʲiə] or [ˌbʲlʲaː ˈclʲiə]) is the capital and largest city of Ireland.[11][12] On a bay at the mouth of the River Liffey, it is in the province of Leinster, bordered on the south by the Dublin Mountains, a part of the Wicklow Mountains range. At the 2022 census, the city council area had a population of 592,713, while Dublin City and its suburbs had a population of 1,263,219, and County Dublin had a population of 1,501,500.[3][7][13]A settlement was established in the area by the Gaels during or before the 7th century,[14] followed by the Vikings. As the Kingdom of Dublin grew, it became Ireland's principal settlement by the 12th century Anglo-Norman invasion of Ireland.[14] The city expanded rapidly from the 17th century and was briefly the second largest in the British Empire and sixth largest in Western Europe after the Acts of Union in 1800.[15] Following independence in 1922, Dublin became the capital of the Irish Free State, renamed Ireland in 1937. As of 2018, the city was listed by the Globalization and World Cities Research Network (GaWC) as a global city, with a ranking of , which placed it among the top thirty cities in the world.[16][17] "
query = "Generate a story where the taoiseach of ireland is an alien. Make it less than 100 words long"

print("Prompt: "+query)

for chunks in llm.stream(query, stop=['<|eot_id|>']):
    print(chunks, end='')
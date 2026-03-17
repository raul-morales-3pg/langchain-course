UV
$env:Path = "C:\Users\raul.morales\.local\bin;$env:Path"


 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
 .\.venv\Scripts\activate.ps1  


 ollama.com
    Models
        + gpt-oss
        + gemma3

example of model name: 
+ gemma3:270m
+ gpt-oss:20b

commands:
- ollama pull <model_name>
- ollama list
- ollama --help
- ollama run <model_name>


Monitoring 
https://smith.langchain.com/
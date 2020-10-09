### Virtual Personal Assistant

#### Current functionality:

1. If told to '**search youtube <query>**', it will open a remote controlled firefox window with the search in youtube.
The youtube search also happens when told to 'play <query>'.
The same works for wikipedia (but it will not respond to 'play').
To open the search in Google, either 'search google <query>, or simply 'search <query>'.
   
2. Has unique responses to queries 'who are you' and 'who made you'.

3. If told to 'open Chrome', it will open Google Chrome.
The same functionality is available for 'Firefox', 'Word', 'Virtualbox' (virtual machine), 'command prompt', 'control panel', and 'file explorer'.
Handles the case of 'open <application that is not supported>'.
   
4. If told to 'open <website name without the https://www.>', the website is opened.
   
5. If told 'current weather in <city>', it will report the current weather, as well as the maximum and minimum temperatures in celcius, in that city.
Handles the case when the prompted location is not a city.
   
6. If told 'time', it will report the current time on the user's system.
   
7. If told 'hello', the system will respond with the proper time of day (morning, afternoon, evening).
   
8. If asked for 'news' or 'news for today', the headings of the top 15 news articles from Google's RSS feed are read.
   
9. When asked to 'tell me about <anything>', the first 1000 characters of the associated Wikipedia article are read.
   
10. If the prompt cannot be interpreted as above, then the assistant offers to search for it on Google.
   
11. At any point, the user can tell the computer to 'exit','sleep', or 'bye' to end the program.
The impolite alternative is to say 'be quiet computer', or 'computer be quiet', forcing an apology from the machine.

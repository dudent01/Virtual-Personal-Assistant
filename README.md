### Virtual Personal Assistant

#### Interacting with the program

Run the Basic Virtual Assistant script inside the Virtual Assistant directory.<br>
Communicate with the script by clearly speaking with the machine.

#### Current functionality:

1. If told to '**search youtube SOMETHING**', it will open a remote controlled firefox window with the search in youtube.
The youtube search also happens when told to '**play SOMETHING**'.
The same works for wikipedia - '**search wikipedia SOMETHING**' (but it will not respond to '**play**').
To open the search in Google, either '**search google SOMETHING**', or simply '**search SOMETHING**'.
   
2. Has unique responses to queries '**who are you**' and '**who made you**'.

3. If told to '**open Chrome**', it will open Google Chrome.
The same functionality is available for ***Firefox***, ***Word***, ***Virtualbox*** (virtual machine), ***command prompt***, ***control panel***, and ***file explorer***.
Gracefully handles the case of '**open APPLICATION_THAT_IS_NOT_SUPPORTED**'.
   
4. If told to '**open (website name without the https://www.)**', the website is opened.
   
5. If told '**current weather in CITY**' or '**weather in CITY**', it will report the current weather, as well as the maximum and minimum temperatures in celcius, in that city.
Handles the case when the prompted location is not a city.
   
6. If told '**time**', it will report the current time on the user's system.
   
7. If told '**hello**', the system will respond with the proper time of day (morning, afternoon, evening).
   
8. If asked for '**news**' or '**news for today**' or '**what's happening**', the headings of the top 15 news articles from Google's RSS feed are read.
   
9. When asked to '**tell me about SOMETHING**', the first 1000 characters of the associated Wikipedia article are read (the last sentence is finished).
   
10. If the prompt cannot be interpreted as above, then the assistant offers to search for it on Google.
   
11. At any point, the user can tell the computer to '**exit**','**sleep**', or '**bye**' to end the program.
The impolite alternative is to say '**be quiet computer**', or '**computer be quiet**', forcing an apology from the machine.

# JackG619-PROJECT-BRIEF-DTS16103-C1-Practical-Project-Report

What does the code do?

This project is a FIFA 19 database searching application. FIFA 19 is a video game based on real life football, which inludes real life players within the game. Each player has their own individual 'character' which has it's own statistics based on how the player performs in real life. For instance, statistics like sprint speed, agility, standing tackle, and finishing all based on their real life ability.

I retrieved all this information from an open source, in the form of a csv file. This code parses this csv file, processing the data and visualises the results. This answers specific questions, but also gives the user the ability to search through the 'database' to visualise data about their favourite players. FIFA 19 has different game modes, with information relating to the different game modes. This application seperates this information and can display it to the player. Insight into correlation between ability of the player and wage, who the top players are and more niche statistics like what is the tallest height are just some of the interpretations we can produce from the application.

How do you use it?

The introduction and menu sections give brief explanations and pointers of how to use the application. Such as, prompting the player for an input, stating how this will direct them through the application. Or explaining which direction will allow them to do what. 

It is a text based program, so largely surrounds entering values such as 'yes' or 'no', or a certain number - both to signify what the user wants to do. Another input would be a player name, to specify which player's data you want to see.

Possible improvements and future features:
- When searching for some player's with accents, the database has trouble recongnising the name. For instance, the user may input 'Ibrahimovic' when the database entry is 'Ibrahimović'. So the code returns that the player was not found in the database, when in fact they are in the database. This can be worked around by just entering an abbrievated version, for example 'Ibra', and the full name would be returned. However, to improve this, some sort of unicode library feature would need to be implemented, to convert characters into their closest form, as unicode covers most characters.
- Implement a graphical user interface (GUI). This is because with text based applications it is hard to keep track of each element of a project, especially when user           interaction is involved. For example, having a numbered list, which requires the user to enter a number for what they want to do; which is complex and difficult to comprehend.   A GUI would allow me to implement a menu screen, that is user friendly and much more accessible. Clicking on a button would take the user to the desired path. This could also   allow for a drop down menu for player's, rather than having to input the exact name. Overall a GUI would be a welcome improvment to improve readability, accessibility and       make the program more user friendly.
- For the radar chart feature, an improvement would be to be able to compare two player's statistics on the same chart. Such as - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cs.middlebury.edu%2F~candrews%2Fshowcase%2Finfovis_techniques_s16%2Fradar_chart%2F&psig=AOvVaw1nn9vuaAskyVL4M5kcn020&ust=1601314130057000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIC195XuiewCFQAAAAAdAAAAABAD - this would allow people to compare their favourite player's, meaning they could pick the better player.                   The visualisation of this comparison would make things much easier for the user.

CSV file and data source:
- Retrieved from open source - https://data.world/raghav333/fifa-players/workspace/project-summary?agentid=raghav333&datasetid=fifa-players 
- "FIFA PLAYERS dataset"
- "The dataset contains around 18000 fifa players scraped from sofifa.com"
- "It has over 88 features (columns)" 

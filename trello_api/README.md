## Coding to an API

This repository contains a Python program for the Coding to an API portion of the project.

To use this program, you need to get a **Trello API Key and API Token**, which you can retrieve from [here](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

Once you've obtained both of those, navigate to **assets/info.py**, and enter your information in both fields respectively.

Also, you should have **Python** installed on your system, and should have the **requests** library installed. If you don't have *requests* installed, just run this command:

`
python -m pip install requests
`

You can also run this program in .venv, thereby ensuring you're not installing libraries and overloading your storage. You use this link [here](https://docs.python.org/3/library/venv.html) to a learn how to make a .venv.

### Now, you can begin running the application!

To run this application from your CLI, open up your command terminal and navigate to this repository and run the following command:

`
python main.py
`

It will prompt you for **three** things:
- The ID of the column which the card will go to.
- The ID(s) of the labels you want to add to the card.
- The description that will be included in the card.

If you've done the above steps properly, your console should print out the details of the card that was just created.

In the **assets/info.py** file, I've also included a testing column ID, and two testing labels ID's you can use. Feel free to to use those when verifying this solution. (**Note:** You will still need your own API Key and API Token).

The board can be seen here:https://trello.com/b/EMEIXQNv/testing

Also, if you're having trouble accessing/using my board, please feel free to reach out to me, or you can also use your own board.

### Resources used/Thoughts

To develop this CLI program, I've extensively read over this webpage: https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-group-cards

The Atlassian Documentation on their API is quite extensive, and I was able to comprehend what params where needed and what the user would be prompted for.

I did not use any other online resource to write my code, and only did some minor testing using online resources like these: https://reqbin.com/code/python (JSON Testing).

I also tried to account for edge cases, say if the user only enters in some fields and not others, and so my program accounts attempts to prevent total failure, except for not providing a column ID (you need that even run the program)

All in all, this little side project took me two hours to develop, with some time spent on requirements gathering and research on calling the API, and edge case and exception handling.

### Future Development

I've created the project with the correct nomenclature and setup so we can add more API calls to this program, and the Atlassian web-page contains an extensive list of API's to add on. More personally, I'd add Unit Testing to each of these methods to ensure correct behaviour and error catching, and I'd add an API call to create a Board, I think that would really begin to extend the support of this program.
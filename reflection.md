# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The first time I ran it the game looked pretty polished with the streamlit UI. But I noticed a lot of bugs. The first 3 are bugs that I fixed.
1. The hint is backwards, telling you to go lower when the number is actually higher, or higher when the number is actually lower.
2. Pressing the New Game button doesn't reset attempts or history from previous game, and should remove the "You already won" message
3. Pressing enter to submit a guess doesn't work
4. Changing difficulty to Easy mode does not adjust the possible value of the secret.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Copilot.
One AI suggestion that was correct was the refactoring of the backwards hints, as Copilot successfully figured out the bug and created good test cases.
Another AI suggestion that was correct was the testing of the new game button. Copilot successfuly identified that the state status should be set back to playing, even though I didn't notice that. I verified these results by running the pytests I made and re-running the streamlit app.
One AI suggestion that was somewhat misleading was fixing submitting a guess by pressing the Enter button. Copilot did implement the functionality at first by making it into a form, but this also messed up the alignment of the New Game button and the Show Hint Toggle. I resolved this by prompting it again to return the layout to a same line and Copilot did that successfully, with me verifying on Streamlit directly.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided that a bug was really fixed if I was able to run the streamlit app twice with the bug resolved. For submitting a guess by pressing the Enter button, I tested this manually by inputting my guesses and pressing Enter. Copilot taught me that apps that have this functionality use forms in order for the Enter button to submit something, and that using columns is necessary to keep things on the same line.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

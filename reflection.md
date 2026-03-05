# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The first time I ran it the game looked pretty polished with the streamlit UI. But I noticed a lot of bugs:
1. The hint is backwards, telling you to go lower when the number is actually higher, or higher when the number is actually lower.
2. The attempt number doesn't always decrease
3. Pressing enter to submit a guess doesn't work
4. Starting a new game doesn't delete the history from the previous game
5. Starting a new game keeps the "You already won. Start a new game to play again." message and the game fails.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

-Copilot
One AI suggestion that was correct was the refactoring of the backwards hints, as Copilot successfully figured out the bug and created good test cases.
Another AI suggestion that was correct was the testing of the new game button. Copilot successfuly identified that the state status should be set back to playing, even though I didn't notice that. I verified these results by running the pytests I made and re-running the streamlit app.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I decided that a bug was really fixed if I was able to run the streamlit app twice with the bug resolved.
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

# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

# Phase 1, Step 1: 
- Secret was 94, when I inputted 1, the hint showed "Go lower" -> bug
- Normal mode range 1-100, yet hard mode range was 1-50, smaller = easier -> bug
- After clicking new game, I cannot play again -> bug
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

1. used GPT 5.3 Codex
2. Suggested changing 
```python
if guess > secret:
    return "Too High", "📉 Go LOWER!"
else:
    return "Too Low", "📈 Go HIGHER!"
```
which is correct (I just went into the file where the code was and yes, made sense)
3. Honestly none, great model.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

1. By checking the file
2. The test was well-done and passed
3. Yes, by suggesting, generating, and checking
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

1. The secret number kept changing because Streamlit reruns the whole script every time I clicked a button or changed input. In the original version, that meant parts of state got re-initialized at the wrong time, so the game effectively “forgot” the old secret and behaved like a new round. From a player perspective, it felt like the app was cheating, because the target moved after each guess. The bug wasn’t random bad luck, it was state being reset during reruns.

2. I’d explain Streamlit reruns like this: imagine your app is a function that gets executed from top to bottom on every interaction. Buttons, text inputs, checkboxes all trigger that rerun. st.session_state is the one place where you can store values that survive across those reruns, like memory between frames in a game. So reruns are normal behavior, and session state is how you keep things stable and intentional.

3. The key fix was making sure the secret number is initialized only once and then reused from st.session_state. In practice, that means guarding initialization with if "secret" not in st.session_state: and only assigning a new secret when I explicitly start a new game. I also kept new-game resets deliberate (status/history/attempts), so state changes happen only when intended. That’s what made the secret finally stable and the game feel fair.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

1. One habit I want to keep is writing a small regression test right after fixing a bug. It made me feel way more confident that the issue was actually solved and wouldn’t quietly come back later.

2. Next time, I’d ask AI for a quick “why this works” explanation with each code suggestion, not just the fix itself. That would help me learn faster and catch edge cases earlier.

3. This project changed how I see AI-generated code: it’s super helpful for speed, but I still need to verify behavior and test it like any other code. I trust it more as a teammate now, but not as autopilot.
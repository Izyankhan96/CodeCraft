# FunPark.py: Build Plan

This is a step-by-step plan for building **FunPark.py**, a small theme park program that runs in the terminal.
There is **no solution code here on purpose**. Each phase gives you a goal, what "done" looks like, and a few hints. Try each phase on your own before looking anything up.

## The idea

A visitor arrives at the FunPark gate. The program:

1. Asks for their name and greets them.
2. Asks for their age and turns away anyone **under 15**.
3. Asks for the PIN on their prepaid ticket and lets them in only if it is correct.
4. Shows a main menu that keeps coming back until the visitor chooses to leave.

Tickets are prepaid, so there is **no wallet, money, or balance** in this project.

---

## Phase 1: Welcome at the gate

**Goal:** Print a welcome banner and ask for the visitor's name, then greet them by name.

**Done when:**
- Running `python3 FunPark.py` shows a banner with the park's name.
- The visitor types a name and sees a greeting that uses it.

**Hints:**
- `input()` always gives you back a string.
- Think about what should happen if the visitor just presses Enter without typing a name. Can you keep asking until you get something?
- `.strip()` removes extra spaces around what someone typed.

---

## Phase 2: Age check

**Goal:** Ask for the visitor's age. Anyone under 15 is politely refused and the program ends.

**Done when:**
- Age 15 or older moves on to the next step.
- Age 14 or younger sees a friendly "sorry" message and the program stops.
- Typing something that is not a number (like `ten` or `abc`) does **not** crash the program.

**Hints:**
- You will need to turn the text from `input()` into a number.
- Converting text that isn't a number raises an error. Look up `try` / `except` and `ValueError`.
- Be careful with the boundary: is 15 allowed in or not? (It is.) Test 14, 15 and 16.
- Negative numbers or silly ages like 500 are worth thinking about too.

---

## Phase 3: Ticket PIN

**Goal:** Ask for the PIN on the visitor's prepaid ticket. Only a correct PIN gets them through the gate.

**Done when:**
- The correct PIN lets the visitor in.
- A wrong PIN shows a message and lets them try again.
- After **3** wrong tries, the visitor is turned away and the program ends.

**Hints:**
- Store the correct PIN in a variable near the top of the file so it is easy to change.
- Decide whether to compare the PIN as text or as a number. Which one keeps a PIN like `0420` working?
- A loop with a counter is a good way to limit attempts.
- Show how many tries are left after each wrong guess.

---

## Phase 4: Main menu loop

**Goal:** Once inside, show a numbered menu and keep showing it until the visitor picks "Leave the park".

Example options (pick your own if you like):
1. See the rides
2. Get a snack
3. Visit the gift shop
4. Leave the park

**Done when:**
- The menu appears again after each choice.
- Each option prints something fitting.
- Choosing "Leave" says goodbye using the visitor's name and ends the program.
- An invalid choice (like `9` or `hello`) shows a message and the menu comes back, with no crash.

**Hints:**
- A `while` loop that keeps going until a "leave" choice is made fits well here.
- `if` / `elif` / `else` lets you handle each option and the "invalid choice" case.
- Remember the name from Phase 1 so you can use it here.

---

## Phase 5: Tidy up with functions

**Goal:** Split the program into small functions so each part does one job.

**Done when:**
- There is one function per step, for example: welcome, get name, check age, check PIN, main menu.
- A single `main()` function calls them in order.
- The program only starts when the file is run directly.

**Hints:**
- Functions can `return` values (like the name) so other parts can use them.
- Look up `if __name__ == "__main__":` to see why it is used.
- If a function is getting long, that is a sign it could be split.

---

## Phase 6 (optional): Stretch goals

Pick any that sound fun:
- **Ride details:** when the visitor picks "See the rides", show a sub-menu where they choose a ride and get a short description.
- **Ride height or age limits:** some rides need the visitor to be older than 15. Reuse the age you already asked for.
- **Visit summary:** keep a list of everything the visitor did and print it when they leave.
- **Hide the PIN:** look up the `getpass` module so the PIN is not shown while typing.
- **Clear screen** between menus for a cleaner look.

Remember: still no wallet or money, because tickets are prepaid.

---

## Testing checklist

Run the program and try each of these by hand:

- [ ] Empty name
- [ ] Age `14` (refused), `15` (allowed), `16` (allowed)
- [ ] Age `abc` (no crash)
- [ ] Correct PIN on the first try
- [ ] Wrong PIN twice, then correct
- [ ] Wrong PIN three times (turned away)
- [ ] Every menu option
- [ ] Invalid menu choice (`9`, `hello`, empty)
- [ ] Leave the park (goodbye with name)

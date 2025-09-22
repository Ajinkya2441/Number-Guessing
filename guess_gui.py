import random
import dearpygui.dearpygui as dpg

# Game state
target_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts, target_number
    guess = dpg.get_value("input")

    if not guess.isdigit():
        dpg.set_value("result", "❌ Please enter a valid number.")
        return

    guess = int(guess)
    attempts += 1

    if guess < target_number:
        dpg.set_value("result", "🔼 Too low!")
    elif guess > target_number:
        dpg.set_value("result", "🔽 Too high!")
    else:
        dpg.set_value("result", f"🎉 Correct in {attempts} tries!")
        dpg.configure_item("submit_btn", label="🔁 Play Again")
        dpg.set_item_callback("submit_btn", reset_game)

def reset_game():
    global target_number, attempts
    target_number = random.randint(1, 100)
    attempts = 0
    dpg.set_value("input", "")
    dpg.set_value("result", "")
    dpg.configure_item("submit_btn", label="🎯 Submit")
    dpg.set_item_callback("submit_btn", lambda: check_guess())

# --- DPG Setup ---
dpg.create_context()
dpg.create_viewport(title="🎯 Number Guessing Game", width=420, height=350)

with dpg.window(label="", width=400, height=300, pos=(10, 10)):
    dpg.add_text("🔢 Guess a number between 1 and 100", tag="title_text")
    dpg.add_spacer(height=10)

    dpg.add_input_text(
        label="", 
        hint="Enter your guess...", 
        tag="input", 
        width=200, 
        on_enter=True, 
        callback=lambda: check_guess()
    )
    dpg.add_spacer(height=10)

    dpg.add_button(label="🎯 Submit", tag="submit_btn", width=150, callback=lambda: check_guess())
    dpg.add_spacer(height=20)

    dpg.add_text("", tag="result", wrap=350)

# Global dark theme
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (30, 30, 30), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (50, 120, 220), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (70, 150, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (60, 60, 60), category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

from pyscript import document, when #type:ignore
from js import window #type:ignore

# --- 1. Class แม่ ---
class Animal:
    def __init__(self):
        self.sound_text = ""
        self.display_text = ""

    def make_noise(self):
        # สั่งให้ Browser พูด (Speech Synthesis)
        if self.sound_text:
            utterance = window.SpeechSynthesisUtterance.new(self.sound_text)
            utterance.lang = "th-TH" 
            window.speechSynthesis.speak(utterance)
        return self.display_text

# --- 2. Class ลูก ---
class Dog(Animal):
    def __init__(self):
        self.sound_text = "โฮ่ง โฮ่ง โฮ่ง"
        self.display_text = "🐕 สุนัขกำลังเห่า!"

class Cat(Animal):
    def __init__(self):
        self.sound_text = "เมี๊ยว เมี๊ยว"
        self.display_text = "🐈 แมวกำลังร้อง!"

class Duck(Animal):
    def __init__(self):
        self.sound_text = "ก้าบ ก้าบ ก้าบ"
        self.display_text = "🦆 เป็ดกำลังร้องก๊าบๆ!"

class Cow(Animal):
    def __init__(self):
        self.sound_text = "มอออมอออมอออ"
        self.display_text = "🐄 วัวกำลังร้องมออ!"



@when("click", "#btn_sound")
def play_sound(event):
    choice = document.getElementById("animal_selector").value
    animal = None
    
    if choice == "dog": animal = Dog()
    elif choice == "cat": animal = Cat()
    elif choice == "duck": animal = Duck()
    elif choice == "cow": animal = Cow()
    
    if animal:
        text = animal.make_noise()

        document.getElementById("output").innerText = text
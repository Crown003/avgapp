from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
#builder s
helper_string="""
ScreenManager:
	id:sm_manager
	Rules:
	Home:
<Home>:
	name:"mainpage"
	BoxLayout:
		size_hint_y:None 
		height:"820dp"
		orientation:"vertical"
		FitImage:
			source:"New.jpg"
			size_hint:1,None
			height:"820dp"
	MDToolbar:
		title:"Average app"
		pos_hint:{"top":1}
		md_bg_color:1,0,.5,1
	MDLabel:
		text:"WELCOME"
		font_style:"H3"
		halign:"center"
		theme_text_color:"Custom"
		text_color:(1,1,1,1)
		pos_hint:{"center_y":.865}
	MDCard:
		name:"card"
		size_hint:None,None
		height:"600dp"
		width:"400dp"
		md_bg_color:(1,1,1,.2)
		pos_hint:{"top":.80,"center_x":.5}
		GridLayout:
			cols:1
			padding:"25dp"
			spacing:"30dp"
			MDTextField:
				id:num1
				hint_text:"Enter your number"
				size_hint:None,None
				#mode:"rectangle"
				width:"360dp"
				pos_hint:{"center_y":0.4}
				color_mode:"custom"
				line_color_normal:(1,1,1,1)
				line_color_focus:(0,0,1,1)
			MDRaisedButton:
				text:"Convert"
				on_release:
					app.convert()
			MDRaisedButton:
    			text: "Rules"
    			on_release:
    				root.manager.current="rule"
    				root.manager.transition.direction="left"
				
				
			
<Rules>:
	id:rule
	name:"rule"
	MDFloatLayout:
		BoxLayout:
			size_hint_y:None 
			height:"820dp"
			orientation:"vertical"
			FitImage:
				source:"New.jpg"
				size_hint:1,None
				height:"820dp"
		MDCard:
			name:"card"
			size_hint:None,None
			md_bg_color:(0,0,0,.4)
			height:"820dp"
			width:"400dp"
			pos_hint:{"top":1,"center_x":.5}
			radius:(100,100)
		MDLabel:
			text:"HOW TO USE"
			theme_text_color:"Custom"
			text_color:(1,0,.5,1)
			font_style:"H3"
			pos_hint:{"center_y":.95,"x":0.11}
		MDLabel:
			multiline:True
			text:"I - Enter your numbers of which you wants average."
			theme_text_color:"Custom"
			text_color:(1,1,1,1)
			font_style:"Subtitle2"
			pos_hint:{"center_y":.80,"x":0.1/3}
		MDLabel:
			multiline:True
			text:"II - Do not enter any alphabetical character."
			theme_text_color:"Custom"
			text_color:(1,1,1,1)
			font_style:"Subtitle2"
			pos_hint:{"center_y":.77,"x":0.1/3}
		MDLabel:
			multiline:True
			text:"III - Seperate each number by commas ' , ' ."
			theme_text_color:"Custom"
			text_color:(1,1,1,1)
			font_style:"Subtitle2"
			pos_hint:{"center_y":.74,"x":0.1/3}
			
		MDRaisedButton:
			text:"Click to open app"
			text_theme_color:"Custom"
			md_bg_color:(1,1,1,.2)
			text_color:(1,1,1,1)
			pos_hint:{"center_x":.5,"center_y":.25}
			on_press:
				root.manager.current="mainpage"
				root.manager.transition.direction = 'right'
"""

#defining class
class Home(Screen):
	pass

class Rules(Screen):
	pass
	
	
#Adding home page to screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(Home(name="mainpage"))
sm.add_widget(Rules(name="rule"))
	


class Main(MDApp):
	def build(self):
		self.theme_cls.primary_hue="A700"
		self.theme_cls.theme_style="Light"
		screen = Screen()
		self.main_page = Builder.load_string(helper_string)
		screen.add_widget(self.main_page)
		return screen
	def convert(self):
		list1 = [] #an emplty list
		field_text = self.main_page.get_screen("mainpage").ids.num1.text
		list1 = list(field_text.split(","))
		done_btn = MDRaisedButton(text="OK",md_bg_color=[1,0,.5,1])
		if field_text == "":
			dialog = MDDialog(title="Error",text="Please enter some value.",
			buttons=[done_btn],size_hint=[.8,None])
			dialog.open()
		else:
			for i in range(0, len(list1)): 
				list1[i] = int(list1[i])
			average = sum(list1)/len(list1)
			average = round(average,2)
			dialog = MDDialog(title="Your Result",text=f"Your Input Numbers: {list1}\nYour average is {average}",
				buttons=[done_btn],size_hint=[.8,None])
			dialog.open()
	
if __name__ == "__main__":
	Main().run()

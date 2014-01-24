# Written by Magnus Hauge Bakke (mhbakke@gmail.com)

import sublime
import sublime_plugin

import subprocess
import webbrowser

def searchForGoogle(text):
	url = 'https://www.google.no/#q=' + text.replace(' ','%20')
	webbrowser.open_new_tab(url)

def searchForStackoverflow(text):
	url = 'http://stackoverflow.com/search?tab=relevance&q=' + text.replace(' ','%20')
	webbrowser.open_new_tab(url)

def searchForWordpress(text):
	url = 'http://wordpress.org/search/' + text.replace(' ','%20')
	webbrowser.open_new_tab(url)

class GoogleSearchSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for selection in self.view.sel():
			
			if selection.empty():
				text = self.view.word(selection)

			text = self.view.substr(selection)
						
			searchForGoogle(text)

class GoogleSearchFromInputCommand(sublime_plugin.WindowCommand):
	def run(self):
		
		self.window.show_input_panel('Search Google for', '',
			self.on_done, self.on_change, self.on_cancel)
		
	def on_done(self, input):
		searchForGoogle(input)

	def on_change(self, input):
		pass

	def on_cancel(self):
		pass

class StackoverflowSearchSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for selection in self.view.sel():
			
			if selection.empty():
				text = self.view.word(selection)

			text = self.view.substr(selection)
						
			searchForStackoverflow(text)

class StackoverflowSearchFromInputCommand(sublime_plugin.WindowCommand):
	def run(self):
		
		self.window.show_input_panel('Search Stack Overflow for', '',
			self.on_done, self.on_change, self.on_cancel)
		
	def on_done(self, input):
		searchForStackoverflow(input)

	def on_change(self, input):
		pass

	def on_cancel(self):
		pass

class WordpressSearchSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for selection in self.view.sel():
			
			if selection.empty():
				text = self.view.word(selection)

			text = self.view.substr(selection)
						
			searchForWordpress(text)

class WordpressSearchFromInputCommand(sublime_plugin.WindowCommand):
	def run(self):
		
		self.window.show_input_panel('Search WordPress Codex for', '',
			self.on_done, self.on_change, self.on_cancel)
		
	def on_done(self, input):
		searchForWordpress(input)

	def on_change(self, input):
		pass

	def on_cancel(self):
		pass
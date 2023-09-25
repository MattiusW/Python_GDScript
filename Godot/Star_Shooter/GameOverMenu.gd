extends Control

onready var score_label =$Score

func _on_RetryButton_pressed():
	get_tree().change_scene("res://World.tscn")

func _on_BackButton_pressed():
	get_tree().change_scene("res://MainMenu.tscn")

func set_score(val):
	score_label.text = "SCORE: " + str(val)

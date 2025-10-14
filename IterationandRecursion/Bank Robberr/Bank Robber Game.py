import random

def task_check(task_type, difficulty, role, item):
	"""
	task_type: 'strength', 'speed', or 'stealth'
	difficulty: 'normal', 'hard', or 'very hard'
	role: player's chosen role (string)
	item: player's chosen item (string)
	Returns True if player passes, False if fails.
	"""
	# Base fail chances
	if difficulty == 'normal':
		fail_chance = 0.5  # 50% fail
	elif difficulty == 'hard':
		fail_chance = 0.6  # 60% fail
	else:  # very hard
		fail_chance = 0.7  # 70% fail
	# Role bonus: +10% pass for matching stat
	role = role.lower()
	if (role == 'muscle' and task_type == 'strength') or \
	   (role == 'hacker' and task_type == 'stealth') or \
	   (role == 'driver' and task_type == 'speed'):
		fail_chance -= 0.10
	# Item bonus: +20% pass for matching stat
	if (item == 'Sledgehammer' and task_type == 'strength') or \
	   (item == 'Adrenaline Pack' and task_type == 'speed') or \
	   (item == 'Ghost Shoes' and task_type == 'stealth'):
		fail_chance -= 0.20
	# Clamp fail_chance between 0 and 1
	fail_chance = max(0, min(1, fail_chance))
	return random.random() > fail_chance

play_again = True
while play_again:
	print("\nWelcome to Bank Heist Simulator!\n")
	print()
	print("Choose wisely to get away with the money!\n")
	print()
	print("Will you suceed and survive the heist?\n")
	print()
	print("Before we begin, here are the roles you can choose:\n")
	print()
	print("\nThe Muscle: The team's powerhouse, best at breaking through obstacles and handling guards head-on.\n")
	print("The Hacker: The stealthy tech expert, skilled at bypassing security and moving unseen.\n")
	print("The Driver: The getaway specialist, unmatched at fast escapes and quick maneuvers.\n")
	role = input("Choose your role (Hacker, Driver, Muscle): ")
	while role.lower() not in ["hacker", "driver", "muscle"]:
		role = input("Please type Hacker, Driver, or Muscle: ")
	print()
	print(f"You have chosen the role of {role.title()} for this heist!\n")
	print()

	print()
	print("Item Options:\n")
	print()
	print("1. Sledgehammer\n   A heavy tool for smashing through obstacles. Boosts your Strength.\n")
	print("2. Adrenaline Pack\n   A one-time shot of energy for quick moves. Boosts your Speed.\n")
	print("3. Ghost Shoes\n   Silent shoes that let you move without a sound. Boosts your Stealth.\n")
	print()
	print("Choose an item to help you with your mission:\n")
	print("  1. Turn yourself in and surrender to the authorities.")
	print("  2. Try to pry open the vault door while you still have a chance.")
	print("You notice the hacker on your team has already hacked the vault's control panel, disabling the security system. All that's left is brute force!")
	print()
	vault_choice = input("Type 1 to surrender, or 2 to pry open the vault: ")
	print()
	while vault_choice not in ["1", "2"]:
		vault_choice = input("Please type 1 or 2: ")
		print()
	if vault_choice == "1":
		print()
		print("You surrender to the authorities. The heist is over, but at least you are alive.\n")
		print()
	else:
		pry_result = task_check('strength', 'very hard', role, item)
		if pry_result:
			print()
			print("With a mighty effort, you wedge your tool into the vault door and pry it open. The door finally gives way with a sharp, echoing clang. The riches inside are yours—if you can escape!\n")
			print()
			print("You grab as much cash as you can carry. Now you have to escape!")
			print()
			print("How will you make your getaway?")
			print()
			print("  1. Charge straight through the bank's main hall")
			print()
			print("  2. Dodge guards and sprint for the side alley")
			print()
			print("  3. Use the shadows to sneak out unseen")
			print()
			escape_choice = input("Type 1 to charge, 2 to sprint, or 3 to sneak: ")
			print()
			while escape_choice not in ["1", "2", "3"]:
				escape_choice = input("Please type 1, 2, or 3: ")
				print()
			if escape_choice == "1":
				escape_result = task_check('strength', 'hard', role, item)
				if escape_result:
					print()
					print("You lower your shoulder and charge through the main hall, scattering anyone in your way. You burst out the front doors into the chaos outside—you're free, for now!\n")
					print()
					print("You make it to the getaway car with the money, hoping your driver can lose the police in the chase ahead.")
					print()
					# End or next branch
				else:
					print()
					print("You try to charge through, but the guards are ready this time. They tackle you before you can escape. The heist is over.\n")
					print()
			elif escape_choice == "2":
				escape_result = task_check('speed', 'hard', role, item)
				if escape_result:
					print()
					print("You weave and dodge past the guards, sprinting for the side alley. You make it out just as the sirens close in—you're gone before anyone can catch you!\n")
					print()
					print("You make it to the getaway car with the money, hoping your driver can lose the police in the chase ahead.")
					print()
					# End or next branch
				else:
					print()
					print("You try to sprint for the alley, but a guard spots you and brings you down. The heist is over.\n")
					print()
			else:
				escape_result = task_check('stealth', 'very hard', role, item)
				if escape_result:
					print()
					print("Sticking to the shadows, you move silently past the chaos. No one even notices as you slip out a side door and vanish into the night with the loot.\n")
					print()
					print("You make it to the getaway car with the money, hoping your driver can lose the police in the chase ahead.")
					print()
					# End or next branch
				else:
					print()
					print("You try to sneak out, but a flashlight beam catches you at the last second. The guards close in and the heist is over.\n")
					print()
		else:
			print()
			print("You strain with all your strength, but the vault door won't budge. The guards catch up to you and the heist is over.\n")
			print()
else:
rush_result = task_check('speed', 'hard', role, item)
							if rush_result:
								print()
								print("You sprint down the corridor, dodging obstacles and making it to the vault just ahead of the guards.\n")
								print()
								# Arrive at the vault (see above)
								print("You finally reach the vault, heart pounding.")
								print()
								print("You see two options:")
								print()
								print("  1. Turn yourself in and surrender to the authorities.")
								print()
								print("  2. Try to pry open the vault door while you still have a chance.")
								print()
								print("You notice the hacker on your team has already hacked the vault's control panel, disabling the security system. All that's left is brute force!")
								print()
								vault_choice = input("Type 1 to surrender, or 2 to pry open the vault: ")
								print()
								while vault_choice not in ["1", "2"]:
									vault_choice = input("Please type 1 or 2: ")
									print()
								if vault_choice == "1":
									print()
									print("You surrender to the authorities. The heist is over, but at least you are alive.\n")
									print()
								else:
									pry_result = task_check('strength', 'very hard', role, item)
									if pry_result:
										print()
										print("With a mighty effort, you wedge your tool into the vault door and pry it open, the heavy metal groaning as it gives way. The riches inside are yours—if you can escape!\n")
										print()
										# Next story branch: escape
									else:
										print()
										print("You strain with all your strength, but the vault door won't budge. The guards catch up to you and the heist is over.\n")
										print()
							else:
								print()
								print("You try to rush for the vault, but the guards are too quick—they catch you before you can get inside. The heist is over.\n")
								print()
					else:
						print()
						print("You try to fight the guards, but they outnumber you and quickly restrain you. The heist is over.\n")
						print()
				else:
					dodge_result = task_check('speed', 'hard', role, item)
					if dodge_result:
						print()
						print("You dodge past the guards with quick reflexes and make it further into the bank!\n")
						print()
						print("You quickly spot a nearby closet and slip inside, holding your breath as the guards rush past, unaware of your presence.")
						print()
						print("Heart pounding, you scan your surroundings from the darkness of the closet. Time is running out—you must act fast before the guards return.\n")
						print("  1. Crawl through a vent towards the vault (hard stealth)")
						print("  1. Crawl through a vent towards the vault")
						print()
						print("  2. Sprint for the vault while the coast is clear (hard speed)\n")
						print("  2. Sprint for the vault while the coast is clear\n")
						print()
						closet_choice = input("Type 1 to crawl through the vent, or 2 to sprint for the vault: ")
						print()
						while closet_choice not in ["1", "2"]:
							closet_choice = input("Please type 1 or 2: ")
							print()
						if closet_choice == "1":
							vent_result = task_check('stealth', 'hard', role, item)
							vent_result = task_check('stealth', 'hard', role, item)
							if vent_result:
								print()
								print("You quietly crawl through the vent, avoiding all detection, and drop down right outside the vault.\n")
								print()
								# Arrive at the vault (see above)
								print("You finally reach the vault, heart pounding.")
								print()
								print()
								print("  1. Turn yourself in and surrender to the authorities.")
								print()
								print("  2. Try to pry open the vault door while you still have a chance.")
								print()
								print("You notice the hacker on your team has already hacked the vault's control panel, disabling the security system. All that's left is brute force!")
								print()
								vault_choice = input("Type 1 to surrender, or 2 to pry open the vault: ")
								print()
								while vault_choice not in ["1", "2"]:
									vault_choice = input("Please type 1 or 2: ")
									print()
								if vault_choice == "1":
									print()
									print("You drop to the ground and surrender. The authorities take you into custody. The heist is over, but at least you are alive.\n")
									print()
								else:
									pry_result = task_check('strength', 'very hard', role, item)
									if pry_result:
										print()
										print("With a mighty effort, you wedge your tool into the vault door and pry it open, the heavy metal groaning as it gives way. The riches inside are yours—if you can escape!\n")
										print()
										# Next story branch: escape
									else:
										print()
										print("You strain with all your strength, but the vault door won't budge. The guards catch up to you and the heist is over.\n")
										print()
							else:
								print()
								print("You try to crawl through the vent, but make too much noise. An alarm sounds and guards rush to your location. The heist is over.\n")
								print()
						else:
							sprint_result = task_check('speed', 'hard', role, item)
							sprint_result = task_check('speed', 'hard', role, item)
							if sprint_result:
								print()
								print("You burst from the closet and sprint for the vault, making it just in time before anyone notices.\n")
								print()
								# Next story branch can go here
							else:
								print()
								print("You try to sprint for the vault, but a guard spots you and tackles you before you get there. The heist is over.\n")
								print()
					else:
						print()
						print("You try to dodge the guards, but one grabs you and you are taken down. The heist is over.\n")
						print()
			else:
				print()
				print("You try to charge the front door, but the alarm sounds and the guards quickly take you to the ground before you get any further.\n")
				print()
		else:
			passed = task_check('stealth', 'normal', role, item)
			if passed:
				print()
				print("You sneak to the side entrance and crouch in the shadows, looking for a way in.\n")
				print()
				print("How do you want to get inside?")
				print()
				print("  1. Kick open the door")
				print()
				print("  2. Pick the lock quietly")
				print()
				side_entry_choice = input("Type 1 to kick the door, or 2 to pick the lock: ")
				print()
				while side_entry_choice not in ["1", "2"]:
					side_entry_choice = input("Please type 1 or 2: ")
					print()
				if side_entry_choice == "1":
					kick_result = task_check('strength', 'normal', role, item)
					if kick_result:
						print()
						print("You kick the door open with a loud crash and rush inside before anyone can react.\n")
						print()
						print("Once inside, you have to act fast. What do you do?")
						print()
						print("  1. Power through any guards in your way")
						print()
						print("  2. Sprint towards the vault as fast as you can")
						print()
						print("  3. Hide in a nearby janitor's closet")
						print()
						side_in_bank_choice = input("Type 1 to power through, 2 to sprint, or 3 to hide: ")
						print()
						while side_in_bank_choice not in ["1", "2", "3"]:
							side_in_bank_choice = input("Please type 1, 2, or 3: ")
							print()
						if side_in_bank_choice == "1":
							power_result = task_check('strength', 'hard', role, item)
							if power_result:
								print()
								print("You charge forward, knocking aside any guards in your path and make your way deeper into the bank!\n")
								print()
								# Arrive at the vault
								print("You finally reach the vault, heart pounding.")
								print()
								print("  1. Turn yourself in and surrender to the authorities.")
								print()
								print("  2. Try to pry open the vault door while you still have a chance.")
								print()
								print("You notice the hacker on your team has already hacked the vault's control panel, disabling the security system. All that's left is brute force!")
								print()
								vault_choice = input("Type 1 to surrender, or 2 to pry open the vault: ")
								print()
								while vault_choice not in ["1", "2"]:
									vault_choice = input("Please type 1 or 2: ")
									print()
								if vault_choice == "1":
									print()
									print("You surrender to the authorities. The heist is over, but at least you are alive.\n")
									print()
								else:
									pry_result = task_check('strength', 'very hard', role, item)
									if pry_result:
										print()
										print("With a mighty effort, you wedge your tool into the vault door and pry it open. The door finally gives way with a sharp, echoing clang. The riches inside are yours—if you can escape!\n")
										print()
										print("You grab as much cash as you can carry. Now you have to escape!")
										print()
										print("How will you make your getaway?")
										print()
										print("  1. Charge straight through the bank's main hall")
										print()
										print("  2. Dodge guards and sprint for the side alley")
										print()
										print("  3. Use the shadows to sneak out unseen")
										print()
										escape_choice = input("Type 1 to charge, 2 to sprint, or 3 to sneak: ")
										print()
										while escape_choice not in ["1", "2", "3"]:
											escape_choice = input("Please type 1, 2, or 3: ")
											print()
										if escape_choice == "1":
											escape_result = task_check('strength', 'hard', role, item)
											if escape_result:
												print()
												print("You lower your shoulder and charge through the main hall, scattering anyone in your way. You burst out the front doors into the chaos outside—you're free, for now!\n")
												print()
												print("You make it to the getaway car with the money, hoping your driver can lose the police in the chase ahead.")
												print()
											else:
												print()
												print("You try to charge through, but the guards are ready this time. They tackle you before you can escape. The heist is over.\n")
												print()
										elif escape_choice == "2":
											escape_result = task_check('speed', 'hard', role, item)
											if escape_result:
												print()
												print("You weave and dodge past the guards, sprinting for the side alley. You make it out just as the sirens close in—you're gone before anyone can catch you!\n")
												print()
												print("You make it to the getaway car with the money, hoping your driver can lose the police in the chase ahead.")
												print()
											else:
												print()
												print("You try to sprint for the alley, but a guard spots you and brings you down. The heist is over.\n")
												print()
										else:
											escape_result = task_check('stealth', 'very hard', role, item)
											if escape_result:
												print()
												print("Sticking to the shadows, you move silently past the chaos. No one even notices as you slip out a side door and vanish into the night with the loot.\n")
												print()
												print("You make it to the getaway car with the money, hoping your driver can lose the police in the chase ahead.")
												print()
											else:
												print()
												print("You try to sneak out, but a flashlight beam catches you at the last second. The guards close in and the heist is over.\n")
												print()
									else:
										print()
										print("You strain with all your strength, but the vault door won't budge. The guards catch up to you and the heist is over.\n")
										print()
							else:
								print()
								print("You try to power through, but the guards overwhelm you. The heist is over.\n")
								print()
						elif side_in_bank_choice == "2":
							sprint_result = task_check('speed', 'hard', role, item)
							if sprint_result:
								print()
								print("You dash past the guards, weaving through the chaos and heading straight for the vault!\n")
								print()
								# Arrive at the vault
								print("You finally reach the vault, heart pounding.")
								print()
								print("  1. Turn yourself in and surrender to the authorities.")
								print()
								print("  2. Try to pry open the vault door while you still have a chance.")
								print()
								print("You notice the hacker on your team has already hacked the vault's control panel, disabling the security system. All that's left is brute force!")
								print()
								vault_choice = input("Type 1 to surrender, or 2 to pry open the vault: ")
								print()
								while vault_choice not in ["1", "2"]:
									vault_choice = input("Please type 1 or 2: ")
									print()
								if vault_choice == "1":
									print()
									print("You surrender to the authorities. The heist is over, but at least you are alive.\n")
									print()
								else:
									pry_result = task_check('strength', 'very hard', role, item)
									if pry_result:
										print()
										print("With a mighty effort, you wedge your tool into the vault door and pry it open. The door finally gives way with a sharp, echoing clang. The riches inside are yours—if you can escape!\n")
										print()
										# Next story branch: escape
									else:
										print()
										print("You strain with all your strength, but the vault door won't budge. The guards catch up to you and the heist is over.\n")
										print()
							else:
								print()
								print("You try to sprint, but a guard intercepts you before you reach the vault. The heist is over.\n")
								print()
						else:
							print()
							print("You slip into the janitor's closet, heart pounding as you listen to the guards rush by.\n")
							print()
							# Connect to closet branch (reuse closet logic from front door)
							print("Heart pounding, you scan your surroundings from the darkness of the closet. Time is running out—you must act fast before the guards return.\n")
							print("  1. Crawl through a vent towards the vault")
							print()
							print("  2. Sprint for the vault while the coast is clear\n")
							print()
							closet_choice = input("Type 1 to crawl through the vent, or 2 to sprint for the vault: ")
							print()
							while closet_choice not in ["1", "2"]:
								closet_choice = input("Please type 1 or 2: ")
								print()
							if closet_choice == "1":
								vent_result = task_check('stealth', 'hard', role, item)
								if vent_result:
									print()
									print("You quietly crawl through the vent, avoiding all detection, and drop down right outside the vault.\n")
									print()
									# Arrive at the vault
								else:
									print()
									print("You try to crawl through the vent, but make too much noise. An alarm sounds and guards rush to your location. The heist is over.\n")
									print()
							else:
								sprint_result = task_check('speed', 'hard', role, item)
								if sprint_result:
									print()
									print("You burst from the closet and sprint for the vault, making it just in time before anyone notices.\n")
									print()
									# Arrive at the vault
								else:
									print()
									print("You try to sprint for the vault, but a guard spots you and tackles you before you get there. The heist is over.\n")
									print()
					else:
						print()
						print("You try to kick the door, but it barely budges and the noise draws a guard. The heist is over.\n")
						print()
				else:
					pick_result = task_check('stealth', 'hard', role, item)
					if pick_result:
						print()
						print("You quietly pick the lock and slip inside unnoticed.\n")
						print()
						print("Once inside, you have to act fast. What do you do?")
						print()
						print("  1. Power through any guards in your way")
						print()
						print("  2. Sprint towards the vault as fast as you can")
						print()
						print("  3. Hide in a nearby janitor's closet")
						print()
						side_in_bank_choice = input("Type 1 to power through, 2 to sprint, or 3 to hide: ")
						print()
						while side_in_bank_choice not in ["1", "2", "3"]:
							side_in_bank_choice = input("Please type 1, 2, or 3: ")
							print()
						if side_in_bank_choice == "1":
							power_result = task_check('strength', 'hard', role, item)
							if power_result:
								print()
								print("You charge forward, knocking aside any guards in your path and making your way deeper into the bank!\n")
								print()
								# Continue to vault or next branch
							else:
								print()
								print("You try to power through, but the guards overwhelm you. The heist is over.\n")
								print()
						elif side_in_bank_choice == "2":
							sprint_result = task_check('speed', 'hard', role, item)
							if sprint_result:
								print()
								print("You dash past the guards, weaving through the chaos and heading straight for the vault!\n")
								print()
								# Arrive at the vault
								print("You finally reach the vault, heart pounding.")
								print()
								print("  1. Turn yourself in and surrender to the authorities.")
								print()
								print("  2. Try to pry open the vault door while you still have a chance.")
								print()
								print("You notice the hacker on your team has already hacked the vault's control panel, disabling the security system. All that's left is brute force!")
								print()
								vault_choice = input("Type 1 to surrender, or 2 to pry open the vault: ")
								print()
								while vault_choice not in ["1", "2"]:
									vault_choice = input("Please type 1 or 2: ")
									print()
								if vault_choice == "1":
									print()
									print("You surrender to the authorities. The heist is over, but at least you are alive.\n")
									print()
								else:
									pry_result = task_check('strength', 'very hard', role, item)
									if pry_result:
										print()
										print("With a mighty effort, you wedge your tool into the vault door and pry it open. The door finally gives way with a sharp, echoing clang. The riches inside are yours—if you can escape!\n")
										print()
										# Next story branch: escape
									else:
										print()
										print("You strain with all your strength, but the vault door won't budge. The guards catch up to you and the heist is over.\n")
										print()
							else:
								print()
								print("You try to sprint, but a guard intercepts you before you reach the vault. The heist is over.\n")
								print()
						else:
							print()
							print("You slip into the janitor's closet, heart pounding as you listen to the guards rush by.\n")
							print()
							# Connect to closet branch (reuse closet logic from front door)
							print("Heart pounding, you scan your surroundings from the darkness of the closet. Time is running out—you must act fast before the guards return.\n")
							print("  1. Crawl through a vent towards the vault")
							print()
							print("  2. Sprint for the vault while the coast is clear\n")
							print()
							closet_choice = input("Type 1 to crawl through the vent, or 2 to sprint for the vault: ")
							print()
							while closet_choice not in ["1", "2"]:
								closet_choice = input("Please type 1 or 2: ")
								print()
							if closet_choice == "1":
								vent_result = task_check('stealth', 'hard', role, item)
								if vent_result:
									print()
									print("You quietly crawl through the vent, avoiding all detection, and drop down right outside the vault.\n")
									print()
									# Arrive at the vault
								else:
									print()
									print("You try to crawl through the vent, but make too much noise. An alarm sounds and guards rush to your location. The heist is over.\n")
									print()
							else:
								sprint_result = task_check('speed', 'hard', role, item)
								if sprint_result:
									print()
									print("You burst from the closet and sprint for the vault, making it just in time before anyone notices.\n")
									print()
									# Arrive at the vault
								else:
									print()
									print("You try to sprint for the vault, but a guard spots you and tackles you before you get there. The heist is over.\n")
									print()
					else:
						print()
						print("You fumble with the lock, making too much noise. A guard hears you and catches you before you can get inside. The heist is over.\n")
						print()
			else:
				print()
				print("You try to sneak into the side entrance, but a guard spots you and quickly catches you before you can get inside.\n")
				print()

	# ...other storylines for Hacker/Driver can go here...


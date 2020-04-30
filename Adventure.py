import time
start = time.time()
print "You enter a dark room with four doors. Choose a door: 1, 2, 3, 4\n"

door = raw_input("> ")

if door == "1":
    print "\nThere's a giant bear masturbating in here. What do you do?\n"
    print "1. Join.\n"
    print "2. Scream at the bear 'I'M CALLING BOSHO.' (BOSHO stands for 'Bears Often Stay Home Often.'\nIt's a news organization specializing in the habits of grizzly bears framed in a quirky yet sensible context.)\n"
    print "3. Dance the bubble toss.\n"
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "\nYou are immediately destroyed. Due to the bear's shame. Its family must never know.\n"
        
    elif bear == "2":
        print "\nThe bear screams back, 'Ok, call them! I'm friends with BOSHO administrator Peter Bear.' You shrink away in defeat. I'm sorry.\n"
        
    elif bear == "3":
        print "\nThe bear is mesmorized by your bubble toss skills. So impressed,\nin fact, that it kills you. The end. You just lost. How does that feel? Don't dance the bubble toss.\n" 
        
elif door == "2":
    print "\nYou walk into a living LSD trip.\n"
    print "1. I Am The One Who Speaks And Delivers All.\n"
    print "2. Yellow was pretty once.\n"
    print "3. The silent songs are louder than the screaming fiends.\n"
    
    insanity = raw_input("> ")
    
    if insanity == "1":
        print "\nTurn off your mind, relax and float down stream"
        print "It is not dying, it is not dying"
        print "Lay down all thoughts, surrender to the void"
        print "It is shining, it is shining"
        print "\nYet you may see the meaning of within"
        print "It is being, it is being"
        print "Love is all and love is everyone"
        print "It is knowing, it is knowing"
        print "\nAnd ignorance and hate mourn the dead"
        print "It is believing, it is believing"
        print "But listen to the colour of your dreams"
        print "It is not leaving, it is not leaving"
        print "\nSo play the game 'Existence' to the end"
        print "Of the beginning, of the beginning"
        print "Of the beginning, of the beginning"
        print "Of the beginning, of the beginning"
        print "Of the beginning, of the beginning\n"
        
    elif insanity == "2":
        print "\nThe sky goes all the way over there.\n"
        print "Can you see it?\n"
        print "1. Yes.\n"
        print "2. The sky is like the world's strongest shield.\n"
        
        sky = raw_input("> ")
        
        if sky == "1":
            count = 0
            while count <= 40000:
                print "I "
                print "\tCan "
                print "\t\tSee "
                print "\t\t\tIt"
                count += 1
                
        else:
            print "\nStairs bring me to point B. They serve no other purpose."
            print "You were at point A. You required the use of stairs."
            print "For just a moment."
            print "Stairs connect the world."
            print "\t~haiku\n"
                    
    else:
        print "\nThe air gives way to more air. You breathe it in. Are you hot or cold?\n"
        print "1. Hot.\n"
        print "2. Cold.\n"
        
        temp = raw_input("> ")
        
        if temp == "1":
            print "\nYou have fallen through the floor into the flames of fire. Sorry about that but"
            print "you know how it is. Play with fire and you're going to get burned. That's like Fire Class 101. \nSorry."
            print "No seriously."
            print "You're done."
            print "The end.\n"
        
        else:
            for i in range(100):
                print "We are counting to", i
            print "Red armies of light converge on the edge.\n"              
        
elif door == "3":
    print "\nYou see a man attempting to put himself inside his Dropbox folder.\n"
    print "1. Delete his Dropbox folder.\n"
    print "2. Create a new Dropbox account so that his requires an additional login.\n"
    print "3. Blow apart his world by syncing your own Dropbox folder.\n"
    
    dropbox = raw_input("> ")
    
    if dropbox == "1":
        print "\nThe man becomes enraged and reformats himself. Dropbox, inc. is contacted"
        print " and they begin legal proceedings that investigate the circumstances of the situation.\n"
        print "How do you plead?\n"
        print "1. Guilty.\n"
        print "2. Not guilty, but secretly pleased the reformat took place.\n"
        print "3. Not guilty, and visibly upset that you were not able to sync your own \npublic folder before the loss of data occurred.\n"
        
        verdict = raw_input("> ")
        
        if verdict == "1":
            print "\nYou are punched in the face. Sorry, that is the punishment in this land of wonders.\n"
            
        elif verdict == "2":
            print "\nThomas Biggles-Ruptureton, CEO of Whatever Town, notices your secret pleasure"
            print " and slides up next to you. He slips a knife into your side and whispers 'yeeeeeeahhhhhh' loudly. Don't underestimate Thomas Biggles-Ruptureton.\n"
            
        else:
            print "\nThe court rules there are insufficient funds left in their account. Thank "
            print "you for playing and close the door that led you here. There is a draft and the CEO of Whatever Town "
            print "just caught fucking measles or whatever.\n"
        
    elif dropbox == "2":
        print "\nYou need to create a password. What is your password?\n"
        print "1. 'password'\n"
        print "2. 'password1234'\n"
        
        password = raw_input("> ")
        
        if password == "1":
            print "\nFucking horrible password. The game is lost and God destroys your home, eats your dog.\n"
            
        else:
            print "\nExcellent choice. No one will ever guess that. Moving right along."
            print "Your dropbox account successfully prevents the man (his name is Tony Displacable) from "
            print "uh, doing whatever he wanted to do. You win. Enjoy your victory and the illusion of freedom it gives you."
            print "Haha just kidding we know all about freedom.\n"
            
    else:
        print "\nYour internet connection speed is total fucking dogshit. This is going to take awhile."
        print "Do you have all the time in the world?"
        print "\n1. Yes.\n"
        print "2. No.\n"
        
        lots_of_time = raw_input("> ")
        
        if lots_of_time == "1":
            print "\nOk get yourself a big ol' cup of coffee and drink it real fast so you scald your tongue.\n"
            print "Do you scream or do you not scream?\n"
            print "1. Scream.\n"
            print "2. Do not scream.\n"
            
            scream = raw_input("> ")
            
            if scream == "1":
                print "\nYeah I bet that hurt. What were you thinking though? Just go home and close the door behind you. "
                print "There is a bus outside waiting to take you to hell.\n"
                
            else:
                print "\nGood job. There is nothing for you to accomplish. Just like life. The end. You are forgotten."
                print " The world didn't know your name. Now you're just an entry in some book somewhere, if you're lucky. No "
                print "one's going to read that book. Nobody even knows there is a book. The world continues without you. I'm sorry.\n"
        
        else:
            print "\nThen get the fuck out. GET OUT.\n"
            print "1. Run.\n"
            print "2. Walk.\n"
            
            run = raw_input("> ")
            
            if run == "1":
                print "\nYou sprint away. You twist your ankle unfortunately and the poison fog turns you into a skeleton."
                print "That sucks.\n"
                
            else:
                print "\nYou turn around slowly and walk away into the void. You never stop walking. Your feet gradually "
                print "grind into bloody stumps that harden and turn black. You feel no pain. That's the path you took. The end.\n"
        
elif door == "4":
    print "\nYou've entered an empty room. Nothing to see here. What do you want to do now?"
    print "\n1. Turn around.\n"
    print "2. Continue walking.\n"
    print "3. Eat your old sandwich.\n"

    door4 = raw_input("> ")

    if door4 == "1":
        print "\nYou turn around and go back the way you came. You lame wad. \nClose this game and sell your computer. Buy a ferret and just spend your time with that.\n"

    elif door4 == "2":
        print "\nYou find a big book on the floor.\n"
        print "1. Open it up.\n"
        print "2. Kick it out of the way.\n"
        print "3. Huff glue.\n"

        book = raw_input("> ")

        if book == "1":
            print "\nThe book is large. Tons is written. Nothing is said.\n"
            print "1. Laugh.\n"
            print "2. Cry.\n"

            laugh_or_cry = raw_input("> ")

            if laugh_or_cry == "1":
                print "\nYou win. Yep."
                print "Yep that's it."
                print "Game over."
                print "You win the princess. She is your property."
                print "Laughing means you win."
                print "Go home and enjoy your property.\n"
                print "No wait, one more thing.\n"
                print "1. Go home.\n"
                print "2. Read the book.\n"

                read = raw_input("> ")

                if read == "2":
                    i = 0
                    while i < 200:
                        print "Lots of reading to do."
                        if i == 195:
                            print "\t\t\tGotta get some reading done."
                        if i == 196:
                            print "\t\t\tr\t\t\te\t\t\ta\t\t\td\t\t\ti\tn\tg\t!!!!\t\t\t!!!"
                        if i > 190:
                            print "loTts ofF Raedin Toodo"
                        i += 1
                    print "\nYou have been killed by your own hatred of the book's contents. \nYou have drowned in a pool of hate. You should not hate so much."
                    print "But you are already dead. Dead Men Learn No Lessons.\n"
                    
                else:
                    print "\nYou win for real this time. Stay away from doors.\n"
                    
            else:
                print "\nStop crying. You chose this path.\n"
                print "1. Stop.\n"
                print "2. Ignore command.\n"

                command = raw_input("> ")

                if command == "1":
                    print "\nYou get bored with the situation. Your brain melts from boredom. This is a crisis.\n"
                    print "1. Call the crisis hotline 362/24/7.\n"
                    print "2. Deplete energy reserves.\n"

                    crisis = raw_input("> ")

                    if crisis == "1":
                        print "\n'Thank you for calling the Crisis Hotline. Jimmy Chuckle-Truckle here. Where are you located?'\n"
                        print "1. Door Number 4.\n"
                        print "2. I don't know.\n"
                        print "3. Trapped within the venom of the lustful.\n"

                        location = raw_input("> ")

                        if location == "1":
                            print "\n'Ah gee Jimmy got no help for ya. HEEEEEEEE! Lots to do. Lots to do!'"
                            print "You have failed. Good bye."
                            print "The end."
                            print "That's all there is. I'm sorry."
                            print "Try again later.\n"

                        elif location == "2":
                            print "\n'I don't know either, big shot. And that's all the time we have for today."
                            print "And now back to American Gladiators.'\n"

                        else:
                            print "\nTo invoke the hive-mind representing chaos."
                            print "Invoking the feeling of chaos."
                            print "With out order."
                            print "purgs."
                            print "Help."
                            print "purgs."
                            print "The Asply hive-mind of chaos. Wiggle won."
                            print "Lust."
                            print "((((LUST))))"
                            print "He who Waits Behind The Wall."
                            print "WIGGLE WON."
                            print "He loves you."
                            print "We love you."
                            print "Purgs."
                            print "\tPurgs."
                            print "Purgs."
                            print "Help."
                            print "WIGGLE WON."
                            print "PURGS."
                            print "\n\n.\nn\n\nWIGGLE"
                            print "W O N.\n"
                            print "That was the wrong choice. You've shattered the fragile psyches of every human being.\nYou've disappointed us.\n"
                    else:
                        print "\nDEPLETING"
                        print "\tENERGY"
                        print "\t\tRESERVES"
                        print "The crisis is averted however your brain is now mush slop puke slop. Goodbye.\n"

                else:
                    print "\nYou've got a lot of guts ignoring the command."
                    print "Now what do you want to do?\n"
                    print "1. Continue the cryage that you are insisting upon yourself.\n"
                    print "2. Blame the Space Cannister for all your problems.\n"

                    continuing = raw_input("> ")

                    if continuing == "1":
                        print "\nYou cry until you die. Look. You chose to cry. You were asked to stop. You ignored that."
                        print "What the fuck do you want?"
                        print "You're playing MY GAME. You lose.\n"

                    else:
                        print "\nThe Space Cannister reflects sadly upon the choices that it has made. The dent in its side contracts and then explodes."
                        print "\t\t\t\t\tYou're experiencing excessive tabbed indentation."
                        print "I'm sorry things turned out this way. You lose. The end. Good bye. Take your fuckin tickin' top with you. The end. Do not ignore commands.\n"

        elif book == "2":
            print "\nThe book sails across the room. It connects with the face of Bob Rob Plip, the manager of Door 4.\n"
            print "1. Apologize.\n"
            print "2. Apologize A LOT.\n"
            print "3. Do a little dance.\n"

            apology = raw_input("> ")

            if apology == "1":
                print "\n'Iffa jigga weeba heeee haaaaa?'"
                print "......"
                print "It's clear this fuckjack doesn't speak your language.\n"
                print "1. So do. A little. DANCE!\n"
                print "2. Gesticulate submissively to communicate contrition.\n"

                dance = raw_input("> ")

                if dance == "1":
                    print "\nYou dance. You dance the bubble toss. Bob Rob Plip seems mildly impressed, although you can't be sure since you have destroyed his face."
                    print "He allows you to leave on the condition you bubble toss your way back through Door 4."
                    print "You neither win nor lose. That's life. Sorry. It happens to a lot of people. No winning or losing, just passing through."
                    print "No recognition. Nothing remarkable. Just stare into the concrete horizon on your bus commute home. Good job. \nStay in line. Here is your coupon for 29 cents off of a 2-liter bottle of Squirt.\n"

                else:
                    print "\nBob Rob Plip doesn't understand."
                    print "He produces a sidearm from the side of his arm and pumps you full of bullets. The end.\n"
                    print "You can try again.\n"
                    print "IF YOU DARE!\n"

            elif apology == "2":
                print "\nYou're really overdoing it with the apologies. You mean well, but this comes across as hopeless and desperate. You lose. For being a loser.\n"

            else:
                print "\nWhat dance are you going to do?"
                print "\n1. The plaintive wail.\n"
                print "2. The bubble toss.\n"
                print "3. The racist behavior.\n"

                dance_type = raw_input("> ")

                if dance_type == "1":
                    print "\nThe plaintive wail is a crowd favorite with a rich historical history, but historically historians have argued the plaintive wail has gone out of fashion"
                    print " amongst dance enthusiasts such as Door 4 Manager Bob Rob Plip."
                    print "He shakes his head. You lose. I am really sorry about that. Gotta start all over.\n"

                elif dance_type == "2":
                    print "\nBob Rob Plip likes the bubble toss. He lets you leave. You don't win anything, really, but you do have the opportunity to try another door."
                    print "You're pretty damn lucky considering what could have happened though. Just sayin is all.\n"

                else:
                    print "\nYou dance the racist behavior. It is an instant hit. Congratulations!"
                    print "You win."
                    print "You win everything."
                    print "Bob Rob Plip takes off his belt and shuffles over to you, handing you his belt. It contains a gem. The gem is:\n"
                    print "1. White.\n"
                    print "2. Red.\n"

                    gem = raw_input("> ")

                    if gem == "1":
                        print "\nAh man as soon as you touch the gem it flashes its embarrassing whiteness at you and incinerates the universe."
                        print "So close."
                        print "Looks like you lost after all."
                        print "I mean where can you go from there?"
                        print "So yeah so that counts as a fail."
                        print "You racist.\n"

                    else:
                        print "\nThe red gem is warm."
                        print "\tMmmmmmmm."
                        print "Warm."
                        print "Warm like victory.\n"
                        
        elif book == "3":
        	print "\nThe glue enters your nose and you are reminded of why you began huffing glue all those years ago in the elementary school bathroom. \nIt's not your fault nobody taught you how to pee standing up.\n"
        	print "1. Continue huffing.\n"
        	print "2. One hit is enough. Let's not overdo it.\n" 
        	
        	huff = raw_input("> ")
        	
        	if huff == "1":
        		print "\nKeep the rhythm going. IN AND OUT. IN AND OUT."
        		print "Life's not fair."
        		print "Hey slow down there now. Slow down!"
        		print "IN AND OUT."
        		print "Not everyone gets going at the same time."
        		print "The world fades away as white noise comes out of the walls."
        		print "The world is a neglected run-down racetrack."
        		print "The glue wins."
        		print "The world wins. You do not. The end.\n"
        		      		
        	else:
        		print "\nThe euphoria fades pleasantly. Just a little bump is all you needed. Good call.\n You should put the glue away now. What do you do next?"
        		print "\n1. Huff more glue."
        		print "\n2. Avoid the book and continue thinking uselessly about your purpose.\n"
        		
        		thinking = raw_input("> ")
        		
        		if thinking == "1":
        			print "\nDead. You die. The glue kills you, you loser. Why would you do that? WHY?\n"
        			
        		else:
        			print "\nGood. You hate books anyway and everything they represent. Why are you here?"
        			print "\n1. Seeking more glue to huff furiously."
        			print "\n2. Just trying to find the you-sized hole in the world's mysterious chaos.\n"
        			
        			purpose = raw_input("> ")
        			
        			if purpose == "1":
        				print "\nWrong choice. Stay off the glue. Stay out of Door #4! If you can't go two minutes \nwithout shooting chemicals in your face just stay out of this game completely!"
        				print "Game over. Done. Gone. We're done here. The door closes. Try again.\n"
        				
        			else:
        				print "\nSo is everyone. Even the designer of this psychopathic Door scenario."
        				print "He (or she) just wanted to create something that resonates with strangers."
        				print "That's easier said than done."
        				print "Congratulations. You understand."
        				print "You win. The end. Please enter your address so your Certificate of Understanding \ncan be mailed to you.\n"
        				
        				address = raw_input("Enter your real address please: ")
        				
        				print "\nStand by. Contacting mainframe...\n"
        				raw_input("Press any key to continue.")
        				
        				if len(address) >= 0:
        					print "\nERROR. ADDRESS DOES NOT EXIST. \nYOU \nDO \nNOT \nEXIST."
        					print "NOTHING IS REAL. THE ARCHITECTS WILL REVIEW THE RESULTS OF THIS EXPERIMENT."
        					print "\nS. I. M. U. L. A. T. I. O. N.  T. E. R. M. I. N. A. T. E. D."
        				
    else:
    	print "\nThe sandwich sighs. You interpret the sandwich's sigh as a preference for:"
    	print "\n1. Being eaten."
    	print "\n2. Not being eaten."
    	print "\n3. Being content with itself.\n"
    	
    	sandwich_preference = raw_input("> ")
    	
    	if sandwich_preference == "1":
    		print "\nTherefore the sandwich will be eaten. You enjoy it. It is a tasty sandwich."
    		print "Delicious."
    		print "Yummy!"
    		print "The sandwich was loaded with healthy nutrients. You glide back out of Door 4 wraith-like and satisfied. You return home to your studio apartment in the Warehouse District and continue re-reading your favorite book Angels & Demons by Dan Brown. \nYou didn't make it very far in the Door Scenario but the brief pangs of regret that life maybe could have \nchanged had you made different choices are repressed as time marches on in a parade of missed chances and social misfires.\n"
    		
    	elif sandwich_preference == "2":
    		print "\nThis is the moment you realize you no longer have automony over the workings of your mind."
    		print "You have received communications from a sandwich."
    		print "Nothing comes after this. The end.\n"
    		
    	else:
    		print "\nNice! Contentment is a sacred state of being. Make yourself a drink. What'll it be tonight?"
    		print "\n1. A grand mojito."
    		print "\n2. A blisket whisket."
    		print "\n3. A dark-skinned stranger."
    		print "\n4. A plastic vial of subjugated children's tears."
    		print "\n5. Just a glass of water, thanks.\n"
    		
    		drink = raw_input("> ")
    		
    		if drink == "1":
    			print "\nGrand mojitos are banned in all countries in all states of consciousness. Drink it NOW or pour it OUT before you are caught!!!\n"
    			print "1. Guzzle it.\n"
    			print "2. Pour it out.\n"
    			
    			pour = raw_input("> ")
    			
    			if pour == "1":
    				print "\nHoly shit you are gonna die. Goodbye. In five seconds you are going to find out why grand mojitos \nare banned everywhere.\n"
    			
    			else:
    				print "\nThe grand mojito steams and screams, boils and roils, smokes and pokes its way \nout into the night (the ceiling beyond Door #4 is open by the way), the sky turns red with the fire of a supernova. THIS IS WHY GRAND MOJITOS ARE BANNED!!!\n You perceive a brief glimpse of the heavens as the sky burns down. Understanding floods your little mind before it winks out.\n"
    				
    		elif drink == "2":
    			print "\nThis imaginary drink comes to life before your eyes. It is a beautiful concoction but has no inherent value because there is no taste. It doesn't even exist. What are you on???\n"
    			print "1. Drugs.\n"
    			print "2. I'm high on life lol.\n"
    				
    			high = raw_input("> ")
    				
    			if high == "1":
    				print "\nYeah you're getting lost in imaginary drinks. Go outside and come back when you can remember your name. LOSER.\n"
    					
    			else:
    				print "\nThat's cute. You lack sufficient self-awareness to proceed.\nThe world is not small enough to fit in a Facebook status. \nGoodbye.\n"
    				
    		elif drink == "3":
    			print "\nCareful with this one...."
    			print "\n1. Drink it."
    			print "\n2. Think better of your racist choices.\n"
    				
    			racist = raw_input("> ")
    				
    			if racist == "1":
    				print "\nGLUG"
    				print "\tGLUG"
    				print "\t\tGLUG"
    				print "\t\t\tGLUG"
    				print "\t\t\t\tGLUG"
    				print "\t\t\tGLUG"
    				print "\t\tGLUG"
    				print "\tGLUG"
    				print "GLUG"
    				print "Drinking the dark-skinned stranger brings you a self-assured sense of superiority and a persistent conscience that is ignored without difficulty."
    				print "Its benefits include social privilege and access to more dark-skinned strangers."
    				print "\n1. Drink more."
    				print "\n2. Drink A LOT MORE.\n"
    					
    				drink_more = raw_input("> ")
    					
    				if drink_more == "2":
    					print "\nYour greed has gotten the better of you. That's unfortunate because things were going well. You collapse in an exhausted heap of laundry. Door #4 doesn't fuck around. The end.\n"
    						
    				else:
    					print "\nOkay you can have some more, but be careful, this drink is known to cause feelings of deep shame in its drinkers' grandchildren."
    					print "\n1. Have one more, then turn in for the night."
    					print "\n2. Slam back another glass and dance your favorite dance (the bubble toss).\n"
    						
    					one_more = raw_input("> ")
    						
    					if one_more == "1":
    						print "\nYou nurse another dark-skinned stranger and then head home for the night. You awaken with foggy memories of your time in the Door Scenario.\n Convincing yourself it was a mere dream, you get ready for your job routing Moneygram transfers. You don't win or lose, but simply continue."
    						print "You're just another body on this choked planet, but nobody really notices. Your mild existential malaise remains inarticulable and you just kind of tacitly assume this is what adulthood is. \nYou consider picking up a new skill in the hopes of starting a career, but that's funny because that's idealistic. Dreams don't come true. That's for kids who don't know better."
    						print "\nThat's the problem with dark-skinned strangers...\n"
    							
    					else:
    						end = time.time()
    						seconds = int(end - start)
    						print "\nYou passed through Door #4 %d seconds ago and you're already slamming back dark-skinned strangers? Please start over and go more slowly.\n" % seconds
    			
    			else:
    				print "\nVery wise. But what are you doing with your life? You considered drinking something called the dark-skinned stranger. How can you possibly hope to win with that approach? The end.\n"    				
    		
    		elif drink == "4":
    			print "\nYeah you love the taste."
    			print "\n1. Tastes like democracy."
    			print "\n2. Tastes like salt."
    			print "\n3. Tastes like a grand mojito.\n"
    			
    			taste = raw_input("> ")
    			
    			if taste == "1":
    				print "\nDoor #4 fucks with your mind too much. Despite the delicious democratic taste, you suffer a momentary bout of morality and put the vial down.\nYou turn around and walk away. Maybe you should not have eaten that old sandwich. I'm sorry. The end.\n"
    				
    			elif taste == "2":
    				print "\nSlaves cry salty tears. You have just learned another thing about the world."
    				print "\n1. Sweet! LEVEL UP!"
    				print "\n2. The guilt train comes rollin into the hate station.\n"
    				
    				guilt = raw_input("> ")
    				
    				if guilt == "1":
    					print "\nYou become dictator. You round up more slave children. You swim in pools of their tears. You are a fucking monster. Years pass. You think you've won.\nBut deep down you know you made the wrong choice. You munch on a child's shinbone. This was not the most ideal outcome.\n"
    					
    				else:
    					print "\nALL ABOARD!!! Too late. This mothafucka takes the express route to Sorrowsville. Here you will see how children's tears are harvested. You have made some dark choices. \nThe world continues, shamefully acknowledging that you were once a part of it. Game over.\n"
    					
    			else:
    				print "\nNo it doesn't. You have failed. The end.\n"
    		
    		else:
    			print "\nWater is always a smart choice in the event of confusing options. Do you want ice?\n"
    			print "1. Yes.\n"
    			print "2. GIMME DAT ICE.\n"
    			
    			ice = raw_input("> ")			
    				
    			if ice == "1":
    				print "\nYou enjoy the cool ice water and relax in Door #4's chamber."
    				print "You don't have much motivation to continue but that's okay. Door #4 contained some unspeakable horrors. Just get out while you can. Congrats. You win. Your dog will not be killed.\n"
    				
    			else:
    				print "\nFucking what?"
    				print "\n1. I SAY GIMME DAT ICE."
    				print "\n2. Nevermind; no ice.\n"
    
    				gimme_ice = raw_input("> ")
    				
    				if gimme_ice == "1":
    					print "\nYou shut your loser mouth. You know what. No, forget it. Game over. Nobody talks in caps like that to me. Go home.\n"
    				
    				else:
    					print "\nA large monster (made of ice) crashes through the wall and tears you apart with its icy gaze. You reflect grimly on the crushing irony of the situation."
    					print "Another large monster (made of iron) crushes through the other wall and laughs a hearty laugh that sounds like ambivalent rage. The end?\n"
    					
else:
    print "\nTHERE \tARE \tNO \tOTHER \tOPTIONS."

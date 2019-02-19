import random
'''
capitals = {' Alabama' : ' Montgomery' , ' Alaska' : ' Juneau' , ' Arizona' : ' Phoenix' ,
' Arkansas' : ' Little Rock' , ' California' : ' Sacramento' , ' Colorado' : ' Denver' ,
' Connecticut' : ' Hartford' , ' Delaware' : ' Dover' , ' Florida' : ' Tallahassee' ,
' Georgia' : ' Atlanta' , ' Hawaii' : ' Honolulu' , ' Idaho' : ' Boise' , ' Illinois' :
' Springfield' , ' Indiana' : ' Indianapolis' , ' Iowa' : ' Des Moines' , ' Kansas' :
' Topeka' , ' Kentucky' : ' Frankfort' , ' Louisiana' : ' Baton Rouge' , ' Maine' :
' Augusta' , ' Maryland' : ' Annapolis' , ' Massachusetts' : ' Boston' , ' Michigan' :
' Lansing' , ' Minnesota' : ' Saint Paul' , ' Mississippi' : ' Jackson' , ' Missouri' :
' Jefferson City' , ' Montana' : ' Helena' , ' Nebraska' : ' Lincoln' , ' Nevada' :
' Carson City' , ' New Hampshire' : ' Concord' , ' New Jersey' : ' Trenton' , ' New Mexico' :
' Santa Fe' , ' New York' : ' Albany' , ' North Carolina' : ' Raleigh' ,
' North Dakota' : ' Bismarck' , ' Ohio' : ' Columbus' , ' Oklahoma' : ' Oklahoma City' ,
' Oregon' : ' Salem' , ' Pennsylvania' : ' Harrisburg' , ' Rhode Island' : ' Providence' ,
' South Carolina' : ' Columbia' , ' South Dakota' : ' Pierre' , ' Tennessee' :
' Nashville' , ' Texas' : ' Austin' , ' Utah' : ' Salt Lake City' , ' Vermont' :
' Montpelier' , ' Virginia' : ' Richmond' , ' Washington' : ' Olympia' , ' West Virginia' :
 ' Charleston' , ' Wisconsin' : ' Madison' , ' Wyoming' : ' Cheyenne' }
'''
capitals={'Andhra Pradesh':'Hyderabad (shared with Telangana)','Arunachal Pradesh':'Itanagar','Assam':'Dispur','Bihar':'Patna','Chhattisgarh':'Raipur','Goa':'Panaji','Gujarat':'Gandhinagar','Haryana':'Chandigarh (shared with Punjab)','Himachal Pradesh':'Shimla','Jammu &amp; Kashmir':'Srinagar (Summer) Jammu (Winter)','Jharkhand':'Ranchi','Karnataka':'Bangalore','Kerala':'Thiruvananthapuram','Madhya Pradesh':'Bhopal','Maharashtra':'Mumbai','Manipur':'Imphal','Meghalaya':'Shillong','Mizoram':'Aizawl','Nagaland':'Kohima','Odisha (Orissa)':'Bhubaneshwar','Punjab':'Chandigarh (shared with Haryana)','Rajasthan':'Jaipur','Sikkim':'Gangtok','Tamil Nadu':'Chennai','Telangana (from June 2':'Hyderabad (shared with Andhra Pradesh)','Tripura':'Agartala','Uttar Pradesh':'Lucknow','Uttarakhand':'Dehradun','West Bengal':'Kolkata'}
for k,v in capitals.items():
	print(k.rjust(20), '  ',v)

def createQuizFile():
	for quizNum in range(3): #3files
		
		quizFile=open('capitalsquiz%s.txt'%(quizNum+1),'w')
		answerKeyFile=open('capitalquiz_answers%s.txt'%(quizNum+1),'w')

		#Write out the header for the quiz
		quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
		quizFile.write((' '*20)+'State Capitals Quiz (Form %s)' % (quizNum+1))
		quizFile.write('\n\n')
		
		#shuffle the order of the states
		states=list(capitals.keys())

		random.shuffle(states)
		
		#Loop through all 50 states making a question for each

		for questionNum in range(5): #5 questions per file
			#Get the right and wrong
			correctAnswer=capitals[states[questionNum]]	
			wrongAnswers=list(capitals.values())		
			del wrongAnswers[wrongAnswers.index(correctAnswer)]			
			wrongAnswers=random.sample(wrongAnswers,3)			
			answerOptions=wrongAnswers+[correctAnswer]
			random.shuffle(answerOptions)

			#write the question and the answer options to the quiz file
			quizFile.write('%s. What is the capital of %s?\n' %(questionNum+1,states[questionNum]))
			for i in range(4):
				quizFile.write(' %s. %s\n' % ('ABCD'[i],answerOptions[i]))
			quizFile.write('\n')

			#write the answer key to a file.
			answerKeyFile.write('%s. %s\n'%(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
		quizFile.close()
		answerKeyFile.close()
			




if __name__ == '__main__':
	createQuizFile()
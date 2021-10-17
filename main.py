import movie
b = movie.Book_Ticket()
while True:
	print('==================================================')
	print('1. Show the tickets')
	print('2. Buy a tickets')
	print('3. Statistics')
	print('4. Show booked ticket user info')
	print('0. Exit')
	choice = input('Please select your choice from above: ')
	while choice.isdigit()==False:
		print('Please choose the choice in numbers')
		choice = input('Please select your choice from above: ')
		continue
	choice = int(choice)
	if choice==0:
		break
	if choice ==1:
		b.show_seats()
	elif choice == 2:
		b.buy_ticket()
	elif choice==3:
		b.statistics()
	elif choice == 4:
		b.get_details()

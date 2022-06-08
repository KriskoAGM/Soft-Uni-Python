student_tickets = 0
standard_tickets = 0
kid_tickets = 0
occupied_tickets = 0
command = ''

while command != 'Finish':
    movie_name = input()
    free_seats = int(input())

    current_ticket = 0

    while free_seats >= occupied_tickets:
        ticket_type = input()

        if ticket_type == 'student':
            student_tickets += 1
            occupied_tickets += 1
            current_ticket += 1

        elif ticket_type == 'standard':
            standard_tickets += 1
            occupied_tickets += 1
            current_ticket += 1

        elif ticket_type == 'kid':
            kid_tickets += 1
            occupied_tickets += 1
            current_ticket += 1

        if ticket_type == 'End':
            break

        if ticket_type == 'Finish':
            command = 'Finish'
            break

        if free_seats < occupied_tickets:
            break

    print(f'{movie_name} - {current_ticket / free_seats * 100:.2f}% full.')

print(f'Total tickets: {occupied_tickets}')
print(f'{student_tickets / occupied_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / occupied_tickets * 100:.2f}% standard tickets.')
print(f'{kid_tickets / occupied_tickets * 100:.2f}% kids tickets.')


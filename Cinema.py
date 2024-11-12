class star_cinema:
    hall_list=[]

    def entry_hall(self, hall):
        star_cinema.hall_list.append(hall)


class hall(star_cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats={}
        self._show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        self._show_id=show_id
        self._movie_name=movie_name
        self.time=time
        self._show_list.append((show_id, movie_name, time))
        self._seats[show_id]=[[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, show_id, rows, cols):
        if show_id in self._seats:
            if rows>self.rows or cols>self.cols:
                print('Invalid seat.')
            elif self._seats[show_id][rows-1][cols-1]=='1':
                print('Seat is not available.')
            else:
                self._seats[show_id][rows-1][cols-1]='1'
                print(f'Seat booked at row = {rows} and cols = {cols}')
        else:
            print('Invalid!')

    def view_show_list(self):
        print('Available show: ')
        for x in self._show_list:
            print("Show name: " + x[1] + " Show time: " + x[2])

    def view_available_seats(self, show_id):
        for x in self._seats[show_id]:
            print(x)


halll=hall(5, 5, 1)
halll.entry_show('3', 'Jawan Majhi', '1212')
halll.entry_show('2', 'Sujon Majhi', '1211')


while True:
    print('''1. View All Show Today.
2. View Available Seats.
3. Book Ticket.
4. Exit''')
    x=int(input('ENTER OPTION: '))
    print('-------------')
    if x==1:
        halll.view_show_list()
        print('-------------')
    elif x==2:
        z=input('ENTER SHOW ID: ')
        halll.view_available_seats(z)
        print('-------------')
    elif x==3:
        showid=input('Show ID: ')
        NumofT=int(input('Number of Tickets? '))
        for i in range(0,NumofT):
            srow=int(input('Enter Seat Row: '))
            scol=int(input('Enter Seat Col: '))
            halll.book_seats(showid, srow, scol)
        else:
            halll.view_available_seats(showid)
        print('-------------')
    else:
        break



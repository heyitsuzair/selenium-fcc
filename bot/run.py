from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.close_modal()
    # bot.change_currency('EUR')
    bot.select_place_to_go('Lahore')
    bot.select_dates('2023-03-16', '2023-03-14')
    bot.select_occupancy(10)
    bot.search()
from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency('EUR')
    bot.select_place_to_go('Lahore')
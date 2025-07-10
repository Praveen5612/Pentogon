print('..................................................')
print('.................Welcome to Goa.................')
print('..................................................')

def booking(aadhar, dl, vehicle, price, days):
    amount = price * days
    print('....Your Booking details are as follows....')
    print('------------------------------------------')
    print('Vehicle : ', vehicle)
    print('Amount per day : ', price)
    print('Aadhar Number : ', aadhar)
    print('Driving License Number : ', dl)
    print('Number of days : ', days)
    print('Total Amount : ', amount)
    print('------------------------------------------')
    print('Do you want to continue?')
    print('1.Yes \n 2.No \n')
    confirm  = int(input('Choose an option: '))
    if confirm == 1:
        print('Congratulations....! Your booking is confirmed..!!')
        print('Please pay at the amount at the time of pick-up by providing your documents.')
    else:
        print('Your booking is cancelled!!!')
print('Thank you for choosing us!')

# Main program
print('What do you want to rent?')
print('1. Two Wheeler \n2. Four Wheeler')
rent = int(input('Choose an option: '))
if rent == 1:
    print('1. Bike \n2. Scooter')
    print('Choose an option: ')
    bike = int(input())

    if bike  == 1:
        print('Select what bike you want to rent: ')
        print('1. Royal Enfield \n2. Yamaha')
        bike_choice = int(input('Choose an option: '))
        if bike_choice == 1:
            print('You have selected the Royal Enfield bike for rent')
            days = int(input('For how many days do you want to rent this vehicle?'))
            aadhar = input('Enter your Aadhar number: ')
            dl = input('Enter your Driving License number: ')
            booking(aadhar, dl, 'Royal Enfield', 1200, days)
        elif bike_choice == 2:
            print('You have selected the Yamaha bike for rent')
            days = int(input('For how many days do you want to rent this vehicle?'))
            aadhar = input('Enter your Aadhar number: ')
            dl = input('Enter your Driving License number: ')
            booking(aadhar, dl, 'Yamaha', 1000, days)
        else:
            print('Please select a valid bike option.')

    elif bike == 2:
        print('Select what bike you want to rent: ')
        print('1. Honda \n2. Suzuki')
        bike_choice = int(input('Choose an option: '))
        if bike_choice == 1:
            print('You have selected the Honda bike for rent')
            days = int(input('For how many days do you want to rent this vehicle?'))
            aadhar = input('Enter your Aadhar number: ')
            dl = input('Enter your Driving License number: ')
            booking(aadhar, dl, 'Honda', 500, days)
        elif bike_choice == 2:
            print('You have selected the Suzuki bike for rent')
            days = int(input('For how many days do you want to rent this vehicle?'))
            aadhar = input('Enter your Aadhar number: ')
            dl = input('Enter your Driving License number: ')
            booking(aadhar, dl, 'Suzuki', 400, days)
        else:
            print('Please select a valid bike option.')
    else:
        print('please select the two wheeler option or four wheeler option.')
elif rent == 2:
    print('1. Car \n2. SUV')
    print('Choose an option: ')
    car = int(input())

    if car == 1:
        print('Select what car you want to rent: ')
        print('1. Maruti Suzuki \n2. Hyundai')
        car_choice = int(input('Choose an option: '))
        if car_choice == 1:
            print('You have selected the Maruti Suzuki car for rent')
            days = int(input('For how many days do you want to rent this vehicle?'))
            aadhar = input('Enter your Aadhar number: ')
            dl = input('Enter your Driving License number: ')
            booking(aadhar, dl, 'Maruti Suzuki', 2000, days)
        elif car_choice == 2:
            print('You have selected the Hyundai car for rent')
            days = int(input('For how many days do you want to rent this vehicle?'))
            aadhar = input('Enter your Aadhar number: ')
            dl = input('Enter your Driving License number: ')
            booking(aadhar, dl, 'Hyundai', 2200, days)
        else:
            print('Please select a valid car option.')

    elif car == 2:
        print('Select what SUV you want to rent: ')
        print('1. Mahindra \n2. Tata')
        suv_choice = int(input('Choose an option: '))
        if suv_choice == 1:
            print('You have selected the Mahindra SUV for rent')
            days = int(input('For how many days do you want to rent this vehicle?'))
            aadhar = input('Enter your Aadhar number: ')
            dl = input('Enter your Driving License number: ')
            booking(aadhar, dl, 'Mahindra', 2500, days)
        elif suv_choice == 2:
            print('You have selected the Tata SUV for rent')
            days = int(input('For how many days do you want to rent this vehicle?'))
            aadhar = input('Enter your Aadhar number: ')
            dl = input('Enter your Driving License number: ')
            booking(aadhar, dl, 'Tata', 2700, days)
        else:
            print('Please select a valid SUV option.')
else:
    print('Please select a valid option for renting a vehicle.')

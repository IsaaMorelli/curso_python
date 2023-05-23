# complexibilidade de código

speed = 61             #velocidade do carro
position = 100

RADAR = 60               #velocidade máximo
RADAR_POSITION = 100     #onde o radar está
RANGE = 1                #distancia que o radar pega

car_position = position == RADAR_POSITION or \
position == (RADAR_POSITION - 1) or \
position == (RADAR_POSITION + 1)

if speed > RADAR:
    print("You are above the speed allowed by the radar")
    if speed > RADAR and car_position:
        print("Your car was fined")
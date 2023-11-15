#perfect humidity is 50 RH, range is 0-100
h_score = 5- (abs(50-humidity)/10)
#perfect temperautre is 20 C, range is about 0 to 40
t_score = 5- (abs(20-temperature)/4)
#perfect sound level is 0, goes up to about 400
s_score = 5- (sound/80)
#perfect light score is 0, goes up to about 500
l_score = 5- (light/100)

total_score = h_score+t_score+s_score+l_score

#add/subtract based on weather
if rain > 0:
    total_score = total_score + 2
if snowfall > 0:
    total_score = total_score + 3
if cloud_cover > 0:
    total_score = total_score - 1

setText("Vibe Score: " + str(total_score))
setRGB
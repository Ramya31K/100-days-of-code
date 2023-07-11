def cal_total_time(X, Y):
    tot_time = X + Y - (Y * 0.5)
    return tot_time
X = int(input("Enter the total duration of the movie (in minutes): "))
Y = int(input("Enter the duration of the first part of the movie (in minutes, even number): "))
total_time = cal_total_time(X, Y)
print("Chef will spend watching the total movie", total_time, "minutes")

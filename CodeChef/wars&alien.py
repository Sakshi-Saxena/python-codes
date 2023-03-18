deptThh,deptTmm = input().split(" ")
timetravelhh,timetravelmm = input().split(" ")
deptThh = int(deptThh)
deptTmm = int(deptTmm)
timetravelhh = int(timetravelhh)
timetravelmm = int(timetravelmm)

totalTravelTime = (timetravelhh * 60) + timetravelmm

for x in range(1, totalTravelTime + 1):
    deptTmm += 1
    if deptTmm > 59:
        deptTmm = 0
        deptThh += 1
        if deptThh > 23:
            deptThh = 0

print(f"{deptThh:02d}", f"{deptTmm:02d}")
import json

def findStations(required, stations):
    required = set(required)
    stationsUsed = []

    while required:
        bestOne = None
        coveredByBest = set()

        for s in stations:
            covered = required & set(s["Cities"])
            
            if len(covered) > len(coveredByBest):
                bestOne = s
                coveredByBest = covered

        if bestOne is None:
            break

        required -= coveredByBest
        stationsUsed.append(bestOne["Name"])
        
    return stationsUsed

def main():
    required = json.loads(input())
    stations = []
    num_stations = int(input())
    
    for _ in range(num_stations):
        stations_in = json.loads(input())
        stations.append(stations_in)
        
    print(sorted(findStations(required, stations)))

main()
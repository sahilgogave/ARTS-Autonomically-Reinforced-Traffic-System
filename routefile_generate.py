import random

def generate_train(i):
    """generate SUMO road network xml files for training"""
    random.seed(i)
    with open("data/cross.rou.xml", "w") as routes:
        p = list()
        p.append(random.randint(32, 43))
        p.append(random.randint(40, 55))
        p.append(random.randint(5, 8))
        p.append(random.randint(5, 8))
        p.append(random.randint(10, 15))
        p.append(random.randint(10, 15))
        print("""<routes>""", file=routes)
        print("""<vTypeDistribution id="mixed">
                    <vType id="car" vClass="passenger" speedDev="0.2" minGap = "1" sigma = "0.5" latAlignment="compact" probability="{}"/>
                    <vType id="motorcycle" vClass="motorcycle" speedDev="0.4" minGap = "0.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                    <vType id="bus" vClass="bus" speedDev="0.15" minGap = "1.5" sigma = "0.3" latAlignment="compact" probability="{}"/>
                    <vType id="truck" vClass="truck" speedDev="0.1" minGap = "1.5" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="sedan" vClass="taxi" speedDev="0.2" minGap = "1" sigma = "0.5" latAlignment="compact" probability="{}" color="grey"/>
                    <vType id="moped" vClass="moped" speedDev="0.4" minGap = "0.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                </vTypeDistribution>""".format(p[0], p[1], p[2], p[3], p[4], p[5]), file=routes)
        p = []
        p.append(random.randint(32, 43))
        p.append(random.randint(40, 55))
        p.append(random.randint(5, 8))
        p.append(random.randint(5, 8))
        p.append(random.randint(10, 15))
        p.append(random.randint(10, 15))
        print("""<vTypeDistribution id="mixed1">
                    <vType id="car1" vClass="passenger" speedDev="0.2" minGap = "1" sigma = "0.5" latAlignment="compact" probability="{}"/>
                    <vType id="motorcycle1" vClass="motorcycle" speedDev="0.4" minGap = "0.5" sigma = "0.5" latAlignment="compact" probability="{}"/>
                    <vType id="bus1" vClass="bus" speedDev="0.15" minGap = "1.5" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="truck1" vClass="truck" speedDev="0.1" minGap = "1.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                    <vType id="sedan1" vClass="taxi" speedDev="0.2" minGap = "1" sigma = "0.4" latAlignment="compact" probability="{}" color="grey"/>
                    <vType id="moped1" vClass="moped" speedDev="0.4" minGap = "0.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                </vTypeDistribution>""".format(p[0], p[1], p[2], p[3], p[4], p[5]), file=routes)
        p = []
        p.append(random.randint(32, 43))
        p.append(random.randint(40, 55))
        p.append(random.randint(5, 8))
        p.append(random.randint(5, 8))
        p.append(random.randint(10, 15))
        p.append(random.randint(10, 15))
        print("""<vTypeDistribution id="mixed2">
                    <vType id="car2" vClass="passenger" speedDev="0.2" minGap = "1" sigma = "0.3" latAlignment="compact" probability="{}"/>
                    <vType id="motorcycle2" vClass="motorcycle" speedDev="0.4" minGap = "0.5" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="bus2" vClass="bus" speedDev="0.15" minGap = "1.5" sigma = "0.2" latAlignment="compact" probability="{}"/>
                    <vType id="truck2" vClass="truck" speedDev="0.1" minGap = "1.5" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="sedan2" vClass="taxi" speedDev="0.2" minGap = "1" sigma = "0.5" latAlignment="compact" probability="{}" color="grey"/>
                    <vType id="moped2" vClass="moped" speedDev="0.4" minGap = "0.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                </vTypeDistribution>""".format(p[0], p[1], p[2], p[3], p[4], p[5]), file=routes)
        p = []
        p.append(random.randint(32, 43))
        p.append(random.randint(40, 55))
        p.append(random.randint(5, 8))
        p.append(random.randint(5, 8))
        p.append(random.randint(10, 15))
        p.append(random.randint(10, 15))
        print("""<vTypeDistribution id="mixed3">
                    <vType id="car3" vClass="passenger" speedDev="0.2" minGap = "1" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="motorcycle3" vClass="motorcycle" speedDev="0.4" minGap = "0.5" sigma = "0.5" latAlignment="compact" probability="{}"/>
                    <vType id="bus3" vClass="bus" speedDev="0.15" minGap = "1.5" sigma = "0.5" latAlignment="compact" probability="{}"/>
                    <vType id="truck3" vClass="truck" speedDev="0.1" minGap = "1.5" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="sedan3" vClass="taxi" speedDev="0.2" minGap = "1" sigma = "0.3" latAlignment="compact" probability="{}" color="grey"/>
                    <vType id="moped3" vClass="moped" speedDev="0.4" minGap = "0.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                </vTypeDistribution>""".format(p[0], p[1], p[2], p[3], p[4], p[5]), file=routes)
        print("""<routes>
                <routeDistribution id="r0" departSpeed="random">
                    <route id="route0" color="1,1,0" edges="51o 1o 4i 54i" probability="3"/>
                    <route id="route1" color="1,1,0" edges="51o 1o 2i 52i" probability="19"/>
                    <route id="route2" color="1,1,0" edges="51o 1o 3i 53i" probability="3"/>
                    <route id="route3" color="1,1,0" edges="53o 3o 1i 51i" probability="3"/>
                    <route id="route4" color="1,1,0" edges="53o 3o 4i 54i" probability="19"/>
                    <route id="route5" color="1,1,0" edges="53o 3o 2i 52i" probability="3"/>
                    <route id="route6" color="1,1,0" edges="52o 2o 1i 51i" probability="19"/>
                    <route id="route7" color="1,1,0" edges="52o 2o 4i 54i" probability="3"/>
                    <route id="route8" color="1,1,0" edges="52o 2o 3i 53i" probability="3"/>
                    <route id="route9" color="1,1,0" edges="54o 4o 1i 51i" probability="3"/>
                    <route id="route10" color="1,1,0" edges="54o 4o 2i 52i" probability="3"/>
                    <route id="route11" color="1,1,0" edges="54o 4o 3i 53i" probability="19"/>
                </routeDistribution>
                <routeDistribution id="r1" departSpeed="random">
                    <route id="route0" color="1,1,0" edges="51o 1o 4i 54i" probability="4"/>
                    <route id="route1" color="1,1,0" edges="51o 1o 2i 52i" probability="17"/>
                    <route id="route2" color="1,1,0" edges="51o 1o 3i 53i" probability="4"/>
                    <route id="route3" color="1,1,0" edges="53o 3o 1i 51i" probability="4"/>
                    <route id="route4" color="1,1,0" edges="53o 3o 4i 54i" probability="17"/>
                    <route id="route5" color="1,1,0" edges="53o 3o 2i 52i" probability="4"/>
                    <route id="route6" color="1,1,0" edges="52o 2o 1i 51i" probability="17"/>
                    <route id="route7" color="1,1,0" edges="52o 2o 4i 54i" probability="4"/>
                    <route id="route8" color="1,1,0" edges="52o 2o 3i 53i" probability="4"/>
                    <route id="route9" color="1,1,0" edges="54o 4o 1i 51i" probability="4"/>
                    <route id="route10" color="1,1,0" edges="54o 4o 2i 52i" probability="4"/>
                    <route id="route11" color="1,1,0" edges="54o 4o 3i 53i" probability="17"/>
                </routeDistribution>
                <routeDistribution id="r2" departSpeed="random">
                    <route id="route0" color="1,1,0" edges="51o 1o 4i 54i" probability="15"/>
                    <route id="route1" color="1,1,0" edges="51o 1o 2i 52i" probability="70"/>
                    <route id="route2" color="1,1,0" edges="51o 1o 3i 53i" probability="15"/>
                </routeDistribution>
                <routeDistribution id="r3" departSpeed="random">             
                    <route id="route6" color="1,1,0" edges="52o 2o 1i 51i" probability="60"/>
                    <route id="route7" color="1,1,0" edges="52o 2o 4i 54i" probability="20"/>
                    <route id="route8" color="1,1,0" edges="52o 2o 3i 53i" probability="20"/>                
                </routeDistribution>
                <routeDistribution id="r4" departSpeed="random">                
                    <route id="route3" color="1,1,0" edges="53o 3o 1i 51i" probability="20"/>
                    <route id="route4" color="1,1,0" edges="53o 3o 4i 54i" probability="60"/>
                    <route id="route5" color="1,1,0" edges="53o 3o 2i 52i" probability="20"/>                                
                </routeDistribution>
                <routeDistribution id="r5" departSpeed="random">                                                
                    <route id="route9" color="1,1,0" edges="54o 4o 1i 51i" probability="25"/>
                    <route id="route10" color="1,1,0" edges="54o 4o 2i 52i" probability="25"/>
                    <route id="route11" color="1,1,0" edges="54o 4o 3i 53i" probability="50"/>
                </routeDistribution>
            </routes>        
            <flow id="mixed0" begin="0" number="100" vehsPerHour="500" route="r0" type="mixed3" departLane="random" departPosLat="random"/>
            <flow id="mixed5" begin="0" number="100" vehsPerHour="500" route="r5" type="mixed2" departLane="random" departPosLat="random"/>
            <flow id="mixed1" begin="50" number="100" vehsPerHour="500" route="r4" type="mixed1" departLane="random" departPosLat="random"/>
            <flow id="mixed3" begin="50" number="100" vehsPerHour="500" route="r2" type="mixed" departLane="random" departPosLat="random"/>
            <flow id="mixed4" begin="100" number="100" vehsPerHour="500" route="r3" type="mixed1" departLane="random" departPosLat="random"/>
            <flow id="mixed" begin="100" number="100" vehsPerHour="500" route="r1" type="mixed3" departLane="random" departPosLat="random"/>
            <flow id="mixed2" begin="300" number="100" vehsPerHour="500" route="r3" type="mixed2" departLane="random" departPosLat="random"/>
            <flow id="mixed6" begin="300" number="100" vehsPerHour="500" route="r5" type="mixed" departLane="random" departPosLat="random"/>""",
              file=routes)
        print("</routes>", file=routes)

def generate_test(i):
    """Generate SUMO road network xml files for testing"""
    random.seed(i)
    with open("data/cross.rou.xml", "w") as routes:
        p = []
        p.append(random.randint(32, 43))
        p.append(random.randint(40, 55))
        p.append(random.randint(5, 8))
        p.append(random.randint(5, 8))
        p.append(random.randint(10, 15))
        p.append(random.randint(10, 15))
        print("""<routes>""", file=routes)
        print("""<vTypeDistribution id="mixed">
                    <vType id="car" vClass="passenger" speedDev="0.2" minGap = "1" sigma = "0.5" latAlignment="compact" probability="{}"/>
                    <vType id="motorcycle" vClass="motorcycle" speedDev="0.4" minGap = "0.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                    <vType id="bus" vClass="bus" speedDev="0.15" minGap = "1.5" sigma = "0.3" latAlignment="compact" probability="{}"/>
                    <vType id="truck" vClass="truck" speedDev="0.1" minGap = "1.5" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="sedan" vClass="taxi" speedDev="0.2" minGap = "1" sigma = "0.5" latAlignment="compact" probability="{}" color="grey"/>
                    <vType id="moped" vClass="moped" speedDev="0.4" minGap = "0.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                </vTypeDistribution>""".format(p[0], p[1], p[2], p[3], p[4], p[5]), file=routes)
        p = []
        p.append(random.randint(32, 43))
        p.append(random.randint(40, 55))
        p.append(random.randint(5, 8))
        p.append(random.randint(5, 8))
        p.append(random.randint(10, 15))
        p.append(random.randint(10, 15))
        print("""<vTypeDistribution id="mixed1">
                    <vType id="car1" vClass="passenger" speedDev="0.2" minGap = "1" sigma = "0.5" latAlignment="compact" probability="{}"/>
                    <vType id="motorcycle1" vClass="motorcycle" speedDev="0.4" minGap = "0.5" sigma = "0.5" latAlignment="compact" probability="{}"/>
                    <vType id="bus1" vClass="bus" speedDev="0.15" minGap = "1.5" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="truck1" vClass="truck" speedDev="0.1" minGap = "1.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                    <vType id="sedan1" vClass="taxi" speedDev="0.2" minGap = "1" sigma = "0.4" latAlignment="compact" probability="{}" color="grey"/>
                    <vType id="moped1" vClass="moped" speedDev="0.4" minGap = "0.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                </vTypeDistribution>""".format(p[0], p[1], p[2], p[3], p[4], p[5]), file=routes)
        p = []
        p.append(random.randint(32, 43))
        p.append(random.randint(40, 55))
        p.append(random.randint(5, 8))
        p.append(random.randint(5, 8))
        p.append(random.randint(10, 15))
        p.append(random.randint(10, 15))
        print("""<vTypeDistribution id="mixed2">
                    <vType id="car2" vClass="passenger" speedDev="0.2" minGap = "1" sigma = "0.3" latAlignment="compact" probability="{}"/>
                    <vType id="motorcycle2" vClass="motorcycle" speedDev="0.4" minGap = "0.5" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="bus2" vClass="bus" speedDev="0.15" minGap = "1.5" sigma = "0.2" latAlignment="compact" probability="{}"/>
                    <vType id="truck2" vClass="truck" speedDev="0.1" minGap = "1.5" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="sedan2" vClass="taxi" speedDev="0.2" minGap = "1" sigma = "0.5" latAlignment="compact" probability="{}" color="grey"/>
                    <vType id="moped2" vClass="moped" speedDev="0.4" minGap = "0.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                </vTypeDistribution>""".format(p[0], p[1], p[2], p[3], p[4], p[5]), file=routes)
        p = []
        p.append(random.randint(32, 43))
        p.append(random.randint(40, 55))
        p.append(random.randint(5, 8))
        p.append(random.randint(5, 8))
        p.append(random.randint(10, 15))
        p.append(random.randint(10, 15))
        print("""<vTypeDistribution id="mixed3">
                    <vType id="car3" vClass="passenger" speedDev="0.2" minGap = "1" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="motorcycle3" vClass="motorcycle" speedDev="0.4" minGap = "0.5" sigma = "0.5" latAlignment="compact" probability="{}"/>
                    <vType id="bus3" vClass="bus" speedDev="0.15" minGap = "1.5" sigma = "0.5" latAlignment="compact" probability="{}"/>
                    <vType id="truck3" vClass="truck" speedDev="0.1" minGap = "1.5" sigma = "0.4" latAlignment="compact" probability="{}"/>
                    <vType id="sedan3" vClass="taxi" speedDev="0.2" minGap = "1" sigma = "0.3" latAlignment="compact" probability="{}" color="grey"/>
                    <vType id="moped3" vClass="moped" speedDev="0.4" minGap = "0.5" sigma = "0.6" latAlignment="compact" probability="{}"/>
                </vTypeDistribution>""".format(p[0], p[1], p[2], p[3], p[4], p[5]), file=routes)
        print("""<routes>                
                <routeDistribution id="r0" departSpeed="random">
                    <route id="route0" color="1,1,0" edges="51o 1o 4i 54i" probability="3"/>
                    <route id="route1" color="1,1,0" edges="51o 1o 2i 52i" probability="19"/>
                    <route id="route2" color="1,1,0" edges="51o 1o 3i 53i" probability="3"/>
                    <route id="route3" color="1,1,0" edges="53o 3o 1i 51i" probability="3"/>
                    <route id="route4" color="1,1,0" edges="53o 3o 4i 54i" probability="19"/>
                    <route id="route5" color="1,1,0" edges="53o 3o 2i 52i" probability="3"/>
                    <route id="route6" color="1,1,0" edges="52o 2o 1i 51i" probability="19"/>
                    <route id="route7" color="1,1,0" edges="52o 2o 4i 54i" probability="3"/>
                    <route id="route8" color="1,1,0" edges="52o 2o 3i 53i" probability="3"/>
                    <route id="route9" color="1,1,0" edges="54o 4o 1i 51i" probability="3"/>
                    <route id="route10" color="1,1,0" edges="54o 4o 2i 52i" probability="3"/>
                    <route id="route11" color="1,1,0" edges="54o 4o 3i 53i" probability="19"/>
                </routeDistribution>
                <routeDistribution id="r1" departSpeed="random">
                    <route id="route0" color="1,1,0" edges="51o 1o 4i 54i" probability="4"/>
                    <route id="route1" color="1,1,0" edges="51o 1o 2i 52i" probability="17"/>
                    <route id="route2" color="1,1,0" edges="51o 1o 3i 53i" probability="4"/>
                    <route id="route3" color="1,1,0" edges="53o 3o 1i 51i" probability="4"/>
                    <route id="route4" color="1,1,0" edges="53o 3o 4i 54i" probability="17"/>
                    <route id="route5" color="1,1,0" edges="53o 3o 2i 52i" probability="4"/>
                    <route id="route6" color="1,1,0" edges="52o 2o 1i 51i" probability="17"/>
                    <route id="route7" color="1,1,0" edges="52o 2o 4i 54i" probability="4"/>
                    <route id="route8" color="1,1,0" edges="52o 2o 3i 53i" probability="4"/>
                    <route id="route9" color="1,1,0" edges="54o 4o 1i 51i" probability="4"/>
                    <route id="route10" color="1,1,0" edges="54o 4o 2i 52i" probability="4"/>
                    <route id="route11" color="1,1,0" edges="54o 4o 3i 53i" probability="17"/>
                </routeDistribution>
                <routeDistribution id="r2" departSpeed="random">
                    <route id="route0" color="1,1,0" edges="51o 1o 4i 54i" probability="20"/>
                    <route id="route1" color="1,1,0" edges="51o 1o 2i 52i" probability="60"/>
                    <route id="route2" color="1,1,0" edges="51o 1o 3i 53i" probability="20"/>
                </routeDistribution>
                <routeDistribution id="r3" departSpeed="random">             
                    <route id="route6" color="1,1,0" edges="52o 2o 1i 51i" probability="60"/>
                    <route id="route7" color="1,1,0" edges="52o 2o 4i 54i" probability="20"/>
                    <route id="route8" color="1,1,0" edges="52o 2o 3i 53i" probability="20"/>                
                </routeDistribution>
                <routeDistribution id="r4" departSpeed="random">                
                    <route id="route3" color="1,1,0" edges="53o 3o 1i 51i" probability="20"/>
                    <route id="route4" color="1,1,0" edges="53o 3o 4i 54i" probability="60"/>
                    <route id="route5" color="1,1,0" edges="53o 3o 2i 52i" probability="20"/>                                
                </routeDistribution>
                <routeDistribution id="r5" departSpeed="random">                                                
                    <route id="route9" color="1,1,0" edges="54o 4o 1i 51i" probability="20"/>
                    <route id="route10" color="1,1,0" edges="54o 4o 2i 52i" probability="20"/>
                    <route id="route11" color="1,1,0" edges="54o 4o 3i 53i" probability="60"/>
                </routeDistribution>             
            </routes>                      
            <flow id="mixed0" begin="0" number="1" vehsPerHour="1000" route="r0" type="mixed3" departLane="random" departPosLat="random"/>
            <flow id="mixed5" begin="100" number="500" vehsPerHour="1000" route="r5" type="mixed1" departLane="random" departPosLat="random"/>
            <flow id="mixed1" begin="100" number="500" vehsPerHour="1000" route="r4" type="mixed1" departLane="random" departPosLat="random"/>
            <flow id="mixed3" begin="100" number="500" vehsPerHour="1000" route="r3" type="mixed1" departLane="random" departPosLat="random"/>
            <flow id="mixed4" begin="100" number="500" vehsPerHour="1000" route="r2" type="mixed1" departLane="random" departPosLat="random"/>""", file=routes)
        print("</routes>", file=routes)
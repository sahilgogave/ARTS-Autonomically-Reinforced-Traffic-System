from __future__ import absolute_import
from __future__ import print_function
import numpy as np
import tqdm
import os
import sys
import optparse
import shutil
import pickle
from PyQt5 import QtWidgets, QtCore
import threading
from routefile_generate import generate_test, generate_train
from agent import Agent
import pickle

episodes = 20000
PRE_TRAIN_STEPS = 500
epsilon_decay = 0.0001

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa

def get_options():
    """Get the command line options for TraCI-SUMO interface"""
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options

def vehnums(phase, X):
    """Get the number of vehicles in each lane"""
    phase = phase // 2
    x = np.zeros((4, 6))

    x[3, 0] = traci.lanearea.getLastStepVehicleNumber("401") + traci.lanearea.getLastStepVehicleNumber("400")
    x[3, 1] = traci.lanearea.getLastStepVehicleNumber("411") + traci.lanearea.getLastStepVehicleNumber("410")
    x[3, 2] = traci.lanearea.getLastStepVehicleNumber("421") + traci.lanearea.getLastStepVehicleNumber("420")
    x[3, 3] = traci.lanearea.getLastStepVehicleNumber("431") + traci.lanearea.getLastStepVehicleNumber("430")

    x[2, 0] = traci.lanearea.getLastStepVehicleNumber("301") + traci.lanearea.getLastStepVehicleNumber("300")
    x[2, 1] = traci.lanearea.getLastStepVehicleNumber("311") + traci.lanearea.getLastStepVehicleNumber("310")
    x[2, 2] = traci.lanearea.getLastStepVehicleNumber("321") + traci.lanearea.getLastStepVehicleNumber("320")
    x[2, 3] = traci.lanearea.getLastStepVehicleNumber("331") + traci.lanearea.getLastStepVehicleNumber("330")

    x[1, 0] = traci.lanearea.getLastStepVehicleNumber("201") + traci.lanearea.getLastStepVehicleNumber("200")
    x[1, 1] = traci.lanearea.getLastStepVehicleNumber("211") + traci.lanearea.getLastStepVehicleNumber("210")
    x[1, 2] = traci.lanearea.getLastStepVehicleNumber("221") + traci.lanearea.getLastStepVehicleNumber("220")
    x[1, 3] = traci.lanearea.getLastStepVehicleNumber("231") + traci.lanearea.getLastStepVehicleNumber("230")

    x[0, 0] = traci.lanearea.getLastStepVehicleNumber("101") + traci.lanearea.getLastStepVehicleNumber("100")
    x[0, 1] = traci.lanearea.getLastStepVehicleNumber("111") + traci.lanearea.getLastStepVehicleNumber("110")
    x[0, 2] = traci.lanearea.getLastStepVehicleNumber("121") + traci.lanearea.getLastStepVehicleNumber("120")
    x[0, 3] = traci.lanearea.getLastStepVehicleNumber("131") + traci.lanearea.getLastStepVehicleNumber("130")

    X = np.zeros((6, 24))
    X[phase] = np.squeeze(x.reshape(24, 1))/100

    return X.reshape(144, 1), X

def normalrun(ft=40):
    """Run the road network simulation with constant signal timing"""
    steps = 0
    phase = 0
    durs = 0
    vehsp = []
    vehlist = {}

    while traci.simulation.getMinExpectedNumber() > 0:
        if durs <= 0:
            traci.trafficlight.setPhase("0", phase)
            if phase % 2 == 0:
                traci.trafficlight.setPhaseDuration("0", 3)
                durs = 3

            else:
                traci.trafficlight.setPhaseDuration("0", ft)
                durs = ft

            phase = (phase + 1) % 12

        traci.simulationStep()

        if durs > 0:
            durs -= 1
        steps += 1

    return steps, vehsp

def normalrunreward(ft = 40):
    """Run the road network simulation with constant signal timing and calculate reward"""
    steps = 0
    phase = 0
    durs = 0
    tots1 = 0
    tots = 0
    totreward = 0
    count = 0

    while traci.simulation.getMinExpectedNumber() > 0:
        if durs <= 0:
            traci.trafficlight.setPhase("0", phase)
            if phase % 2 == 0:
                traci.trafficlight.setPhaseDuration("0", 3)
                durs = 3
                tots1 = 0
                for i in traci.vehicle.getIDList():
                    tots1 += traci.vehicle.getWaitingTime(i)
            else:
                if steps > 3:
                    reward = tots - tots1
                    totreward += reward
                    count += 1

                tots = 0
                for i in traci.vehicle.getIDList():
                    tots += traci.vehicle.getWaitingTime(i)
                traci.trafficlight.setPhaseDuration("0", ft)
                durs = ft

            phase = (phase + 1) % 12

        traci.simulationStep()

        if durs > 0:
            durs -= 1
        steps += 1

    return steps, totreward

def trainagent():
    """Pretrain the model"""
    print("-------------train---------------")
    epsilon = 1
    epsilon_min = 0.01
    agent = Agent()

    for episode in tqdm.tqdm(range(episodes), ascii=True, unit="episode"):
        totreward = 0
        step = 0
        done = False
        generate_train(episode % 50)

        if episode < 50:
            traci.load(["--start", "-c", "data/cross.sumocfg", "--tripinfo-output", "tripinfo.xml"])
            cons, _ = normalrun()
            print("\ncons {}".format(cons))
            shutil.copy("tripinfo.xml", f"trips/tripinfoprim{episode}.xml")

        traci.load(["--start", "-c", "data/cross.sumocfg", "--tripinfo-output", "tripinfo.xml"])
        phase = 0
        durs = 0
        tots = 0
        current_state = 0
        next_state = 0
        tots1 = 0
        X = np.zeros((6, 24))
        action = 0

        while traci.simulation.getMinExpectedNumber() > 0:
            if durs <= 0:
                if phase % 2 == 0:
                    traci.trafficlight.setPhase("0", phase)
                    traci.trafficlight.setPhaseDuration("0", 3)
                    durs = 3
                    if step > 3:
                        tots1 = 0
                        for i in traci.vehicle.getIDList():
                            tots1 += traci.vehicle.getAccumulatedWaitingTime(i)
                else:
                    if step > 3:
                        reward = (tots - tots1)
                        totreward += reward
                        next_state, X = vehnums(phase, X)
                        agent.update_replay_memory((current_state, action, reward, next_state, done))

                        if PRE_TRAIN_STEPS < step:
                            agent.train(done)
                        current_state = next_state

                    if step <= 3:
                        current_state, X = vehnums(phase, X)

                    if np.random.random() <= epsilon:
                        action = np.random.randint(0, 48)
                    else:
                        action = np.argmax(agent.get_qs(current_state.reshape(1, 144)))
                        print("sugg-time {}".format(action + 2))

                    tots = 0
                    for i in traci.vehicle.getIDList():
                        tots += traci.vehicle.getAccumulatedWaitingTime(i)

                    traci.trafficlight.setPhase("0", phase)
                    durs = action + 2
                    traci.trafficlight.setPhaseDuration("0", action + 2)

                phase = (phase + 1) % 12

            traci.simulationStep()

            if durs > 0:
                durs -= 1
            step += 1

        print("\nepisode - {}, epsilon-{}, steps={}\n".format(episode, epsilon, step))
        shutil.copy("tripinfo.xml", f"trips/tripinfo-{episode}.xml")
        done = True
        agent.update_replay_memory((current_state, action, 0, next_state, done))
        agent.train(done)

        if (episode + 1) % 500 == 0:
            if not os.path.isdir('models'):
                os.mkdir('models')
            agent.network.save(f'models/dddqn_traffic_{episode + 1}.model')

        if epsilon > epsilon_min:
            epsilon -= epsilon_decay
            epsilon = max(epsilon, epsilon_min)

    agent.network.save(f'models/dddqn_traffic_pre_trained.model')

def trainmid():
    """Training the pre-trained model"""
    print("-------------train---------------")
    agent = Agent()
    agent.network.load_weights(f'models/dddqn_traffic_pre_trained.model')
    epsilon = 0.01
    episodes = 10000
    rewardspa = []

    for episode in tqdm.tqdm(range(episodes), ascii=True, unit="episode"):
        totreward = 0
        step = 0
        done = False
        generate_train(episode % 10)

        if episode < 10:
            traci.load(["--start", "-c", "data/cross.sumocfg", "--tripinfo-output", "tripinfo.xml"])
            cons, _ = normalrun()
            print("\ncons {}".format(cons))
            shutil.copy("tripinfo.xml", f"tripsdqn/tripinfoprim{episode}.xml")

        traci.load(["--start", "-c", "data/cross.sumocfg", "--tripinfo-output", "tripinfo.xml"])
        phase = 0
        durs = 0
        tots = 0
        current_state = 0
        next_state = 0
        tots1 = 0
        X = np.zeros((6, 24))
        action = 0
        count = 0

        while traci.simulation.getMinExpectedNumber() > 0:
            if durs <= 0:
                if phase % 2 == 0:
                    traci.trafficlight.setPhase("0", phase)
                    traci.trafficlight.setPhaseDuration("0", 3)
                    durs = 3
                    if step > 3:
                        tots1 = 0
                        for i in traci.vehicle.getIDList():
                            tots1 += traci.vehicle.getWaitingTime(i)

                else:
                    if step > 3:
                        reward = (tots - tots1)
                        totreward += reward
                        next_state, X = vehnums(phase, X)
                        agent.update_replay_memory((current_state, action, reward, next_state, done))

                        if PRE_TRAIN_STEPS < step:
                            agent.train(done)
                        current_state = next_state

                    if step <= 3:
                        current_state, X = vehnums(phase, X)
                    if np.random.random() <= epsilon:
                        action = np.random.randint(0, 48)
                    else:
                        action = np.argmax(agent.get_qs(current_state.reshape(1, 144)))
                        print("sugg-time {}".format(action + 2))

                    count += 1
                    tots = 0
                    for i in traci.vehicle.getIDList():
                        tots += traci.vehicle.getWaitingTime(i)

                    traci.trafficlight.setPhase("0", phase)
                    durs = action + 2
                    traci.trafficlight.setPhaseDuration("0", action + 2)

                phase = (phase + 1) % 12

            traci.simulationStep()

            if durs > 0:
                durs -= 1
            step += 1

        rewardspa.append(totreward/count)
        print("\nepisode - {}, epsilon-{}, steps={}\n".format(episode, epsilon, step))
        shutil.copy("tripinfo.xml", f"tripsdqn/tripinfo-{episode}.xml")
        done = True
        agent.update_replay_memory((current_state, action, 0, next_state, done))
        agent.train(done)

        if (episode + 1) % 500 == 0:
            if not os.path.isdir('rewards'):
                os.mkdir('rewards')
            file = open("rewards/reward.bin", "wb")
            pickle.dump(rewardspa, file)
            file.close()
            if not os.path.isdir('models'):
                os.mkdir('models')
            agent.network.save(f'models/dddqn_traffic_20K+{episode + 1}.model')

def testmodels():
    """Test all stored models to select the best one"""
    agent = Agent()
    l = []
    for j in os.listdir("models/"):
        agent.network.load_weights(f"models/{j}")
        st = []
        co = []

        for i in range(100):
            generate_train(i)
            if i < 100:
                traci.load(["--start", "-c", "data/cross.sumocfg", "--tripinfo-output", "tripinfo.xml"])
                cons, _ = normalrun()
                co.append(cons)

            traci.load(["--start", "-c", "data/cross.sumocfg", "--tripinfo-output", "tripinfo.xml"])
            step = 0
            phase = 0
            durs = 0
            current_state = 0
            X = np.zeros((6, 24))

            while traci.simulation.getMinExpectedNumber() > 0:
                if durs <= 0:
                    if phase % 2 == 0:
                        traci.trafficlight.setPhase("0", phase)
                        traci.trafficlight.setPhaseDuration("0", 3)
                        durs = 3

                    else:
                        current_state, X = vehnums(phase, X)
                        action = np.argmax(agent.get_qs(current_state.reshape(1, 144)))
                        traci.trafficlight.setPhase("0", phase)
                        durs = action + 2
                        traci.trafficlight.setPhaseDuration("0", action + 2)

                    phase = (phase + 1) % 12

                traci.simulationStep()

                if durs > 0:
                    durs -= 1
                step += 1
            st.append(step)

        print(f" steps - {np.mean(st)} cons - {np.mean(co)} model - {j}")
        l.append((np.mean(st), np.mean(co), j))

    for i in l:
        print(i)

def test():
    """Test the best model against static traffic light systems"""

    agent = Agent()
    flag = 0
    agent.network.load_weights(f"models/dddqn_traffic_20K+1000.model")      # this was the best model that we obtained in our runs
    st = []
    co = []

    for i in tqdm.tqdm(range(100), ascii=True, unit="episode"):
        generate_train(i)
        if i < 100:
            cons = 0
            traci.load(["--start", "-c", "data/cross.sumocfg", "--tripinfo-output", "tripinfo.xml"])
            cons, x = normalrun(10)
            co.append(cons)
            print("\ncons {}".format(cons))

        traci.load(["--start", "-c", "data/cross.sumocfg", "--tripinfo-output", "tripinfo.xml"])
        step = 0
        phase = 0
        durs = 0

        current_state = 0
        X = np.zeros((6, 24))

        def get_small_gui():
            app = QtWidgets.QApplication(sys.argv)
            main = QtWidgets.QFrame()
            main.setGeometry(1200, 400, 450, 120)
            main.setStyleSheet("QLabel{font-size:20px;}")
            l1 = QtWidgets.QLabel("0.00000", main)
            l1.setGeometry(0, 0, 300, 40)
            l2 = QtWidgets.QLabel("South", main)
            l2.setGeometry(0, 40, 300, 40)
            l3 = QtWidgets.QLabel("Yellow", main)
            l3.setGeometry(0, 80, 450, 40)

            def getphasename(phase):
                color = "yellow"
                lanes = {0: "South", 1: "South-North", 2: "North", 3: "West", 4: "West-East", 5: "East"}
                if phase % 2 == 0:
                    color = "green"

                return color, lanes[(phase - 1) % 12 // 2]

            def changet():
                l1.setText(f"Time remaining for change: {durs}")

                color, lane = getphasename(phase)
                l2.setText(f"LANE: {lane} activated")
                l3.setText(f"LANE {lane} is running on {color.upper()} light")

            main.show()
            timer = QtCore.QTimer()
            timer.timeout.connect(changet)
            timer.start(1)
            sys.exit(app.exec_())

        if flag == 0:
            thread = threading.Thread(target=get_small_gui)
            thread.start()
            flag = 1

        while traci.simulation.getMinExpectedNumber() > 0:
            if durs <= 0:
                if phase % 2 == 0:
                    traci.trafficlight.setPhase("0", phase)
                    traci.trafficlight.setPhaseDuration("0", 3)
                    durs = 3

                else:
                    current_state, X = vehnums(phase, X)
                    action = np.argmax(agent.get_qs(current_state.reshape(1, 144)))
                    traci.trafficlight.setPhase("0", phase)
                    durs = action + 2
                    traci.trafficlight.setPhaseDuration("0", action + 2)

                phase = (phase + 1) % 12

            traci.simulationStep()
            if durs > 0:
                durs -= 1
            step += 1

        st.append(step)

    print(f" avg steps - {np.mean(st)} avg cons - {np.mean(co)}")

if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # first, generate the route file for this simulation
    generate_train(0)   # random seed = 0
    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, "-c", "data/cross.sumocfg", "--tripinfo-output", "tripinfo.xml"])

    trainagent()        # pre-train the agent
    trainmid()          # tune the pre-trained agent model
    # generate_test(2)    # generate specific phasewise test cases for scenario testing
    test()              # test the model
    print(end="\n\n\n")
    traci.close()
    sys.stdout.flush()
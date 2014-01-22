from controller import Supervisor
import optimization.webots as optimization

import random

class optimize(Supervisor):
    def __init__(self):
        Supervisor.__init__(self)
        self.opti = optimization.Webots()

        if self.opti:
            print('Optimization mode!')

            print('Settings:')

            for s in self.opti.settings:
                print('  {0}: {1}'.format(s, self.opti.settings[s]))

            print('Parameters:')

            for s in self.opti.parameters:
                print('  {0}: {1}'.format(s, self.opti.parameters[s].value))
        else:
            print('Not in optimization mode... :(')

    def run(self):
        t = 0
        dt = 1.0 / self.getBasicTimeStep()

        while True:
            if self.step(int(self.getBasicTimeStep())) == -1:
                break

            t += dt

            if t > 3:
                break

        if self.opti:
            self.opti.respond({
                'f1': random.random(),
                'f2': random.random()
            })

            self.simulationQuit(0)

controller = optimize()
controller.run()

# vi:ts=4:et

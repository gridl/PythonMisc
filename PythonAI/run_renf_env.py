import argparse
import gym

def build_arg_parser():
    parser = argparse.ArgumentParser(description='run an environment')
    parser.add_argument('--input-env', dest='input_env', required=True,choices=['cartpole','mountaincar','pendulum','taxi','lake'],help='specify the name of the environment')

    return parser


if __name__ =='__main__':
    args = build_arg_parser().parse_args()
    input_env = args.input_env

    name_map = {'cartpole':'Cartpole-v0',
                'mountaincar': 'MountainCar-v0',
                'pendulum': 'Pendulum-v0',
                'taxi': 'Taxi-v1',
                'lake':'FrozenLake-v0'

                }

    #create environment and reset

    env = gym.make(name_map[input_env])
    env.reset()

    #Iterate 1000 times
    for _ in range(1000):
        env.render()

        # take a random action
        env.step(env.action_space.sample())


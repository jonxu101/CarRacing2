from gym.envs.registration import register

register(
    id='Racing-v0',
    entry_point='gym_race.envs:RaceEnv',
)
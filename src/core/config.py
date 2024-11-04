from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
SERVICE_BASE_URL = env.str('SERVICE_BASE_URL')

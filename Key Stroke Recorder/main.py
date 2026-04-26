import logging

logging.basicConfig(filename='dataKey.txt', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')

def keylogger():
  try:
    while True:
      key = input("Press any key to log:")
      logging.debug(f'Key pressed: {key}')
  except KeyboardInterrupt:
    logging.info('Program terminated by user.')
    print("Logging completed.") 

if __name__ == '__main__':
  keylogger()

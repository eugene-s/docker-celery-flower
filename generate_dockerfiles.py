import os

if __name__ == '__main__':
    with open('./Dockerfile.txt', mode='r') as dockerfile_template_file:
        dockerfile_template = dockerfile_template_file.read()
    brokers_file = open('brokers.txt', mode='r')

    for broker in brokers_file.readlines():
        broker_cleaned = broker.strip('\n')
        if not os.path.exists(broker_cleaned):
            os.mkdir(broker_cleaned)
        with open(f'./{broker_cleaned}/Dockerfile', 'w+') as dockerfile:
            dockerfile.write(dockerfile_template.format(broker_type=broker_cleaned))

    brokers_file.close()

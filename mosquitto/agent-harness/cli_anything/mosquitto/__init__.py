import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['mosquitto', '-d'])
@cli.command()
@click.argument('topic')
def subscribe(topic): subprocess.run(['mosquitto_sub', '-t', topic])
@cli.command()
@click.argument('topic')
@click.argument('message')
def publish(topic, message): subprocess.run(['mosquitto_pub', '-t', topic, '-m', message])
if __name__ == '__main__': cli()

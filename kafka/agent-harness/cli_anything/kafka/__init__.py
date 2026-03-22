import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def topics(): subprocess.run(['kafka-topics', '--list', '--bootstrap-server', 'localhost:9092'])
@cli.command()
@click.argument('topic')
def create(topic): subprocess.run(['kafka-topics', '--create', '--topic', topic, '--bootstrap-server', 'localhost:9092'])
if __name__ == '__main__': cli()

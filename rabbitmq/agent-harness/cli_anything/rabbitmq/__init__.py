import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['rabbitmqctl', 'status'])
@cli.command()
def queues(): subprocess.run(['rabbitmqctl', 'list_queues'])
@cli.command()
def vhosts(): subprocess.run(['rabbitmqctl', 'list_vhosts'])
if __name__ == '__main__': cli()

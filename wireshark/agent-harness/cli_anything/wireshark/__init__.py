import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.option('-i', '--interface', default='eth0')
@click.option('-c', '--count', default=100)
def capture(interface, count): subprocess.run(['tshark', '-i', interface, '-c', str(count)])
@cli.command()
@click.argument('file')
def read(file): subprocess.run(['tshark', '-r', file])
if __name__ == '__main__': cli()

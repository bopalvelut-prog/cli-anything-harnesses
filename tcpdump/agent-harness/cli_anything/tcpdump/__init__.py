import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def capture(): subprocess.run(['tcpdump', '-i', 'eth0', '-c', '100'])
@cli.command()
def port(): subprocess.run(['tcpdump', 'port', '80'])
if __name__ == '__main__': cli()

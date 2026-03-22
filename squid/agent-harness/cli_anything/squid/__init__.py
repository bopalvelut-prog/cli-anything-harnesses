import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['squid', '-k', 'parse'])
@cli.command()
def restart(): subprocess.run(['squid', '-k', 'reconfigure'])
if __name__ == '__main__': cli()

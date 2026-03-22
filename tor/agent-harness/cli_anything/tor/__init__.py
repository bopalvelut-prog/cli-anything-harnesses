import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['tor', '--runas', 'debian-tor'])
@cli.command()
def stop(): subprocess.run(['tor', '--shutdown'])
@cli.command()
def circuit(): click.echo('Current Tor circuit')
if __name__ == '__main__': cli()

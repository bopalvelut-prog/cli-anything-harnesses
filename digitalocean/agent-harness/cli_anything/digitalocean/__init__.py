import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['doctl', 'auth', 'init'])
@cli.command()
def droplets(): subprocess.run(['doctl', 'compute', 'droplet', 'list'])
if __name__ == '__main__': cli()

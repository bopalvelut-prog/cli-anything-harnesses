import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['ufw', 'status'])
@cli.command()
@click.argument('port')
def allow(port): subprocess.run(['ufw', 'allow', port])
@cli.command()
@click.argument('port')
def deny(port): subprocess.run(['ufw', 'deny', port])
@cli.command()
def enable(): subprocess.run(['ufw', 'enable'])
if __name__ == '__main__': cli()

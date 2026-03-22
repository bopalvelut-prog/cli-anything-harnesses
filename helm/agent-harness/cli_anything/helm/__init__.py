import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def install(): subprocess.run(['helm', 'install', 'my-chart', '.'])
@cli.command()
def upgrade(): subprocess.run(['helm', 'upgrade', 'my-chart', '.'])
@cli.command()
def list(): subprocess.run(['helm', 'list'])
@cli.command()
def uninstall(): subprocess.run(['helm', 'uninstall', 'my-chart'])
if __name__ == '__main__': cli()

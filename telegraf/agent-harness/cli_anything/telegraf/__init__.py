import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def test(): subprocess.run(['telegraf', '--test'])
@cli.command()
def start(): subprocess.run(['telegraf', '--config', '/etc/telegraf/telegraf.conf'])
@cli.command()
def config(): subprocess.run(['telegraf', 'config'])
if __name__ == '__main__': cli()

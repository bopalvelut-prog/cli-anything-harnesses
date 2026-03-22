import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def test(): subprocess.run(['filebeat', 'test', 'config'])
@cli.command()
def start(): subprocess.run(['filebeat', '-e'])
@cli.command()
def modules(): subprocess.run(['filebeat', 'modules', 'list'])
if __name__ == '__main__': cli()

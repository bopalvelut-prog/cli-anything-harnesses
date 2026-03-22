import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['symfony', 'server:start'])
@cli.command()
def console(): subprocess.run(['bin/console'])
if __name__ == '__main__': cli()

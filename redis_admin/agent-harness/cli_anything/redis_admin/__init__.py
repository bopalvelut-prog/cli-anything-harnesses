import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def info(): subprocess.run(['redis-cli', 'info'])
@cli.command()
def monitor(): subprocess.run(['redis-cli', 'monitor'])
if __name__ == '__main__': cli()

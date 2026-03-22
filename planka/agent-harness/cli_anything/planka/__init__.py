import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['planka', 'start'])
@cli.command()
def boards(): click.echo('Planka boards')
if __name__ == '__main__': cli()

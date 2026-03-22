import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def connect(): subprocess.run(['mysql', '-u', 'root'])
@cli.command()
def status(): click.echo('MySQL running')
if __name__ == '__main__': cli()

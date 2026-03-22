import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def upload(): click.echo('Swarm upload')
@cli.command()
def download(): click.echo('Swarm download')
if __name__ == '__main__': cli()

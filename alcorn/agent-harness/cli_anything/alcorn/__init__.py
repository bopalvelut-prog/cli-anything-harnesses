import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alcorn running')
@cli.command()
def start(): click.echo('alcorn started')
if __name__ == '__main__': cli()

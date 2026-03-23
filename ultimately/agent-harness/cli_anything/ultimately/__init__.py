import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ultimately running')
@cli.command()
def start(): click.echo('ultimately started')
if __name__ == '__main__': cli()

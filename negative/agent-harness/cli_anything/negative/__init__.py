import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('negative running')
@cli.command()
def start(): click.echo('negative started')
if __name__ == '__main__': cli()

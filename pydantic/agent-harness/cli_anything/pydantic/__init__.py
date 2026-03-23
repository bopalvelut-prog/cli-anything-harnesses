import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pydantic running')
@cli.command()
def start(): click.echo('pydantic started')
if __name__ == '__main__': cli()

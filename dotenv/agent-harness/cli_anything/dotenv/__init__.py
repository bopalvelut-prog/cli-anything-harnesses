import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dotenv running')
@cli.command()
def start(): click.echo('dotenv started')
if __name__ == '__main__': cli()

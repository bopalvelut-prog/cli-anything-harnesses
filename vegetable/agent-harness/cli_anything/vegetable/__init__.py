import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vegetable running')
@cli.command()
def start(): click.echo('vegetable started')
if __name__ == '__main__': cli()

import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gear running')
@cli.command()
def start(): click.echo('gear started')
if __name__ == '__main__': cli()

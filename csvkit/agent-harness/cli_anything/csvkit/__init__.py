import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('csvkit running')
@cli.command()
def start(): click.echo('csvkit started')
if __name__ == '__main__': cli()

import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('balanced running')
@cli.command()
def start(): click.echo('balanced started')
if __name__ == '__main__': cli()

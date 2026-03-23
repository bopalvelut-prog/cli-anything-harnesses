import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('book running')
@cli.command()
def start(): click.echo('book started')
if __name__ == '__main__': cli()

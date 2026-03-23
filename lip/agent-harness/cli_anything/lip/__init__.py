import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lip running')
@cli.command()
def start(): click.echo('lip started')
if __name__ == '__main__': cli()

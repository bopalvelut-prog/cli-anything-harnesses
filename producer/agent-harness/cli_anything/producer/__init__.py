import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('producer running')
@cli.command()
def start(): click.echo('producer started')
if __name__ == '__main__': cli()

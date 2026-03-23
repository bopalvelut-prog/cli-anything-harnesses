import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('brendangregg running')
@cli.command()
def start(): click.echo('brendangregg started')
if __name__ == '__main__': cli()

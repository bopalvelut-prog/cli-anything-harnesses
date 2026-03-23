import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('paint running')
@cli.command()
def start(): click.echo('paint started')
if __name__ == '__main__': cli()

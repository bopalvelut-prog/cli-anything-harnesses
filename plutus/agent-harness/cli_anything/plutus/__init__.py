import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plutus running')
@cli.command()
def start(): click.echo('plutus started')
if __name__ == '__main__': cli()

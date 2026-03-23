import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('funny running')
@cli.command()
def start(): click.echo('funny started')
if __name__ == '__main__': cli()

import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('better running')
@cli.command()
def start(): click.echo('better started')
if __name__ == '__main__': cli()

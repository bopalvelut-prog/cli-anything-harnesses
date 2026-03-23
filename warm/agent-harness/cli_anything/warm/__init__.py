import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('warm running')
@cli.command()
def start(): click.echo('warm started')
if __name__ == '__main__': cli()

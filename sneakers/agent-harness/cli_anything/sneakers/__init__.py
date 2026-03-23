import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sneakers running')
@cli.command()
def start(): click.echo('sneakers started')
if __name__ == '__main__': cli()

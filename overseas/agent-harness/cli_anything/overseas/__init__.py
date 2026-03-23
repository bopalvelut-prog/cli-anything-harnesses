import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('overseas running')
@cli.command()
def start(): click.echo('overseas started')
if __name__ == '__main__': cli()

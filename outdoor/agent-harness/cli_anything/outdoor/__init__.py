import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('outdoor running')
@cli.command()
def start(): click.echo('outdoor started')
if __name__ == '__main__': cli()

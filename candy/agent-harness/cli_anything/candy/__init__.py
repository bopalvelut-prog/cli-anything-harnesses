import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('candy running')
@cli.command()
def start(): click.echo('candy started')
if __name__ == '__main__': cli()

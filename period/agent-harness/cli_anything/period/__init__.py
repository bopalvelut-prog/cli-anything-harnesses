import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('period running')
@cli.command()
def start(): click.echo('period started')
if __name__ == '__main__': cli()

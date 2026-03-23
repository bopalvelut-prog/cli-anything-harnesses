import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('smell running')
@cli.command()
def start(): click.echo('smell started')
if __name__ == '__main__': cli()

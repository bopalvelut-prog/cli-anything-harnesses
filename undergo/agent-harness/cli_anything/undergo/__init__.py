import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('undergo running')
@cli.command()
def start(): click.echo('undergo started')
if __name__ == '__main__': cli()

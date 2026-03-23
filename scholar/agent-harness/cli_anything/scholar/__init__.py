import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scholar running')
@cli.command()
def start(): click.echo('scholar started')
if __name__ == '__main__': cli()

import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quickcheck running')
@cli.command()
def start(): click.echo('quickcheck started')
if __name__ == '__main__': cli()

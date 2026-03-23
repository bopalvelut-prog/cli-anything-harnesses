import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('least running')
@cli.command()
def start(): click.echo('least started')
if __name__ == '__main__': cli()

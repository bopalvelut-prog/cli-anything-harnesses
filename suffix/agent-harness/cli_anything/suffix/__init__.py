import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('suffix running')
@cli.command()
def start(): click.echo('suffix started')
if __name__ == '__main__': cli()

import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cool running')
@cli.command()
def start(): click.echo('cool started')
if __name__ == '__main__': cli()

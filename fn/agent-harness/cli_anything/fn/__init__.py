import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fn running')
@cli.command()
def start(): click.echo('fn started')
if __name__ == '__main__': cli()

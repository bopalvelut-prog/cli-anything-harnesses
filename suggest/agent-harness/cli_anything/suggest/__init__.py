import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('suggest running')
@cli.command()
def start(): click.echo('suggest started')
if __name__ == '__main__': cli()

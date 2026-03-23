import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('adaptive running')
@cli.command()
def start(): click.echo('adaptive started')
if __name__ == '__main__': cli()

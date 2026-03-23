import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cousin running')
@cli.command()
def start(): click.echo('cousin started')
if __name__ == '__main__': cli()

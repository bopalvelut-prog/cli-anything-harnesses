import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('topology running')
@cli.command()
def start(): click.echo('topology started')
if __name__ == '__main__': cli()

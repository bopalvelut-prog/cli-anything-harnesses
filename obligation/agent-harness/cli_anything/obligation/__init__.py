import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('obligation running')
@cli.command()
def start(): click.echo('obligation started')
if __name__ == '__main__': cli()

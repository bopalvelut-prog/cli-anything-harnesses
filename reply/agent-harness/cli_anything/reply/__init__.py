import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reply running')
@cli.command()
def start(): click.echo('reply started')
if __name__ == '__main__': cli()

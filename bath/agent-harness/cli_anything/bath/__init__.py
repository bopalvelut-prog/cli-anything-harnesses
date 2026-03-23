import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bath running')
@cli.command()
def start(): click.echo('bath started')
if __name__ == '__main__': cli()

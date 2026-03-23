import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mind running')
@cli.command()
def start(): click.echo('mind started')
if __name__ == '__main__': cli()

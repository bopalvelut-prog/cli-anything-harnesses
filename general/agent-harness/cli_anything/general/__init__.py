import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('general running')
@cli.command()
def start(): click.echo('general started')
if __name__ == '__main__': cli()

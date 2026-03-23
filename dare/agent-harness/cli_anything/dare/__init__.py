import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dare running')
@cli.command()
def start(): click.echo('dare started')
if __name__ == '__main__': cli()

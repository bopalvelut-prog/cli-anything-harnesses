import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('workplace running')
@cli.command()
def start(): click.echo('workplace started')
if __name__ == '__main__': cli()

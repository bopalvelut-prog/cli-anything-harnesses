import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('settlement running')
@cli.command()
def start(): click.echo('settlement started')
if __name__ == '__main__': cli()

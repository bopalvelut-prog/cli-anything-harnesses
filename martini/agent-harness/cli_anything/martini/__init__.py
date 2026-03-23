import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('martini running')
@cli.command()
def start(): click.echo('martini started')
if __name__ == '__main__': cli()

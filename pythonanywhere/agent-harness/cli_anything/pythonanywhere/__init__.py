import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pythonanywhere running')
@cli.command()
def start(): click.echo('pythonanywhere started')
if __name__ == '__main__': cli()

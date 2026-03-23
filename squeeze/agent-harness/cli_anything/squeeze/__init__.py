import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('squeeze running')
@cli.command()
def start(): click.echo('squeeze started')
if __name__ == '__main__': cli()

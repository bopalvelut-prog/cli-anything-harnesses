import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sector running')
@cli.command()
def start(): click.echo('sector started')
if __name__ == '__main__': cli()

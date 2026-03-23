import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('court running')
@cli.command()
def start(): click.echo('court started')
if __name__ == '__main__': cli()

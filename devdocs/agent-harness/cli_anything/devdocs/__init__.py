import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('devdocs running')
@cli.command()
def start(): click.echo('devdocs started')
if __name__ == '__main__': cli()

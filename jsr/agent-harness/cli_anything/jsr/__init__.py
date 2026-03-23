import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jsr running')
@cli.command()
def start(): click.echo('jsr started')
if __name__ == '__main__': cli()

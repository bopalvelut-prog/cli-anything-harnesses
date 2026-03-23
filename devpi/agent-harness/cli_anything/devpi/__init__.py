import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('devpi running')
@cli.command()
def start(): click.echo('devpi started')
if __name__ == '__main__': cli()

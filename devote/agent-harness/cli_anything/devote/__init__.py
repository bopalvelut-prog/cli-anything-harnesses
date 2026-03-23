import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('devote running')
@cli.command()
def start(): click.echo('devote started')
if __name__ == '__main__': cli()

import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('devfile running')
@cli.command()
def start(): click.echo('devfile started')
if __name__ == '__main__': cli()

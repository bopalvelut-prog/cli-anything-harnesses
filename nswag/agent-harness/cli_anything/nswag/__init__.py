import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nswag running')
@cli.command()
def start(): click.echo('nswag started')
if __name__ == '__main__': cli()

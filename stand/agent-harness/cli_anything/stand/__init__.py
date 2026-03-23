import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stand running')
@cli.command()
def start(): click.echo('stand started')
if __name__ == '__main__': cli()

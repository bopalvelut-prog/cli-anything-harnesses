import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stupid running')
@cli.command()
def start(): click.echo('stupid started')
if __name__ == '__main__': cli()

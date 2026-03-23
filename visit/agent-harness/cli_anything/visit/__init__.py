import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('visit running')
@cli.command()
def start(): click.echo('visit started')
if __name__ == '__main__': cli()

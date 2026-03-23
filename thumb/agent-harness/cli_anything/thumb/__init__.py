import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thumb running')
@cli.command()
def start(): click.echo('thumb started')
if __name__ == '__main__': cli()

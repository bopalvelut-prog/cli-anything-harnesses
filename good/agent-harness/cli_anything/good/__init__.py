import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('good running')
@cli.command()
def start(): click.echo('good started')
if __name__ == '__main__': cli()

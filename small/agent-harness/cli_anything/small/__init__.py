import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('small running')
@cli.command()
def start(): click.echo('small started')
if __name__ == '__main__': cli()

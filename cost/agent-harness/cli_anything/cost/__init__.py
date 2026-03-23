import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cost running')
@cli.command()
def start(): click.echo('cost started')
if __name__ == '__main__': cli()

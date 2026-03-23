import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('proto running')
@cli.command()
def start(): click.echo('proto started')
if __name__ == '__main__': cli()

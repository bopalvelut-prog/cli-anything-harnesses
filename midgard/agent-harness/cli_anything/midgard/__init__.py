import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('midgard running')
@cli.command()
def start(): click.echo('midgard started')
if __name__ == '__main__': cli()

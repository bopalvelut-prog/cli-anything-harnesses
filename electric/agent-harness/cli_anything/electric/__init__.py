import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('electric running')
@cli.command()
def start(): click.echo('electric started')
if __name__ == '__main__': cli()
